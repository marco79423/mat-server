from unittest import mock

from mat_server.domain import entities, helpers, repositories
from mat_server.domain.use_cases import GetProxyServerResponseUseCase


def test_get_proxy_server_response():
    mat_config_repository = mock.MagicMock(spec=repositories.MatConfigRepositoryBase)
    mat_config_repository.get_proxy_host.return_value = 'https://paji.marco79423.net'

    request_helper = mock.MagicMock(spec=helpers.HTTPRequestHelperBase)
    request_helper.send.return_value = entities.HTTPResponse(
        raw_data=b'raw_data',
        status_code=200,
        headers={
            'Name': 'name',
            'connection': 'Close',
        },
    )

    uc = GetProxyServerResponseUseCase(
        mat_config_repository=mat_config_repository,
        request_helper=request_helper,
    )

    server_response = uc.execute(
        request=entities.ClientRequest(
            method='GET',
            path='path',
            query_string='name=name',
            headers={
                'Host': 'host',
                'Name': 'name',
            }
        )
    )

    assert server_response == entities.ServerResponse(
        raw_body=b'raw_data',
        status_code=200,
        headers={
            'Name': 'name',
        },
    )

    request_helper.send.assert_called_with(entities.HTTPRequest(
        url='https://paji.marco79423.net/path?name=name',
        method='GET',
        headers={
            'name': 'name',
        },
        raw_body=b'',
    ))


# class GetProxyServerResponseUseCase(base_types.UseCase):
#
#     def __init__(self,
#                  request_helper: helpers.HTTPRequestHelperBase):
#         self._request_helper = request_helper
#
#     def execute(self, request: entities.ClientRequest) -> entities.ServerResponse:
#         # 取得 Proxy Server Url
#         proxy_host = self._get_proxy_host()
#         proxy_url = f'{proxy_host}/{request.path}?{request.query_string}'
#
#         # 移除不必要的 Header
#         headers = request.headers.copy()
#         del headers['host']
#
#         # 取得 Proxy Server 的回傳值
#         http_response = self._request_helper.send(
#             entities.HTTPRequest(
#                 method=request.method,
#                 url=proxy_url,
#                 headers=headers,
#                 raw_body=request.raw_body,
#             )
#         )
#
#         # 將回傳值轉換為 mat Server 的回傳值
#         headers = {
#             name: value
#             for name, value in headers.items() if name not in HOP_BY_HOP_HEADERS
#         }
#
#         return entities.ServerResponse(
#             raw_data=http_response.raw_data,
#             headers=headers,
#             status_code=http_response.status_code,
#         )
#
#     @staticmethod
#     def _get_proxy_host():
#         return 'https://paji.marco79423.net'
