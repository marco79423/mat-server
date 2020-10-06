import flask
import waitress
from dependency_injector import containers, providers

from mat_server.app.cli import create_cli
from mat_server.app.manager import Manager
from mat_server.app.mat_server import MatServer
from mat_server.domain import use_cases


class DomainContainer(containers.DeclarativeContainer):
    GenerateDefaultConfigUseCase = providers.Factory(
        use_cases.GenerateDefaultConfigUseCase
    )


class AppContainer(containers.DeclarativeContainer):
    DomainContainer = providers.Container(DomainContainer)

    Manager = providers.Factory(
        Manager,
        generate_default_config_use_case=DomainContainer.GenerateDefaultConfigUseCase,
        mat_server=MatServer,
    )

    FlaskApp = providers.Singleton(flask.Flask, __name__)

    MatServer = providers.Factory(
        MatServer,
        flask_app=FlaskApp,
        wsgi_application_prod_serve_func=waitress.serve,
    )

    create_cli = providers.Callable(
        create_cli,
        Manager,
    )
