from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from tests.base_test import BaseTest

#@pytest.mark.usefixtures("oneTimeSetup")
class TestSortBy(BaseTest,unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self,oneTimeSetup):
        self.mb = MobilePage(oneTimeSetup)
        self.ts = MarkTestStatus(oneTimeSetup)

    @pytest.mark.run(order=1)
    def test_sort_by_name(self):
        result = self.mb.mobile_sort_by_name()
        self.ts.finalMark(testcase="Mobile Sort By test",result=result,resultMessage="Testing Mobile SOrt functionality")

    @pytest.mark.run(order=2)
    def test_sort_by_prices(self):
        result = self.mb.mobile_sort_by_price()
        self.ts.finalMark(testcase="Mobile Sort By test", result=result,
                          resultMessage="Testing Mobile SOrt functionality")

