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
        self.registration = Registration(self.driver)
        self.ts = MarkTestStatus(self.driver)

    @allure.testcase("Registration Test")
    @allure.description("Testing the Registration functionality")
    @pytest.mark.parametrize("firstname,lastname,email", json_to_list("datafiles//registration.json"))
    #@pytest.mark.run(1)
    def test_registration_01(self, firstname, lastname, email):
        self.registration.click_register_button()
        self.registration.enter_firstname(firstname)
        self.registration.enter_lastname(lastname)
        self.registration.enter_email(email)
        self.registration.click_submit_button()
        result = self.registration.check_registration_message()
        self.ts.finalMark(testcase="test_registration with data from json", result=result, resultMessage="Testing the registration functionality")

    @pytest.fixture(autouse=True)
    def AfterTest(self):
        yield
        self.driver.back()

    @allure.testcase("Registration Test")
    @allure.description("Testing the Registration functionality")
    @pytest.mark.parametrize("firstname,lastname,email", getCsvData("datafiles//registration.csv"))
    # @pytest.mark.run(2)
    def test_registration_02(self, firstname, lastname, email):
        self.registration.click_register_button()
        self.registration.enter_firstname(firstname)
        self.registration.enter_lastname(lastname)
        self.registration.enter_email(email)
        self.registration.click_submit_button()
        result = self.registration.check_registration_message()
        self.ts.finalMark(testcase="test_registration with data from csv", result=result,
                          resultMessage="Testing the registration functionality")

    @allure.testcase("Registration Test")
    @allure.description("Testing the Registration functionality")
    @pytest.mark.parametrize("testData", json_to_dict("datafiles//registration.json"))
    # @pytest.mark.run(3)
    def test_registration_03(self, testData):
        self.registration.click_register_button()
        self.registration.enter_firstname(testData['firstname'])
        self.registration.enter_lastname(testData['lastname'])
        self.registration.enter_email(testData['email'])
        self.registration.click_submit_button()
        result = self.registration.check_registration_message()
        self.ts.finalMark(testcase="test_registration with data from csv", result=result,
                          resultMessage="Testing the registration functionality")


