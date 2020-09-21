import shlex

from click.testing import CliRunner

from .manager import Manager


def test_create_config(capsys):
    manager = Manager()

    manager.create_config()

    captured = capsys.readouterr()
    assert captured.out == '初始化 mat 設定\n'


def test_serve(capsys):
    manager = Manager()

    manager.serve('0.0.0.0', port=9527)

    captured = capsys.readouterr()
    assert captured.out == f'啟動 mat-server 伺服器 (http://0.0.0.0:9527)\n'
