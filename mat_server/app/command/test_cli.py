import shlex

from click.testing import CliRunner

from .cli import cli


def test_init():
    runner = CliRunner()
    result = runner.invoke(cli, shlex.split('init'))

    assert result.exit_code == 0
    assert result.stdout == '初始化 mat 設定\n'


def test_serve():
    runner = CliRunner()
    result = runner.invoke(cli, shlex.split('serve'))

    assert result.exit_code == 0
    assert result.stdout == f'啟動 mat-server 伺服器 (http://0.0.0.0:9527)\n'
