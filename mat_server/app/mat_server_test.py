from .mat_server import MatServer


def test_serve(capsys):
    mat_server = MatServer()

    mat_server.serve('0.0.0.0', port=9527)

    captured = capsys.readouterr()
    assert captured.out == f'啟動 mat-server 伺服器 (http://0.0.0.0:9527)\n'
