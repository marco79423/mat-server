from mat_server.app.command.mat_server import MatServerBase


class Manager:

    def __init__(self,
                 mat_server: MatServerBase):
        self._mat_server = mat_server

    def create_config(self):
        print('初始化 mat 設定')

    def serve(self, host, port):
        self._mat_server.serve(
            host=host,
            port=port,
        )
