from mat_server.domain import entities
from mat_server.infrastructure.repositories import ConfigRepository


def test_get_proxy_host():
    config_repository = ConfigRepository()
    assert config_repository.get_proxy_host() == 'https://paji.marco79423.net'


def test_query_non_existed_route_config():
    config_repository = ConfigRepository()
    assert config_repository.query_route_config(
        path='path',
        method='GET',
        query_string='name=hello',
    ) is None


def test_query_route_config():
    config_repository = ConfigRepository()
    assert config_repository.query_route_config(
        path='path',
        method='GET',
        query_string='name=大類',
    ) == entities.RouteConfig(
        listen_path='path',
        method='GET',
        status_code=200,
        query={
            'name': ['大類']
        },
        response=entities.RouteResponseConfig(
            raw_data='哈囉 廢物'.encode(),
        )
    )
