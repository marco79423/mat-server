import urllib.parse
from typing import Optional

from mat_server.domain import repositories, entities, helpers


class MatConfigRepository(repositories.MatConfigRepositoryBase):

    CONFIG_DIR_PATH = './mat-data'
    CONFIG_FILE_PATH = './mat-data/config.yml'

    def __init__(self,
                 file_helper: helpers.FileHelperBase,
                 data_retriever_helper: helpers.DataRetrieverHelperBase):
        self._file_helper = file_helper
        self._data_retriever_helper = data_retriever_helper

    def get_proxy_host(self) -> Optional[str]:
        data = self._file_helper.read_yaml(self.CONFIG_FILE_PATH)
        return self._data_retriever_helper.get_value(data, '.server.proxy_url')

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
