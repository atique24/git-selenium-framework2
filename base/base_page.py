from base.selenium_driver import SeleniumDriver
from utilities.util import Utilities


class BasePage(SeleniumDriver):
    def __init__(self,driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Utilities()


    def verify_page_title(self, titleToVerify):
        actualTitle = self.getTitle()
        return self.util.verify_text_contains(actualText = actualTitle, expectedText=titleToVerify)

    def verify_table_header(self, locator, locatorType, tableToVerify):
        actualTableHeader = self.getTextElementList(locator, locatorType)
        return self.util.listcompare(actualList=actualTableHeader, expectedList=tableToVerify)

    def verify_value(self, locator, locatorType, attributeType, expectedValue):
        result = self.getAttribute(locator, locatorType, attributeType)
        return self.util.verify_value(actualValue=result, expectedValue=expectedValue)

    def verify_text_substring(self, locator, locatorType, attributeType, expectedValue):
        result = self.getAttribute(locator, locatorType, attributeType)
        return self.util.verify_text_contains(actualText=result, expectedText=expectedValue)

    def verify_css_attribute(self, locator, locatorType, attributeType, expectedValue):
        result = self.get_value_of_css_property(locator, locatorType, attributeType)
        return self.util.verify_text(actualText=result, expectedText=expectedValue)
