from pages.page_login.login_page_locator import LoginPageLocators
from base.selenium_driver import SeleniumDriver
from assertpy import assert_that
import allure


class Login(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lp = LoginPageLocators()


    @allure.step("Clicking on register from homepage")
    def click_register_linK(self):
        self.elementClick(self.lp.register)

    @allure.step("Enter the registered mobile number")
    def enter_mobile_number(self,number):
        self.elementSend(self.lp.number, number)

    @allure.step("Check the Invalid mobile number is displayed")
    def check_the_error_message(self):
        assert_that(self.isElementPresent(self.lp.error_message)).is_false()
