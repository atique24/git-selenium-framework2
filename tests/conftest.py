import os
import datetime
import allure
import pytest
from base.WebDriverFactory import WebDriverFactory
from pages.page_login.login_page import LoginPage
from pages.page_register.register_page import Registration
from utilities.customlogger import custom_logger
import logging
from base.SeleniumBase import SeleniumBase

driver = None

cl = custom_logger(logging.INFO)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Type in browser type")
    parser.addoption("--screenshot", action="store_true", default=False, help="To enable/disable screenshots")
    parser.addoption("--headless", action="store_true", default=False, help="Browser Headless mode")
    parser.addoption("--url", action="store", default=None, help="URL of the Application under test")
    parser.addoption("--env", action="store", default="batstore", help="URL of the Application under test")
    parser.addoption("--mobile", action="store_true", default=False, help="Run Test in Chrome Mobile Emulator")
    parser.addoption("--device", action="store", default="iPhone X", help="Run Test in Chrome Mobile Emulator")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def screenshot(request):
    return request.config.getoption("--screenshot")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def mobile(request):
    return request.config.getoption("--mobile")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


# ---------------------for new session for each Test class
@pytest.fixture(scope="class")
def oneTimeSetup(request, browser, screenshot, headless, url, env, mobile, device):
    cl.info("############### Starting Test :: " + os.environ.get('PYTEST_CURRENT_TEST').split(' ')[
        0] + " #######################")
    wdf = WebDriverFactory(browser, headless, url, mobile, device)
    SeleniumBase.EnableScreenshotForTest(screenshot)  # ------ Enable / Disable screenshot
    SeleniumBase.setEnv(env)

    global driver
    driver = wdf.get_browser_instance()

    if request.cls is not None:
        request.cls.driver = driver
        yield driver
        driver.quit()
        cl.info("Quiting the browser session")
        cl.info("############### Test Ended :: " + os.environ.get('PYTEST_CURRENT_TEST').split(' ')[
            0] + " #######################")


@pytest.fixture()
def sb(oneTimeSetup):
    return SeleniumBase(driver)


# for single driver session for all test class
# @pytest.fixture(scope="session")
# def oneTimeSetup(request, browser):
#     print("This is one time setup")
#     wdf = WebDriverFactory(browser)
#     driver = wdf.get_browser_instance()
#     if hasattr(request, "cls") and request.cls is not None:
#     request.cls.driver = driver
#     yield driver
#     driver.quit()

# -------------attach screenshot to allure report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        cl.error(rep.longreprtext + rep.caplog + rep.capstdout + rep.capstderr)
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'oneTimeSetup' in item.fixturenames:
                    driver = item.funcargs['oneTimeSetup']
                else:
                    print('Fail to take screen-shot')
            allure.attach(
                driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
            sel = SeleniumBase(driver)
            sel.saveScreenshots()
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


def pytest_csv_register_columns(columns):
    columns['date'] = lambda item, report: {'date': str(datetime.datetime.now())}


@pytest.fixture(autouse=True)
def login_page(oneTimeSetup):
    return LoginPage(oneTimeSetup)


@pytest.fixture(autouse=True)
def register_page(oneTimeSetup):
    return Registration(oneTimeSetup)