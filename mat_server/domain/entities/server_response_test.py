from mat_server.domain.entities import ServerResponse


def test_create_server_response_with_empty_data():
    server_response = ServerResponse()

    assert server_response.raw_data == b''
    assert server_response.status_code == 200
    assert server_response.headers == {}


def test_create_server_response_with_data():
    server_response = ServerResponse(
        raw_data=b'raw_data',
        status_code=201,
        headers={
            'Name': 'name'
        }
    )

    assert server_response.raw_data == b'raw_data'
    assert server_response.status_code == 201
    assert server_response.headers == {
        'Name': 'name'
    }


def test_compare_any_object():
    assert ServerResponse() != ''


def test_compare_different_raw_data_response():
    assert ServerResponse(
        raw_data=b'raw_data',
    ) != ServerResponse(
        raw_data=b'raw_data2',
    )


def test_compare_different_status_code_response():
    assert ServerResponse(
        status_code=200,
    ) != ServerResponse(
        status_code=201,
    )


def test_compare_different_headers_response():
    assert ServerResponse(
        headers={
            'Name': 'value',
        },
    ) != ServerResponse(
        headers={
            'Name': 'value2',
        }
    )


def test_compare_the_same_response():
    assert ServerResponse(
        raw_data=b'raw_data',
        status_code=200,
        headers={
            'Name': 'name'
        }
    ) == ServerResponse(
        raw_data=b'raw_data',
        status_code=200,
        headers={
            'Name': 'name'
        }
    )
