from pages.locators import LoginPageLocators
from base.selenium_driver import SeleniumDriver
import allure


class Login(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lp = LoginPageLocators()


    @allure.step("Enter the username")
    def enter_username(self,username):
        self.elementSend(self.lp.username,username)

    @allure.step("Enter the password")
    def enter_password(self,password):
        self.elementSend(self.lp.password, password)

    @allure.step("Click on Submit button")
    def click_submit_button(self):
        self.elementClick(self.lp.submit)

    @allure.step("Check if the success message is displayed")
    def check_login_successfull(self):
        return self.isElementDisplayed(self.lp.success_message)