from pages.locators import RegisterLocators
from base.selenium_driver import SeleniumDriver
import allure


class Registration(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = RegisterLocators


    @allure.step("Clicking on register from homepage")
    def click_register_button(self):
        self.elementClick(self.locators.register)

    @allure.step("Enter the firstname")
    def enter_firstname(self,firstname):
        self.elementSend(self.locators.firstname, firstname)

    @allure.step("Enter the lastname")
    def enter_lastname(self,lastname):
        self.elementSend(self.locators.lastname, lastname)

    @allure.step("Enter the email")
    def enter_email(self, email):
        self.elementSend(self.locators.email, email)

    @allure.step("Click on Submit button")
    def click_submit_button(self):
        self.elementClick(self.locators.submit)

    @allure.step("Check if the success message is displayed")
    def check_registration_message(self):
        return self.isElementDisplayed(self.locators.success_message)
