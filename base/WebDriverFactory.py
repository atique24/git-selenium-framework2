from selenium import webdriver
from utilities.customlogger import custom_logger
import logging
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datafiles import config
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverFactory():
    cl = custom_logger(logging.INFO)

    def __init__(self, browser):
        self.browser = browser

    def get_browser_instance(self):
        if self.browser == "FF":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        elif self.browser == "Chrome":
            chrome_options = Options()
            # download_dir = "C://Users//A610037//Downloads//download_chrome"
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_experimental_option('prefs', {'geolocation': True})
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

            #driver = webdriver.Chrome(options=chrome_options, executable_path='drivers//chromedriver.exe')
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

        elif self.browser == "Ie":
            driver = webdriver.Ie(IEDriverManager().install())

        elif self.browser == "Edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())

        else:
            driver = webdriver.Chrome(executable_path='drivers//chromedriver.exe')

        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get(config.baseUrl)
        driver.implicitly_wait(5)

        self.cl.info('Launching the URL :: ' + str(config.baseUrl) + ' on browser :: ' + str(self.browser))

        return driver
