from mat_server.infrastructure.helpers import DataRetrieverHelper


def test_get_value():
    data_retriever_helper = DataRetrieverHelper()
    assert data_retriever_helper.get_value({}, '') == 'https://paji.marco79423.net'
