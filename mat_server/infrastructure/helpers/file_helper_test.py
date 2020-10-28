from unittest import mock

from mat_server.infrastructure.helpers.file_helper import FileHelper


def test_read_yaml():
    fp = mock.MagicMock()
    data = {
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

    codecs_module = mock.MagicMock()
    codecs_module.open.return_value.__enter__.return_value = fp

    shutil_module = mock.MagicMock()

    yaml_module = mock.MagicMock()
    yaml_module.safe_load.return_value = data

    file_helper = FileHelper(
        codecs_module=codecs_module,
        shutil_module=shutil_module,
        yaml_module=yaml_module,
    )

    assert file_helper.read_yaml('target_path') == data

    codecs_module.open.assert_called_with('target_path', 'r', encoding='utf-8')
    yaml_module.safe_load.assert_called_with(fp)


def test_copy_folder():
    codecs_module = mock.MagicMock()
    shutil_module = mock.MagicMock()
    yaml_module = mock.MagicMock()

    file_helper = FileHelper(
        codecs_module=codecs_module,
        shutil_module=shutil_module,
        yaml_module=yaml_module,
    )

    file_helper.copy_folder(
        src_path='src_path',
        dest_path='dest_path',
    )

    shutil_module.copytree.assert_called_with('src_path', 'dest_path')
