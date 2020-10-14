from typing import Dict, Any

from mat_server.domain import base_types


class HTTPRequest(base_types.Entity):

    def __init__(self,
                 url: str,
                 method: str = 'GET',
                 headers: Dict[str, str] = None,
                 raw_body: bytes = b''):
        self.url = url
        self.method = method
        self.headers = headers if headers is not None else {}
        self.raw_body = raw_body

    def __eq__(self, other: Any):
        if not isinstance(other, HTTPRequest):
            return False
        if self.url != other.url:
            return False
        if self.method != other.method:
            return False
        if self.headers != other.headers:
            return False
        if self.raw_body != other.raw_body:
            return False
        return True
