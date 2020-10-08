from typing import Dict, Tuple

import requests

from mat_server.domain import helpers


class RequestHelper(helpers.RequestHelperBase):

    def send(self,
             method: str,
             url: str,
             headers: Dict[str, str],
             raw_body: bytes) -> Tuple[bytes, int, Dict[str, str]]:

        req = requests.Request(
            method=method,
            url=url,
            headers=headers,
            data=raw_body,
        )
        resp = requests.Session().send(req.prepare(), stream=True)

        headers = {}
        for name, value in resp.headers.items():
            headers[name.lower()] = value

        return resp.raw.read(), resp.status_code, headers
