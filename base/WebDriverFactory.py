from selenium import webdriver
from utilities.customlogger import custom_logger
import logging
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datafiles import config
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from msedge.selenium_tools import EdgeOptions


class WebDriverFactory():
    cl = custom_logger(logging.INFO)

    def __init__(self, browser, headless):
        self.browser = browser
        self.headless = headless

    def get_browser_instance(self):
        if self.browser.lower() == "firefox":
            options = FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
            #options.add_argument("--disable-gpu")
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile, options=options)

        elif self.browser.lower() == "chrome":
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument('headless')
            chrome_options.add_argument('ignore-certificate-errors')
            #chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_experimental_option('prefs', {'geolocation': True})
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            #driver = webdriver.Chrome(options=chrome_options, executable_path='drivers//chromedriver.exe')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        elif self.browser.lower() == "ie":
            driver = webdriver.Ie(IEDriverManager().install())

        elif self.browser.lower() == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("headless")
            options.add_argument("disable-gpu")
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())

        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get(config.baseUrl)
        driver.implicitly_wait(5)
        if self.headless:
            self.cl.info("Starting " + str(self.browser) + " browser "+ " in headless mode")
        else:
            self.cl.info("Starting " + str(self.browser) + " browser ")

        self.cl.info("Opening the URL :: " + str(config.baseUrl))

        return driver
