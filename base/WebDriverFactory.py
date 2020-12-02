from selenium import webdriver
from utilities.customlogger import custom_logger
import logging

class WebDriverFactory():
    cl = custom_logger(logging.INFO)

    def __init__(self,browser):
        self.browser = browser

    def get_browser_instance(self):
        if self.browser == "FF":
            driver = webdriver.Firefox(executable_path="drivers//geckodriver.exe")

        elif self.browser == "Chrome":
            driver = webdriver.Chrome(executable_path='drivers//chromedriver.exe')

        elif self.browser == "IE":
            driver = webdriver.Ie(executable_path='drivers//IEDriverServer.exe')

        else:
            driver = webdriver.Chrome(executable_path='drivers//chromedriver.exe')


        baseUrl = "http://live.demoguru99.com/index.php/"
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseUrl)
        self.cl.info('Launching the URL :: ' + str(baseUrl) + ' on browser :: ' + str(self.browser))

        return driver



