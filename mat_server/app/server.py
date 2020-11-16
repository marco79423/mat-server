from typing import Callable

import fastapi

from mat_server.domain import use_cases, entities


class Server:

    def __init__(self,
                 get_config_use_case: use_cases.GetConfigUseCase,
                 check_if_mock_response_exists_use_case: use_cases.CheckIfMockResponseExistsUseCase,
                 get_mock_response_use_case: use_cases.GetMockResponseUseCase,
                 get_proxy_server_response_use_case: use_cases.GetProxyServerResponseUseCase,
                 server_serve_func: Callable,
                 ):

        self._server_serve_func = server_serve_func

        def transform_response_to_fastapi_response(response: entities.ServerResponse):
            return fastapi.Response(
                content=response.raw_body,
                headers=response.headers,
                status_code=response.status_code,
            )

        self._app = fastapi.FastAPI()

        @self._app.get('/_mat')
        async def get_config():
            mat_config = get_config_use_case.execute()
            return mat_config.serialize()

        @self._app.api_route('/{path:path}')
        async def proxy(path, request: fastapi.Request):
            client_request = entities.ClientRequest(
                method=request.method,
                path=path,
                query_string=str(request.query_params),
                headers=dict(request.headers),
                raw_body=await request.body()
            )

            # 檢查是否需要 mock response
            existed = check_if_mock_response_exists_use_case.execute(client_request)

            # 如果需要 mock
            if existed:
                mock_response = get_mock_response_use_case.execute(client_request)
                return transform_response_to_fastapi_response(mock_response)

            # 如果不需要 mock，直接轉給 proxy server
            else:
                proxy_server_response = get_proxy_server_response_use_case.execute(client_request)
                return transform_response_to_fastapi_response(proxy_server_response)

    def serve(self, host: str, port: int):
        self._server_serve_func(self._app, host=host, port=port)
