from unittest import mock

from mat_server.infrastructure.helpers.file_helper import FileHelper


def test_read_yaml():
    copy_folder_func = mock.MagicMock()
    file_helper = FileHelper(
        copy_folder_func=copy_folder_func,
    )

    assert file_helper.read_yaml('') == {
        'server': {
            'proxy_url': 'https://marco79423.net',
        }
    }


def test_copy_folder():
    copy_folder_func = mock.MagicMock()
    file_helper = FileHelper(
        copy_folder_func=copy_folder_func,
    )

    file_helper.copy_folder(
        src_path='src_path',
        dest_path='dest_path',
    )

    copy_folder_func.assert_called_with('src_path', 'dest_path')
