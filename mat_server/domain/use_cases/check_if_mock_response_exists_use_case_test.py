from mat_server.domain import entities
from mat_server.domain.use_cases import CheckIfMockResponseExistsUseCase


def test_check_if_mock_response_exists():
    uc = CheckIfMockResponseExistsUseCase()
    assert uc.execute(entities.Request(
        method='GET',
        path='path',
        query_string='query_string',
        headers={},
        raw_body=b''
    )) == False
