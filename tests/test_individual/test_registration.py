from pages.page_register.register_page import Registration
from utilities.mark_test_status import MarkTestStatus
import pytest
from tests.base_test import BaseTest
import allure
from utilities.json_to_list import json_to_list
from utilities.csvdata import getCsvData
from utilities.json_to_dict import json_to_dict

"""
Test using pytest and @pytest.mark.parameterize provider for data driven testing. Data is imported from csv and json.
"""


class TestRegistration(BaseTest):

    @pytest.fixture(autouse=True)
    def PageObjects(self):
        self.ts = MarkTestStatus(self.driver)

    @allure.testcase("Registration Test")
    @allure.description("Testing the Registration functionality")
    @pytest.mark.parametrize("firstname,lastname,email", json_to_list("datafiles//registration.json"))
    #@pytest.mark.run(1)
    def test_registration_01(self, register_page,firstname, lastname, email):
        register_page.accept_privacy_message()
        register_page.click_register_button()
        register_page.enter_firstname(firstname)
        register_page.enter_lastname(lastname)
        register_page.enter_email(email)
        register_page.click_submit_button()
        result = register_page.check_registration_message()
        self.ts.finalMark(testcase="test_registration with data from json", result=result, resultMessage="Testing the registration functionality")

    @pytest.fixture(autouse=True)
    def AfterTest(self):
        yield
        self.driver.back()

    @allure.testcase("Registration Test")
    @allure.description("Testing the Registration functionality")
    @pytest.mark.parametrize("firstname,lastname,email", getCsvData("datafiles//registration.csv"))
    # @pytest.mark.run(2)
    def test_registration_02(self, register_page,firstname, lastname, email):
        register_page.click_register_button()
        register_page.enter_firstname(firstname)
        register_page.enter_lastname(lastname)
        register_page.enter_email(email)
        register_page.click_submit_button()
        result = register_page.check_registration_message()
        self.ts.finalMark(testcase="test_registration with data from csv", result=result,
                          resultMessage="Testing the registration functionality")

    @allure.testcase("Registration Test")
    @allure.description("Testing the Registration functionality")
    @pytest.mark.parametrize("testData", json_to_dict("datafiles//registration.json"))
    # @pytest.mark.run(3)
    def test_registration_03(self, register_page ,testData):
        register_page.click_register_button()
        register_page.enter_firstname(testData['firstname'])
        register_page.enter_lastname(testData['lastname'])
        register_page.enter_email(testData['email'])
        register_page.click_submit_button()
        result = register_page.check_registration_message()
        self.ts.finalMark(testcase="test_registration with data from csv", result=result,
                          resultMessage="Testing the registration functionality")


