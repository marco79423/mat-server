import pathlib

from mat_server.infrastructure.helpers import DataHelper


def test_get_default_mat_data_path():
    data_helper = DataHelper(
        data_dir=pathlib.Path('.')
    )
    assert data_helper.get_default_mat_data_path() == pathlib.Path('.') / 'default' / 'mat-data'
