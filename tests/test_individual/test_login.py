from pages.page_login.login_page import Login
from utilities.mark_test_status import MarkTestStatus
from utilities.util import Utilities
import unittest
import pytest
from tests.base_test import BaseTest
from ddt import ddt, data, unpack, file_data
import allure

"""
Test using pytest and unittest @ddt provider for data driven testing
"""

@ddt
class TestLogin(BaseTest, unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.login = Login(self.driver)
        self.ts = MarkTestStatus(self.driver)

    @allure.testcase("Login Test")
    @allure.description("Testing the login functionality")
    @file_data("..//..//datafiles//login.json")
    #@pytest.mark.run(1)
    def test_login(self, username,password):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.click_submit_button()
        result = self.login.check_login_successfull()
        self.ts.finalMark(testcase="test_login", result=result, resultMessage="Testing the login functionality")


