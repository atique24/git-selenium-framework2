import pytest
from base.WebDriverFactory import WebDriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

#for new session for each Test class
@pytest.fixture(scope="class")
def oneTimeSetup(request,browser):
    print("This is one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_browser_instance()

    if request.cls is not None:
        request.cls.driver = driver

#for single driver session for all test class
# @pytest.fixture(scope="session")
# def oneTimeSetup(request, browser):
#     print("This is one time setup")
#     wdf = WebDriverFactory(browser)
#     driver = wdf.get_browser_instance()
#
#     if hasattr(request, "cls") and request.cls is not None:
#     request.cls.driver = driver



    yield driver
    driver.quit()
