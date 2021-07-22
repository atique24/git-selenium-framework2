# locators
from selenium.webdriver.common.by import By


class LoginPageLocators:
    # register = {"locatorType": By.XPATH, "locatorValue": "//span[text()='Register']"}
    # number = {"locatorType": By.ID, "locatorValue": "MSISDN"}
    # error_message = {"locatorType": By.XPATH, "locatorValue": "//span[contains(text(),'Something')]"}

    register = (By.XPATH, "//span[text()='Register']")
    number = (By.ID, "MSISDN")
    error_message = (By.XPATH, "//span[contains(text(),'Something1')]")