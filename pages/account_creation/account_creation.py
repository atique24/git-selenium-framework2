from base.selenium_driver import SeleniumDriver
from utilities.customlogger import custom_logger
import logging
from pages.mobile_page.mobile_page import MobilePage
import time
from pages.account_creation.account_creation_locators import *


class Account(SeleniumDriver):
    cl = custom_logger(loglevel=logging.INFO)


    def __init__(self,driver):
        super(Account, self).__init__(driver)
        self.driver = driver
        self.mb = MobilePage(self.driver)


    def click_tv_tab(self):
        self.elementClick(tv)

    def add_to_wishlist(self,emailAddress,message):
        self.click_tv_tab()
        self.elementClick(add_to_wishlist)
        self.elementClick(share_wishlist)
        self.elementSend(emailaddress_wishlist,emailAddress)
        self.elementSend(message_wishlist,message)
        self.elementClick(share_wishlist)
        return self.isElementDisplayed(message_success_sharelist)



    def register(self,firstName,lastName,emailAddress,password,confirmPassword):
        self.elementClick(account)
        self.elementClick(register)
        self.elementSend(firstname,firstName)
        self.elementSend(lastname,lastName)
        self.elementSend(email_address, emailAddress)
        self.elementSend(password_loc, password)
        self.elementSend(confirmation, confirmPassword)
        self.elementClick(checkbox)
        self.elementClick(register2)
        return self.isElementDisplayed(success_message)












