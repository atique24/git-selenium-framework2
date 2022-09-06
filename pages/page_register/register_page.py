from selenium.webdriver.common.by import By
from base.SeleniumBase import SeleniumBase
import allure


class Registration(SeleniumBase):
    accept_privacy = (By.CSS_SELECTOR, "#save")
    register = (By.LINK_TEXT, "REGISTER")
    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")
    phone = (By.NAME, "phone")
    email = (By.NAME, "userName")
    submit = (By.NAME, "submit")
    success_message = (By.XPATH, "//font[contains(text(),'Thank you')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Accepting the Privacy Policy")
    def accept_privacy_message(self):
        self.wait_and_switch_Iframe(index=6)
        self.elementClick(self.accept_privacy, force=True)
        self.exitIframe()

    @allure.step("Clicking on register from homepage")
    def click_register_button(self):
        self.wait_for_element_to_be_visible(self.register)
        self.moveToElementAndClick(self.register)

    @allure.step("Enter the firstname")
    def enter_firstname(self, firstname):
        self.elementSend(self.firstname, firstname)

    @allure.step("Enter the lastname")
    def enter_lastname(self, lastname):
        self.elementSend(self.lastname, lastname)

    @allure.step("Enter the email")
    def enter_email(self, email):
        self.elementSend(self.email, email)

    @allure.step("Click on Submit button")
    def click_submit_button(self):
        self.elementClick(self.submit)

    @allure.step("Check if the success message is displayed")
    def check_registration_message(self):
        return self.isElementDisplayed(self.success_message)
