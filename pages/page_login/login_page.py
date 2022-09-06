from selenium.webdriver.common.by import By
from base.SeleniumBase import SeleniumBase
import allure
from assertpy import assert_that


class LoginPage(SeleniumBase):
    username = (By.NAME, "userName")
    password = (By.NAME, "password")
    submit = (By.NAME, "submit")
    success_message = (By.XPATH, "//h3[text()='Login Successfully']")
    sign_off = (By.LINK_TEXT, "SIGN-OFF")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Enter the username")
    def enter_username(self, username):
        self.elementSend(self.username, username)

    @allure.step("Enter the password")
    def enter_password(self, password):
        self.elementSend(self.password, password)

    @allure.step("Click on Submit button")
    def click_submit_button(self):
        self.elementClick(self.submit)

    @allure.step("Check if the success message is displayed")
    def check_login_successfull(self):
        # assert_that(self.isElementDisplayed(self.lp.success_message)).is_true()
        return self.isElementDisplayed(self.success_message)

    @allure.step("Check if the sign off link is displayed")
    def check_sign_off_link_is_displayed(self):
        return self.isElementDisplayed(self.sign_off)
        # assert_that(self.isElementDisplayed(self.lp.sign_off)).is_true()
