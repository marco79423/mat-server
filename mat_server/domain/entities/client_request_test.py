from mat_server.domain.entities import ClientRequest


def test_create_client_request_with_data():
    client_request = ClientRequest(
        method='POST',
        path='path',
        query_string='name=name',
        headers={
            'Name': 'name',
        },
        raw_body=b'hello world'
    )

    assert client_request.method == 'POST'
    assert client_request.path == 'path'
    assert client_request.query_string == 'name=name'
    assert client_request.headers == {
        'name': 'name'
    }
    assert client_request.raw_body == b'hello world'


def test_create_client_request_with_empty_data():
    client_request = ClientRequest()

    assert client_request.method == 'GET'
    assert client_request.path == ''
    assert client_request.query_string == ''
    assert client_request.headers == {}
    assert client_request.raw_body == b''
