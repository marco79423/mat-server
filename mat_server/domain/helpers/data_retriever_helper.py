import abc
from typing import Any

from mat_server.domain import base_types


class DataRetrieverHelperBase(base_types.Helper):

    @abc.abstractmethod
    def get_value(self, data: Any, path: str) -> Any:
        pass
