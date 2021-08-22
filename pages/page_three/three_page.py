import time

from base.SeleniumBase import SeleniumBase
from selenium.webdriver.common.by import By



class ThreePage(SeleniumBase):

    """locators"""
    login = (By.XPATH, "//span[text()='Log in']")
    msisdn = (By.ID, "MSISDN")
    next = (By.ID , "login-next-msisdn")
    errorMessage = (By.XPATH,"//span[contains(text(),'wrong')]")
    link = (By.LINK_TEXT, "Gender pay gap report")

    def __init__(self,driver):
        super(ThreePage, self).__init__(driver)
        self.driver = driver

    def click_login_link(self):
        self.elementClick(self.login)

    def enter_msisdn(self):
        self.elementSend(self.msisdn,12345)

    def click_next_button(self):
        self.elementClick(self.next)

    def verify_error_message(self):
        return self.errorMessage

    def click_link_gender(self):
        self.elementClick(self.link)
        self.switchWindow(1)








