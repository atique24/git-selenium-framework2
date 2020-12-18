from base.selenium_driver import SeleniumDriver
from utilities.customlogger import custom_logger
import logging
from pages.mobile_page.mobile_page import MobilePage
import time


class Account(SeleniumDriver):
    cl = custom_logger(loglevel=logging.INFO)

    def __init__(self,driver):
        super(Account, self).__init__(driver)
        self.driver = driver
        self.mb = MobilePage(self.driver)


    #locators
    _account = "//a/span[text()='Account']"
    _register = "Register"
    _firstname = "firstname"
    _lastname = "lastname"
    _email_address = "email_address"
    _password = "password"
    _confirmation = "confirmation"
    _checkbox = "is_subscribed"
    _register2= "//button[@title='Register']"
    _success_message = "//span[text()='Thank you for registering with Main Website Store.']"
    _tv = "TV"
    _add_to_wishlist = "//a[@title='LG LCD']//following-sibling::div/child::div/ul/li/a"
    _share_wishlist = "//span[text()='Share Wishlist']"
    _emailaddress_wishlist = "email_address"
    _message_wishlist = "message"
    _message_success_sharelist = "//span[text()='Your Wishlist has been shared.']"


    def click_tv_tab(self):
        self.elementClick(self._tv,'link')

    def add_to_wishlist(self,emailAddress,message):
        self.click_tv_tab()
        self.elementClick(self._add_to_wishlist,'xpath')
        self.elementClick(self._share_wishlist,'xpath')
        self.elementSend(self._emailaddress_wishlist,'id',emailAddress)
        time.sleep(5)
        self.elementSend(self._message_wishlist, 'id', message)
        time.sleep(5)
        self.elementClick(self._share_wishlist,'xpath')
        return self.isElementDisplayed(self._message_success_sharelist,'xpath')



    def register(self,firstName,lastName,emailAddress,password,confirmPassword):
        self.elementClick(self._account,'xpath')
        self.elementClick(self._register,'link')
        self.elementSend(self._firstname,'id',firstName)
        self.elementSend(self._lastname,'id',lastName)
        self.elementSend(self._email_address, 'id', emailAddress)
        self.elementSend(self._password, 'id', password)
        self.elementSend(self._confirmation, 'id', confirmPassword)
        self.elementClick(self._checkbox, 'id')
        self.elementClick(self._register2,'xpath')
        return self.isElementDisplayed(self._success_message,'xpath')











