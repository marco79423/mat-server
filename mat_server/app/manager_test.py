from unittest import mock

from mat_server.app.manager import Manager
from mat_server.app.mat_server import MatServer
from mat_server.domain import use_cases


def test_create_config(capsys):
    generate_default_config_use_case = mock.MagicMock(spec=use_cases.GenerateDefaultConfigUseCase)
    mat_server = mock.MagicMock(spec=MatServer)

    manager = Manager(
        generate_default_config_use_case=generate_default_config_use_case,
        mat_server=mat_server,
    )

    manager.create_config()

    captured = capsys.readouterr()
    assert captured.out == '初始化 mat 設定 ...\nmat-data 資料夾建立完成\n'
    generate_default_config_use_case.execute.assert_called_once()


def test_serve():
    generate_default_config_use_case = mock.MagicMock(spec=use_cases.GenerateDefaultConfigUseCase)
    mat_server = mock.MagicMock(spec=MatServer)

    manager = Manager(
        generate_default_config_use_case=generate_default_config_use_case,
        mat_server=mat_server,
    )

    manager.serve('0.0.0.0', port=9527)

    mat_server.serve.assert_called_with(
        host='0.0.0.0',
        port=9527,
    )
