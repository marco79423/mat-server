from unittest import mock

import flask

from mat_server.app.mat_server import MatServer


def test_get_app():
    flask_app = mock.MagicMock(spec=flask.Flask)
    wsgi_application_prod_serve_func = mock.MagicMock()

    mat_server = MatServer(
        flask_app=flask_app,
        wsgi_application_prod_serve_func=wsgi_application_prod_serve_func,
    )

    assert mat_server.get_app() == flask_app


def test_serve():
    flask_app = mock.MagicMock(spec=flask.Flask)
    wsgi_application_prod_serve_func = mock.MagicMock()

    mat_server = MatServer(
        flask_app=flask_app,
        wsgi_application_prod_serve_func=wsgi_application_prod_serve_func,
    )

    mat_server.serve('0.0.0.0', port=9527)

    wsgi_application_prod_serve_func.assert_called_with(
        flask_app,
        host='0.0.0.0',
        port=9527,
    )
