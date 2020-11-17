import os

from mat_server.domain import base_types, entities, repositories, exceptions, helpers


class GetMockResponseUseCase(base_types.UseCase):

    def __init__(self,
                 mat_config_repository: repositories.MatConfigRepositoryBase,
                 file_helper: helpers.FileHelperBase):
        self._mat_config_repository = mat_config_repository
        self._file_helper = file_helper

    def execute(self, request: entities.ClientRequest) -> entities.ServerResponse:
        route_config = self._mat_config_repository.query_route_config(
            path=request.path,
            method=request.method,
            query_string=request.query_string,
        )

        if route_config is None:
            raise exceptions.NotFoundError('找不到對應的 ConfigRoute')

        if route_config.response.file_path and route_config.response.data:
            raise exceptions.ValidationError('回傳資源衝突')

        elif route_config.response.data:
            # 預設直接猜測 json
            headers = {
                'Content-Type': 'application/json',
            }

            return entities.ServerResponse(
                raw_body=route_config.response.data.encode(),
                status_code=route_config.status_code,
                headers=headers,
            )

        elif route_config.response.file_path:
            response_file_path = self._file_helper.join_file_paths(
                'mat-data',
                route_config.response.file_path,
            )

            file_type = self._file_helper.guess_file_type(response_file_path)
            if file_type is None:
                file_type = 'text/html; charset=utf-8'

            headers = {
                'Content-Type': file_type,
            }

            return entities.ServerResponse(
                raw_body=self._file_helper.read_bytes(response_file_path),
                status_code=route_config.status_code,
                headers=headers,
            )

        else:
            raise exceptions.ValidationError('找不到對應的回傳資料')
