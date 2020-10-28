import urllib.parse
from unittest import mock

import pytest

from mat_server.domain import entities, repositories, exceptions
from mat_server.domain.use_cases import GetMockResponseUseCase


def test_failed_to_get_route_config():
    client_request = entities.ClientRequest(
        method='GET',
        path='path',
        query_string='name=name',
        headers={},
        raw_body=b'',
    )

    mat_config_repository = mock.MagicMock(spec=repositories.MatConfigRepositoryBase)
    mat_config_repository.query_route_config.return_value = None

    uc = GetMockResponseUseCase(
        mat_config_repository=mat_config_repository,
    )

    with pytest.raises(exceptions.NotFoundError, match='找不到對應的 ConfigRoute'):
        assert uc.execute(client_request)

    mat_config_repository.query_route_config.assert_called_with(
        path=client_request.path,
        method=client_request.method,
        query_string=client_request.query_string,
    )


def test_get_mock_response_without_file_path_and_raw_data():
    client_request = entities.ClientRequest(
        method='GET',
        path='path',
        query_string='name=name',
        headers={},
        raw_body=b'',
    )

    route_config = entities.RouteConfig(
        listen_path=client_request.path,
        method=client_request.method,
        status_code=200,
        query=urllib.parse.parse_qs(client_request.query_string),
        response=entities.RouteResponseConfig(),
    )

    mat_config_repository = mock.MagicMock(spec=repositories.MatConfigRepositoryBase)
    mat_config_repository.query_route_config.return_value = route_config

    uc = GetMockResponseUseCase(
        mat_config_repository=mat_config_repository,
    )

    with pytest.raises(exceptions.ValidationError, match='找不到對應的回傳資料'):
        assert uc.execute(client_request)

    mat_config_repository.query_route_config.assert_called_with(
        path=client_request.path,
        method=client_request.method,
        query_string=client_request.query_string,
    )


def test_get_mock_response_with_conflict_response_config():
    client_request = entities.ClientRequest(
        method='GET',
        path='path',
        query_string='name=name',
        headers={},
        raw_body=b'',
    )

    route_config = entities.RouteConfig(
        listen_path=client_request.path,
        method=client_request.method,
        status_code=200,
        query=urllib.parse.parse_qs(client_request.query_string),
        response=entities.RouteResponseConfig(
            file_path='file_path',
            data=b'raw_data',
        ),
    )

    mat_config_repository = mock.MagicMock(spec=repositories.MatConfigRepositoryBase)
    mat_config_repository.query_route_config.return_value = route_config

    uc = GetMockResponseUseCase(
        mat_config_repository=mat_config_repository,
    )

    with pytest.raises(exceptions.ValidationError, match='回傳資源衝突'):
        assert uc.execute(client_request)

    mat_config_repository.query_route_config.assert_called_with(
        path=client_request.path,
        method=client_request.method,
        query_string=client_request.query_string,
    )


def test_get_mock_response():
    client_request = entities.ClientRequest(
        method='GET',
        path='path',
        query_string='name=name',
        headers={},
        raw_body=b'',
    )

    route_config = entities.RouteConfig(
        listen_path=client_request.path,
        method=client_request.method,
        status_code=200,
        query=urllib.parse.parse_qs(client_request.query_string),
        response=entities.RouteResponseConfig(
            data='data'
        ),
    )

    mat_config_repository = mock.MagicMock(spec=repositories.MatConfigRepositoryBase)
    mat_config_repository.query_route_config.return_value = route_config

    uc = GetMockResponseUseCase(
        mat_config_repository=mat_config_repository,
    )
    assert uc.execute(client_request) == entities.ServerResponse(
        raw_body=route_config.response.data.encode(),
        status_code=route_config.status_code,
        headers={},
    )

    mat_config_repository.query_route_config.assert_called_with(
        path=client_request.path,
        method=client_request.method,
        query_string=client_request.query_string,
    )
