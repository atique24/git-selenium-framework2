from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from tests.base_test import BaseTest

#@pytest.mark.usefixtures("oneTimeSetup")
class TestCart(BaseTest,unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self,oneTimeSetup):
        self.mb = MobilePage(oneTimeSetup)
        self.ts = MarkTestStatus(self.driver)

    @pytest.mark.run(order=4)
    def test_max_cart_error(self):
        self.mb.mobile_tab()
        result = self.mb.verify_max_cart_error()
        self.ts.finalMark(testcase='Verify max cart error message',result=result,resultMessage='Error displayed')


