from typing import Optional, Dict, Any

from mat_server.domain import base_types


class ServerResponse(base_types.Entity):
    """傳給客戶端的回傳值"""

    def __init__(self,
                 raw_data: Optional[bytes] = None,
                 status_code: int = 200,
                 headers: Optional[Dict[str, str]] = None):
        self.raw_data = raw_data if raw_data is not None else b''
        self.status_code = status_code
        self.headers = headers if headers is not None else {}

    def __eq__(self, other: Any):
        if not isinstance(other, ServerResponse):
            return False
        if self.raw_data != other.raw_data:
            return False
        if self.status_code != other.status_code:
            return False
        if self.headers != other.headers:
            return False
        return True
