import abc
from typing import Dict, Tuple

from mat_server.domain import base_types


class RequestHelperBase(base_types.Helper):

    @abc.abstractmethod
    def send(self,
             method: str,
             url: str,
             headers: Dict[str, str],
             raw_body: bytes) -> Tuple[bytes, int, Dict[str, str]]:
        pass
