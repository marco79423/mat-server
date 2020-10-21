from unittest import mock

from mat_server.domain import entities, helpers
from mat_server.infrastructure.repositories import MatConfigRepository


def test_get_proxy_host():
    config_data = {}

    file_helper = mock.MagicMock(spec=helpers.FileHelperBase)
    file_helper.read_yaml.return_value = config_data

    data_retriever_helper = mock.MagicMock(spec=helpers.DataRetrieverHelperBase)
    data_retriever_helper.get_value.return_value = 'https://paji.marco79423.net'

    mat_config_repository = MatConfigRepository(
        file_helper=file_helper,
        data_retriever_helper=data_retriever_helper,
    )
    assert mat_config_repository.get_proxy_host() == 'https://paji.marco79423.net'

    file_helper.read_yaml.assert_called_with(MatConfigRepository.CONFIG_FILE_PATH)
    data_retriever_helper.get_value.assert_called_with(config_data, '.server.proxy_url')


def test_query_non_existed_route_config():
    file_helper = mock.MagicMock(spec=helpers.FileHelperBase)
    data_retriever_helper = mock.MagicMock(spec=helpers.DataRetrieverHelperBase)

    mat_config_repository = MatConfigRepository(
        file_helper=file_helper,
        data_retriever_helper=data_retriever_helper,
    )

    assert mat_config_repository.query_route_config(
        path='path',
        method='GET',
        query_string='name=hello',
    ) is None


def test_query_route_config():
    file_helper = mock.MagicMock(spec=helpers.FileHelperBase)
    data_retriever_helper = mock.MagicMock(spec=helpers.DataRetrieverHelperBase)

    mat_config_repository = MatConfigRepository(
        file_helper=file_helper,
        data_retriever_helper=data_retriever_helper,
    )

    assert mat_config_repository.query_route_config(
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
