from unittest import mock

from mat_server.app.manager import Manager
from mat_server.app.mat_server import MatServerBase


def test_create_config(capsys):
    mat_server = mock.MagicMock(spec=MatServerBase)

    manager = Manager(
        mat_server=mat_server,
    )

    manager.create_config()

    captured = capsys.readouterr()
    assert captured.out == '初始化 mat 設定\n'


def test_serve():
    mat_server = mock.MagicMock(spec=MatServerBase)

    manager = Manager(
        mat_server=mat_server,
    )

    manager.serve('0.0.0.0', port=9527)

    mat_server.serve.assert_called_with(
        host='0.0.0.0',
        port=9527,
    )
