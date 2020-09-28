from dependency_injector import containers, providers

from mat_server.app.command.cli import create_cli
from mat_server.app.command.manager import Manager
from mat_server.app.command.mat_server import MatServer


class Container(containers.DeclarativeContainer):
    MatServer = providers.Factory(MatServer)

    Manager = providers.Factory(
        Manager,
        mat_server=MatServer,
    )

    create_cli = providers.Callable(
        create_cli,
        Manager,
    )
