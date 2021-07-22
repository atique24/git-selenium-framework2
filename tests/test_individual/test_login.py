from pages.page_login.login_page import Login
from utilities.mark_test_status import MarkTestStatus
import unittest
import pytest
from tests.base_test import BaseTest
from ddt import ddt, data, unpack, file_data
import allure


@ddt
class TestLogin(BaseTest, unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self, oneTimeSetup):
        self.login = Login(self.driver)
        self.ts = MarkTestStatus(self.driver)

    @allure.testcase("Login Test")
    @allure.description("Testing the login functionality for ThreeUK")
    @file_data("..//..//datafiles//login.json")
    @pytest.mark.run(order=1)
    def test_registration(self, number):
        self.login.click_register_linK()
        self.login.enter_mobile_number(number)
        result = self.login.check_the_error_message()
        self.ts.finalMark("test registration",result,"is the element present??")
        #self.ts.finalMark(testcase='Login Functionality', result=result, resultMessage='Error displayed')
