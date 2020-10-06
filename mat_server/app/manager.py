from mat_server.app.mat_server import MatServer
from mat_server.domain import use_cases


class Manager:

    def __init__(self,
                 generate_default_config_use_case: use_cases.GenerateDefaultConfigUseCase,
                 mat_server: MatServer):
        self._generate_default_config_use_case = generate_default_config_use_case
        self._mat_server = mat_server

    def create_config(self):
        print('初始化 mat 設定 ...')
        self._generate_default_config_use_case.execute()
        print('mat-data 資料夾建立完成')

    def serve(self, host, port):
        self._mat_server.serve(
            host=host,
            port=port,
        )
