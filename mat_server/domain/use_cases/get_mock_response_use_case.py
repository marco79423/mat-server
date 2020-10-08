from mat_server.domain import base_types, entities


class GetMockResponseUseCase(base_types.UseCase):

    def execute(self, request: entities.Request) -> entities.Response:
        return entities.Response()
