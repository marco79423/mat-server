import shutil
from typing import Any

from mat_server.domain import helpers


class FileHelper(helpers.FileHelperBase):

    def __init__(self,
                 copy_folder_func=shutil.copytree):
        self._copy_folder_func = copy_folder_func

    def read_yaml(self, target_path: str) -> Any:
        """讀取 yaml 檔案"""
        return {
            'server': {
                'proxy_url': 'https://paji.marco79423.net',
            },
            'routes': [
                {
                    'listen_path': 'demo/hello',
                    'query': {
                        'name': '大類',
                    },
                    'response': {
                        'data': '哈囉 廢物'
                    }
                }
            ]
        }

    def copy_folder(self, src_path: str, dest_path: str):
        """複製資料夾 (支援遞迴複製)"""
        self._copy_folder_func(src_path, dest_path)
