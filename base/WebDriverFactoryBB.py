import logging

from selenium import webdriver

from utilities.customlogger import custom_logger
from datafiles.config_browserstack import *


class WebdriverFactoryBB():
    cl = custom_logger(logging.INFO)

    def get_browser_instance(self):
        driver = webdriver.Remote(command_executor=bb_url,desired_capabilities=browser_config)
        driver.get(baseUrl)
        return driver
