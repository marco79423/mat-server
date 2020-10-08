from mat_server.domain import base_types, entities


class CheckIfMockResponseExistsUseCase(base_types.UseCase):

    def execute(self, request: entities.Request) -> bool:
        return False
