import urllib.parse
from typing import Optional

from mat_server.domain import repositories, entities


class MatConfigRepository(repositories.MatConfigRepositoryBase):

    def get_proxy_host(self) -> str:
        return 'https://paji.marco79423.net'

    def query_route_config(self,
                           path: str,
                           method: str,
                           query_string: str) -> Optional[entities.RouteConfig]:

        query_params = urllib.parse.parse_qs(query_string)
        if set(query_params.get('name', [])) == {'大類'}:
            return entities.RouteConfig(
                listen_path=path,
                method=method,
                status_code=200,
                query=query_params,
                response=entities.RouteResponseConfig(
                    raw_data='哈囉 廢物'.encode(),
                )
            )

        return None
