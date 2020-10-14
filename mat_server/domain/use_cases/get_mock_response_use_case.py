from mat_server.domain import base_types, entities


class GetMockResponseUseCase(base_types.UseCase):

    def execute(self, request: entities.ClientRequest) -> entities.ServerResponse:
        return entities.ServerResponse()
