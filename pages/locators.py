# locators
from selenium.webdriver.common.by import By


class LoginPageLocators:

    username = (By.NAME, "userName")
    password = (By.NAME, "password")
    submit = (By.NAME, "submit")
    success_message=(By.XPATH, "//h3[text()='Login Successfully']")
    sign_off = (By.LINK_TEXT,"SIGN-OFF")


class RegisterLocators:

    register = (By.LINK_TEXT,"REGISTER")
    firstname = (By.NAME,"firstName")
    lastname = (By.NAME,"lastName")
    phone = (By.NAME, "phone")
    email = (By.NAME, "userName")
    submit = (By.NAME, "submit")
    success_message=(By.XPATH,"//font[contains(text(),'Thank you')]")