from utilities.json_to_dict import json_to_dict
from utilities.mark_test_status import MarkTestStatus
from utilities.util import Utilities
import unittest
import pytest
from tests.base_test import BaseTest
import allure
from assertpy import assert_that, soft_assertions, soft_fail



@pytest.mark.parametrize("data", json_to_dict("datafiles//login.json"))
class TestLogin():

    @allure.testcase("Login Test")
    @allure.description("Testing the login functionality")
    def test_login(self, login_page, data):
        login_page.accept_privacy_message()
        login_page.get("http://demo.guru99.com/test/newtours/")
        login_page.enter_username(data["username"])
        login_page.enter_password(data["password"])
        login_page.click_submit_button()
        assert_that(login_page.check_login_successfull()).is_true()
        assert_that(login_page.check_sign_off_link_is_displayed()).is_true()

