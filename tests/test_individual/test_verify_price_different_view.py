from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from tests.base_test import BaseTest


#@pytest.mark.usefixtures("oneTimeSetup")
class TestVerifyPriceDifferentView(BaseTest,unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self,oneTimeSetup):
        self.mb = MobilePage(oneTimeSetup)
        self.ts = MarkTestStatus(oneTimeSetup)

    @pytest.mark.run(order=3)
    def test_verify_price_different_view(self):
        self.mb.mobile_tab()
        result = self.mb.verify_price_different_view()
        self.ts.finalMark(testcase='Verify price in different view',result=result,resultMessage='Value Matched')
