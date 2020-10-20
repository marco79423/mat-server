import abc
from typing import Optional, Dict

from mat_server.domain import base_types, entities


class MatConfigRepositoryBase(base_types.Repository):

    @abc.abstractmethod
    def get_proxy_host(self) -> str:
        pass

    @abc.abstractmethod
    def query_route_config(self,
                           path: str,
                           method: str,
                           query_string: str) -> Optional[entities.RouteConfig]:
        pass
