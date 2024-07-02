from pages.main_page import MainPage
from pages.page_trade_creation import TradeCreationPage
import pytest


class BaseTest:
    main_page: MainPage
    trade_creation_page: TradeCreationPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_chrom):
        request.cls.browser_chrom = browser_chrom
        request.cls.main_page = MainPage(browser_chrom)
        request.cls.trade_creation_page = TradeCreationPage(browser_chrom)
