from mat_server.domain import base_types, entities, repositories, exceptions


class GetMockResponseUseCase(base_types.UseCase):

    def __init__(self,
                 config_repository: repositories.ConfigRepositoryBase):
        self._config_repository = config_repository

    def execute(self, request: entities.ClientRequest) -> entities.ServerResponse:
        route_config = self._config_repository.query_route_config(
            path=request.path,
            method=request.method,
            query_string=request.query_string,
        )

        if route_config is None:
            raise exceptions.NotFoundError('找不到對應的 ConfigRoute')

        if route_config.response.file_path is None and route_config.response.raw_data is None:
            raise exceptions.DataError('找不到對應的回傳資料')

        if route_config.response.file_path and route_config.response.raw_data:
            raise exceptions.DataError('回傳資源衝突')

        if route_config.response.raw_data:
            return entities.ServerResponse(
                raw_body=route_config.response.raw_data,
                status_code=route_config.status_code,
            )

        raise NotImplementedError
