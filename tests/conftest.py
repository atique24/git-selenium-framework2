import pytest
from base.WebDriverFactory import WebDriverFactory
from utilities.customlogger import custom_logger
import logging
import datetime
import os

driver = None

cl = custom_logger(logging.INFO)

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

#---------------------for new session for each Test class
@pytest.fixture(scope="class")
def oneTimeSetup(request,browser):
    cl.info("Launching browser :: " + str(browser))
    wdf = WebDriverFactory(browser)
    global driver
    driver = wdf.get_browser_instance()
    if request.cls is not None:
        request.cls.driver = driver
        yield driver
        driver.quit()

#for single driver session for all test class
# @pytest.fixture(scope="session")
# def oneTimeSetup(request, browser):
#     print("This is one time setup")
#     wdf = WebDriverFactory(browser)
#     driver = wdf.get_browser_instance()
#     if hasattr(request, "cls") and request.cls is not None:
#     request.cls.driver = driver
#     yield driver
#     driver.quit()



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)












