import abc

from mat_server.domain import base_types


class ConfigRepositoryBase(base_types.Repository):

    @abc.abstractmethod
    def get_proxy_host(self) -> str:
        pass
