from mat_server.domain import base_types, helpers


class GenerateDefaultConfigUseCase(base_types.UseCase):

    def __init__(self,
                 data_helper: helpers.DataHelperBase,
                 file_helper: helpers.FileHelperBase):
        self._data_helper = data_helper
        self._file_helper = file_helper

    def execute(self):
        # 取得預設設定檔的路徑
        default_mat_data_path = self._data_helper.get_default_mat_data_path()

        self._file_helper.copy_folder(
            src_path=str(default_mat_data_path),
            dest_path='mat-data'
        )
