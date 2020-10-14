from mat_server.domain import repositories


class ConfigRepository(repositories.ConfigRepositoryBase):

    def get_proxy_host(self) -> str:
        return 'https://paji.marco79423.net'
