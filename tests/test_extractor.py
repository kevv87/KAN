from extractor import process_file
from pytest_mock import MockerFixture
from mocks import PdfPlumberLibMock
import pytest

@pytest.fixture
def setup_pdf_lib_mock(mocker: MockerFixture):
    lib_mock = PdfPlumberLibMock()
    mocker.patch('extractor.pdfplumber', lib_mock)
    yield lib_mock

def test_should_open_file_with_plumber(setup_pdf_lib_mock):
    sample_filename = 'sample.txt'
    lib_mock = setup_pdf_lib_mock

    process_file(sample_filename)

    lib_mock.assert_file_opened(sample_filename)

# TODO: not yet implemeted
def test_should_try_to_find_starting_page(setup_pdf_lib_mock):
    lib_mock = setup_pdf_lib_mock

    process_file('sample.txt')

    lib_mock.assert_tried_to_find_text('Detalle de compras del periodo')

def test_should_try_to_find_ending_page():
    pass


class TestExtractSinglePage:
    def test_should_crop_page(self):
        pass

    def test_should_extract_table_from_page(self):
        pass

    def test_should_return_df_with_extracted_table(self):
        pass

    def test_should_ignore_empty_entries(self):
        pass


class TextExtractMultiPage:
    def test_should_crop_all_pages(self):
        pass

    def test_should_extract_table_from_all_pages(self):
        pass

    def test_should_return_df_with_extracted_table_from_all_pages(self):
        pass



