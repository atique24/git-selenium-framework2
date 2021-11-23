from selenium import webdriver
from utilities.customlogger import custom_logger
import logging
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datafiles.config_browserstack import *
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from msedge.selenium_tools import EdgeOptions
from browserstack.local import Local


class WebDriverFactory:
    cl = custom_logger(logging.INFO)

    def __init__(self, browser, headless, url, mobile, device):
        self.browser = browser
        self.headless = headless
        self.baseUrl = url
        self.mobile = mobile
        self.device = device

    def get_browser_instance(self):
        try:
            if self.browser.lower() == "firefox":
                options = FirefoxOptions()
                if self.headless:
                    options.add_argument("--headless")
                    options.add_argument("-width=1920")
                    options.add_argument("-height=1080")
                # options.add_argument("--disable-gpu")
                profile = webdriver.FirefoxProfile()
                # options.add_argument("--private")
                profile.accept_untrusted_certs = True
                driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=10).install(), firefox_profile=profile,
                                           options=options)

            elif self.browser.lower() == "chrome":
                chrome_options = Options()
                if self.headless:
                    chrome_options.add_argument('headless')
                    chrome_options.add_argument('window-size=1920x1080')
                chrome_options.add_argument('ignore-certificate-errors')

                if self.mobile:
                    mobile_emulation = {"deviceName": self.device}
                    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

                chrome_options.add_argument('--incognito')
                # chrome_options.add_argument('--start-maximized')
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
                #chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
                chrome_options.add_argument('--log-level=3')
                driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=10).install(), options=chrome_options)

            elif self.browser.lower() == "ie":
                driver = webdriver.Ie(IEDriverManager().install())

            elif self.browser.lower() == "edge":
                options = EdgeOptions()
                if self.headless:
                    options.add_argument('headless')
                    options.add_argument('window-size=1920x1080')
                options.use_chromium = True
                options.add_argument('ignore-certificate-errors')
                options.add_experimental_option('useAutomationExtension', False)
                options.add_argument('--inprivate')
                options.add_argument('--log-level=3')
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                driver = webdriver.Chrome(EdgeChromiumDriverManager(cache_valid_range=10, log_level=1).install(), options=options)

            elif self.browser.lower() == 'browserstack':
                bs_local = Local()
                bs_local_args = {"key": key, "localIdentifier": localIdentifier}
                bs_local.start(**bs_local_args)
                driver = webdriver.Remote(command_executor=bb_url, desired_capabilities=browser_config)

            # elif self.browser.lower() =="docker":
            #     options = FirefoxOptions()
            #     options.add_argument("--headless")
            #     options.add_argument("-width=1920")
            #     options.add_argument("-height=1080")
            #     profile = webdriver.FirefoxProfile()
            #     # options.add_argument("--private")
            #     profile.accept_untrusted_certs = True
            #     driver = webdriver.Remote(command_executor="http://localhost:4444", options=options, browser_profile=profile)

            else:
                raise ValueError


            if self.headless:
                self.cl.info("Starting " + str(self.browser).upper() + " browser in headless mode")
            else:
                self.cl.info("Starting " + str(self.browser).upper() + " browser ")
                if self.browser.lower() == "browserstack" and 'browserName' in browser_config.keys():
                    pass
                else:
                    driver.maximize_window()

            driver.delete_all_cookies()
            #driver.set_page_load_timeout(30)

            if self.baseUrl:
                driver.get(self.baseUrl)
                self.cl.info("Opening the URL :: " + str(self.baseUrl))

            # driver.implicitly_wait(10)
            return driver


        except ValueError as val:
            self.cl.error("Browser not supported :: " + str(
                self.browser) + ". Supported browser types are Chrome, Firefox, Edge. Exception occurred. :: " + str(
                val.__class__.__name__) + ' ' + str(val))
            raise val

        except Exception as e:
            self.cl.error("Exception occurred. :: " + str(
                e.__class__.__name__) + ' ' + str(e))
            raise e
