import flask
import waitress
from dependency_injector import containers, providers

from mat_server.app.cli import create_cli
from mat_server.app.manager import Manager
from mat_server.app.mat_server import MatServer


class Container(containers.DeclarativeContainer):
    FlaskApp = providers.Singleton(flask.Flask, __name__)

    MatServer = providers.Factory(
        MatServer,
        flask_app=FlaskApp,
        wsgi_application_prod_serve_func=waitress.serve,
    )

    Manager = providers.Factory(
        Manager,
        mat_server=MatServer,
    )

    create_cli = providers.Callable(
        create_cli,
        Manager,
    )
