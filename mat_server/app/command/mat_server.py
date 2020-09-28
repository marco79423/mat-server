import abc


class MatServerBase(abc.ABC):

    @abc.abstractmethod
    def get_app(self):
        pass

    @abc.abstractmethod
    def serve(self, host: str, port: int):
        pass


class MatServer(MatServerBase):

    def get_app(self):
        pass

    def serve(self, host: str, port: int):
        print(f'啟動 mat-server 伺服器 (http://{host}:{port})')
