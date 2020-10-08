from mat_server.domain import base_types, entities, helpers

HOP_BY_HOP_HEADERS = frozenset(
    (
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-authorization",
        "te",
        "trailers",
        "transfer-encoding",
        "upgrade",
    )
)


class GetProxyServerResponseUseCase(base_types.UseCase):

    def __init__(self,
                 request_helper: helpers.RequestHelperBase):
        self._request_helper = request_helper

    def execute(self, request: entities.Request) -> entities.Response:
        proxy_url = self._get_proxy_host()

        headers = request.headers.copy()
        del headers['host']

        raw_data, status_code, headers = self._request_helper.send(
            method=request.method,
            url=f'{proxy_url}/{request.path}?{request.query_string}',
            headers=headers,
            raw_body=request.raw_body,
        )

        headers = {
            name: value
            for name, value in headers.items() if name not in HOP_BY_HOP_HEADERS
        }

        return entities.Response(
            raw_data=raw_data,
            headers=headers,
            status_code=status_code,
        )

    @staticmethod
    def _get_proxy_host():
        return 'https://paji.marco79423.net'
