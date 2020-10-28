from mat_server.domain import base_types, entities, repositories, exceptions


class GetMockResponseUseCase(base_types.UseCase):

    def __init__(self,
                 mat_config_repository: repositories.MatConfigRepositoryBase):
        self._mat_config_repository = mat_config_repository

    def execute(self, request: entities.ClientRequest) -> entities.ServerResponse:
        route_config = self._mat_config_repository.query_route_config(
            path=request.path,
            method=request.method,
            query_string=request.query_string,
        )

        if route_config is None:
            raise exceptions.NotFoundError('找不到對應的 ConfigRoute')

        if route_config.response.file_path is None and route_config.response.data is None:
            raise exceptions.ValidationError('找不到對應的回傳資料')

        if route_config.response.file_path and route_config.response.data:
            raise exceptions.ValidationError('回傳資源衝突')

        if route_config.response.data:
            return entities.ServerResponse(
                raw_body=route_config.response.data.encode(),
                status_code=route_config.status_code,
            )

        raise NotImplementedError
