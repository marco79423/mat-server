from mat_server.domain import base_types, entities, repositories


class CheckIfMockResponseExistsUseCase(base_types.UseCase):

    def __init__(self,
                 config_repository: repositories.ConfigRepositoryBase):
        self._config_repository = config_repository

    def execute(self, request: entities.ClientRequest) -> bool:
        route = self._config_repository.query_route_config(
            path=request.path,
            method=request.method,
            query_string=request.query_string,
        )

        # 如果找得到對應的 route，代表有 mock response
        if route:
            return True

        return False
