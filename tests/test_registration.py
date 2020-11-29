from pages.mobile_page.mobile_page import MobilePage
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from pages.account_creation.account_creation import Account
from ddt import ddt,data,unpack
from utilities.csvdata import getCsvData

@ddt()
@pytest.mark.usefixtures("oneTimeSetup")
class TestRegistration(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self,oneTimeSetup):
        self.mb = MobilePage(self.driver)
        self.account = Account(self.driver)
        self.ts = MarkTestStatus(self.driver)


    @data(*getCsvData(fileName="C://Users//A610037//PycharmProjects//git-selenium-framework2//datafiles//registration.csv"))
    @unpack
    @pytest.mark.run(order=6)
    def test_registration(self,firstName,lastName,emailAddress,password,confirmPassword):
        result = self.account.register(firstName,lastName,emailAddress,password,confirmPassword)
        self.ts.mark(result=result,resultMessage='Registration Successfull')
        result2 = self.account.add_to_wishlist()
        self.ts.finalMark(testcase='test_registration_share_wishlist',result=result,resultMessage="Wishlist shared successfully")

