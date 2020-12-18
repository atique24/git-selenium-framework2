from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from tests.base_test import BaseTest

#@pytest.mark.usefixtures("oneTimeSetup")

class TestCompare(BaseTest,unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self,oneTimeSetup):
        self.mb = MobilePage(self.driver)
        self.ts = MarkTestStatus(self.driver)


    @pytest.mark.xfail(order=5)
    def test_compare_mobile(self):
        self.mb.mobile_tab()
        self.mb.click_list_view()
        result = self.mb.click_compare_()
        self.ts.finalMark(testcase="Test Compare Mobile", result=result,
                          resultMessage="Compared Successfully")

