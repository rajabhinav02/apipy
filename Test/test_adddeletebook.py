import pytest

from APIs.addBook import addBook
from TestResult.TestStatus import TestStatush


class TestBook:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ts= TestStatush()
        self.ad = addBook()

    def test_addbook(self):
        self.ad.updatebook()
        msg=self.ad.validatemessage()
        self.ts.marktestfinal(msg,"add book", "test_addbook")
