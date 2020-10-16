from unittest import mock

from mat_server.domain import entities, repositories
from mat_server.domain.use_cases import CheckIfMockResponseExistsUseCase


def test_check_mock_response_not_exists():
    config_repository = mock.MagicMock(spec=repositories.ConfigRepositoryBase)
    config_repository.query_route_config.return_value = None

    uc = CheckIfMockResponseExistsUseCase(
        config_repository=config_repository,
    )

    assert uc.execute(entities.ClientRequest(
        method='GET',
        path='path',
        query_string='query_string',
        headers={},
        raw_body=b''
    )) is False


def test_check_mock_response_exists():
    config_repository = mock.MagicMock(spec=repositories.ConfigRepositoryBase)
    config_repository.query_route_config.return_value = entities.RouteConfig(
        listen_path='listen_path',
        method='GET',
        status_code=200,
        query=None,
        response=entities.RouteResponseConfig(),
    )

    uc = CheckIfMockResponseExistsUseCase(
        config_repository=config_repository,
    )

    assert uc.execute(entities.ClientRequest(
        method='GET',
        path='path',
        query_string='query_string',
        headers={},
        raw_body=b''
    )) is True

    config_repository.query_route_config.assert_called_with(
        path='path',
        method='GET',
        query_string='query_string',
    )
