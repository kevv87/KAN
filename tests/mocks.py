from unittest.mock import Mock
from abc import ABC, abstractmethod

class PdfLibMock(ABC, Mock):
    lib_mock: Mock

    @abstractmethod
    def assert_file_opened(self, filename: str) -> bool:
        pass

    @abstractmethod
    def assert_tried_to_find_text(self, text:str) -> bool:
        pass


class PdfPlumberLibMock(PdfLibMock):
    lib_mock: Mock

    def assert_file_opened(self, filename: str) -> bool:
        return self.open.assert_called_with(filename)

    def assert_tried_to_find_text(self, text:str) -> bool:
        return self.find_page_with_text.assert_called_once_with(text)

