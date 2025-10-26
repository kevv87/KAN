from extractor import process_file
from unittest.mock import mock_open
from pytest_mock import MockerFixture

def test_should_read_file(mocker: MockerFixture):
    sample_filename = 'sample.txt'
    file_mock = mock_open(read_data='Sample file content')
    mocker.patch('builtins.open', file_mock)
    process_file(sample_filename)
    file_mock.assert_called_once_with(sample_filename, 'r')

