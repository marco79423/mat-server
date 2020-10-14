from mat_server.infrastructure.repositories import ConfigRepository


def test_get_proxy_host():
    config_repository = ConfigRepository()
    assert config_repository.get_proxy_host() == 'https://paji.marco79423.net'
