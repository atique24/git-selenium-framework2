from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from pages.account_creation.account_creation import Account
from ddt import ddt, data, unpack, file_data
from utilities.csvdata import getCsvData
from tests.base_test import BaseTest


@ddt()
# @pytest.mark.usefixtures("oneTimeSetup") -------instead inherit BaseTest instead of fixture
class TestRegistration(BaseTest, unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self, oneTimeSetup):
        self.mb = MobilePage(self.driver)
        self.account = Account(self.driver)
        self.ts = MarkTestStatus(self.driver)

    # @data(*getCsvData(fileName="datafiles//registration.csv"))  ----used for csv,excel
    # @unpack   -----used for csv,excel
    @file_data("..//..//datafiles//registration.json")  # -----used for JSON FILE

    @pytest.mark.run(order=4)
    def test_registration(self, firstName, lastName, emailAddress, password, confirmPassword, message):
        result1 = self.account.register(firstName, lastName, emailAddress, password, confirmPassword)
        self.ts.mark(result=result1, resultMessage='Registration Successfull')
        result2 = self.account.add_to_wishlist(emailAddress, message)
        self.ts.finalMark(testcase='test_registration_share_wishlist', result=result2,
                          resultMessage="Wishlist shared successfully")
