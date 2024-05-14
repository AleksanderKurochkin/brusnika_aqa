from pages.main_page import MainPage
import pytest


class BaseTest:
    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_chrom):
        request.cls.browser_chrom = browser_chrom
        request.cls.main_page = MainPage(browser_chrom)
