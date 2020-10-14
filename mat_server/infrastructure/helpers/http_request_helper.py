import requests

from mat_server.domain import helpers, entities


class HTTPRequestHelper(helpers.HTTPRequestHelperBase):

    def send(self, request: entities.HTTPRequest) -> entities.HTTPResponse:
        req = requests.Request(
            method=request.method,
            url=request.url,
            headers=request.headers,
            data=request.raw_body,
        )
        resp = requests.Session().send(req.prepare(), stream=True)

        headers = {}
        for name, value in resp.headers.items():
            headers[name.lower()] = value

        return entities.HTTPResponse(
            raw_data=resp.raw.read(),
            status_code=resp.status_code,
            headers=headers,
        )
