from unittest import mock

import flask.views
import pytest

from mat_server import AppContainer
from mat_server.domain import use_cases, entities


@pytest.fixture
def container():
    container = AppContainer()
    return container


@pytest.fixture
def app(container):
    mat_server = container.MatServer()
    return mat_server.get_app()


def test_return_mat_config(client, container):
    mat_config = entities.MatConfig(
        server=entities.ServerConfig(
            proxy_url='proxy_url',
        ),
        routes=[
            entities.RouteConfig(
                listen_path='listen_path',
                method='GET',
                status_code=200,
                query={
                    'key': ['value']
                },
                response=entities.RouteResponseConfig(
                    file_path='file_path',
                    data='data',
                )
            )
        ]
    )

    get_config_use_case = mock.MagicMock(spec=use_cases.GetConfigUseCase)
    get_config_use_case.execute.return_value = mat_config

    with container.DomainContainer.GetConfigUseCase.override(get_config_use_case):
        resp = client.get(flask.url_for('get_config'))
        assert resp.status_code == 200
        assert resp.json == {
            'server': {
                'proxy_url': 'proxy_url'
            },
            'routes': [
                {
                    'listen_path': 'listen_path',
                    'method': 'GET',
                    'status_code': 200,
                    'query': {
                        'key': ['value'],
                    },
                    'response': {
                        'file_path': 'file_path',
                        'data': 'data',
                    }
                }
            ]
        }
