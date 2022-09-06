from utilities.json_to_dict import json_to_dict
from utilities.mark_test_status import MarkTestStatus
from utilities.util import Utilities
import unittest
import pytest
from tests.base_test import BaseTest
from ddt import ddt, data, unpack, file_data
import allure
from assertpy import assert_that, soft_assertions, soft_fail
import pytest_check as check


@pytest.mark.parametrize("data", json_to_dict("datafiles//login.json"))
class TestLogin():

    @allure.testcase("Login Test")
    @allure.description("Testing the login functionality")
<<<<<<< HEAD
    def test_login(self, login_page, data):
        login_page.get("http://demo.guru99.com/test/newtours/")
        login_page.enter_username(data["username"])
        login_page.enter_password(data["password"])
        login_page.click_submit_button()
        assert_that(login_page.check_login_successfull()).is_true()
        assert_that(login_page.check_sign_off_link_is_displayed()).is_true()
=======
    @file_data("..//..//datafiles//login.json")
    @pytest.mark.order(1)
    def test_login(self, username, password):
        self.login.visit("http://demo.guru99.com/test/newtours/")
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.click_submit_button()
        assert_that(self.login.check_login_successfull()).is_true()
        assert_that(self.login.check_sign_off_link_is_displayed()).is_true()

>>>>>>> 2cfa2876295f5d2916d222d8a0866cc4b5e57119

