from typing import Optional, Dict

from mat_server.domain import base_types


class Response(base_types.Entity):
    def __init__(self,
                 raw_data: Optional[bytes] = None,
                 headers: Optional[Dict[str, str]] = None,
                 status_code: int = 200):
        self.raw_data = raw_data
        self.headers = headers if headers is not None else {}
        self.status = status_code

    def __eq__(self, other):
        if self.raw_data != other.raw_data:
            return False
        if self.headers != other.headers:
            return False
        if self.status != other.status:
            return False
        return True
