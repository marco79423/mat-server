from typing import Dict

from mat_server.domain import base_types


class Request(base_types.Entity):
    def __init__(self,
                 method: str,
                 path: str,
                 query_string: str,
                 headers: Dict[str, str],
                 raw_body: bytes):
        self.method = method
        self.path = path
        self.query_string = query_string

        self.headers = {}
        for name, value in headers.items():
            self.headers[name.lower()] = value

        self.raw_body = raw_body
