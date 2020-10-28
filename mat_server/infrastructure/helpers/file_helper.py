from typing import Any

from mat_server.domain import helpers


class FileHelper(helpers.FileHelperBase):

    def __init__(self,
                 codecs_module,
                 shutil_module,
                 yaml_module):

        self._codecs_module = codecs_module
        self._shutil_module = shutil_module
        self._yaml_module = yaml_module

    def read_yaml(self, target_path: str) -> Any:
        """讀取 yaml 檔案"""
        with self._codecs_module.open(target_path, 'r', encoding='utf-8') as fp:
            return self._yaml_module.safe_load(fp)

    def copy_folder(self, src_path: str, dest_path: str):
        """複製資料夾 (支援遞迴複製)"""
        self._shutil_module.copytree(src_path, dest_path)
