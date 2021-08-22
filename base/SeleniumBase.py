import datetime

from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from utilities.customlogger import custom_logger
import logging
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
from selenium.webdriver.support.color import Color
from utilities.util import Utilities


class SeleniumBase:
    enableScreenshot = False
    cl = custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.util = Utilities()

    @classmethod
    def EnableScreenshotForTest(cls, screenshot):
        cls.enableScreenshot = screenshot

    """
    Below method is deprecated
    """

    # def ByType(self, locatorType):
    #     locatorType = locatorType.lower()
    #
    #     if locatorType == "id":
    #         return By.ID
    #     elif locatorType == "xpath":
    #         return By.XPATH
    #     elif locatorType == "css":
    #         return By.CSS_SELECTOR
    #     elif locatorType == "link":
    #         return By.LINK_TEXT
    #     elif locatorType == "partial link":
    #         return By.PARTIAL_LINK_TEXT
    #     elif locatorType == "name":
    #         return By.NAME
    #     elif locatorType == "tag":
    #         return By.TAG_NAME
    #     elif locatorType == "class":
    #         return By.CLASS_NAME
    #
    #     else:
    #         self.cl.info("Invalid Locatortype " + str(locatorType))

    def visit(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            self.cl.error("Unable to open URL from :: " + str(url) + '. ' + "Exception Occurred :: " + str(
                e.__class__.__name__))

    def findElement(self, locator, timeout=10, poll_frequency=0.2):
        element = None

        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            self.cl.info(
                "Waiting for " + str(timeout) + " seconds to find the element for locator :: " + str(
                    locator))
            element = wait.until(ec.presence_of_element_located(locator))
            self.cl.info(
                "Element :: " + str(element.id) + " found for locator :: " + str(locator) + ". Session_id :: " + str(
                    element.parent.session_id))

            # element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
            self.driver.execute_script("arguments[0].style.border='2px solid red'", element)

        except Exception as e:
            self.cl.error("No Element found for locator :: " + str(locator) + '. ' + "Exception Occurred :: " + str(
                e.__class__.__name__))
            print_stack()
        return element

    def findElements(self, locator):
        element = []
        try:
            element = self.driver.find_elements(*locator)
            if len(element) > 0:
                self.cl.info("Elements ::  " + str(element.id) + ", session_id :: " + str(
                    element.parent.session_id) + " found for locator :: " + str(locator))

            else:
                self.cl.info(
                    "Elements not found for locator :: " + str(locator) + ". Empty List returned " + str(element))

        except Exception as e:
            self.cl.error(
                "Element could not be found for :: " + str(locator) + '. ' + str(
                    e.__class__.__name__) + ' ' + str(e))
            print_stack()
        return element

    def selectByIndex(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                sel = Select(element)
                sel.select_by_index(value)
                self.cl.info("Selected element with index " + str(value) + " from the drop down using Index position")
                self.saveScreenshots()

            else:
                self.cl.error("Unable to select element by Index. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to select element by Index. Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def selectByVisibleText(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                self.saveScreenshots()
            if element:
                sel = Select(element)
                sel.select_by_visible_text(value)
                self.cl.info("Selected element with value " + str(value) + " from the drop down using Visible Text")
                self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to select element by Visible Text. No element was found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Unable to select element by Visible Text. Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def selectByValue(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                self.saveScreenshots()
            if element:
                sel = Select(element)
                sel.select_by_value(value)
                self.cl.info("Selected element with Name " + str(value) + " from the drop down using Value")
                self.saveScreenshots()

            else:
                self.cl.error(
                    "Unable to select element by Visible Text. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to select element from the dropdown. Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def elementClick(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)

            if element:
                if self.enableScreenshot:
                    self.saveScreenshots()
                element.click()
                self.cl.info("Clicked on Element : " + str(element.id))
            else:
                self.cl.error("Unable to click on locator. No element was found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Unable to click the element: " + str(locator) + ". Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def elementSend(self, locator, message, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                if self.enableScreenshot:
                    self.saveScreenshots()
                element.send_keys(message)
                self.cl.info("Text :: " + str(message) + " entered on element :: " + str(element.id))
                if self.enableScreenshot:
                    self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to send the message on the element. No Element found for the locator ::  " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to send the message on locator: " + str(locator) + "Exception :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            print_stack()

    def getTitle(self):
        title = None
        try:
            title = self.driver.title
            self.cl.info("The current page title is :: " + str(title))

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current page title. Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            print_stack()
        return title



    def getText(self, locator, element=None):
        element_text = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                element_text = element.text
                self.cl.info("Text of the element : " + str(locator) + " is " + element_text)
            else:
                self.cl.error(
                    "Unable to find the text for element. No Element found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to find the text for element : " + str(
                    locator) + ". Following Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            print_stack()

        return element_text

    def getTextElementList(self, locator, elements=None):
        elementText = []
        elementText2 = []
        try:
            if locator:
                elements = self.findElements(locator)
            if len(elements) > 0:
                for item in elements:
                    itemText = item.text
                    elementText.append(itemText)

            else:
                self.cl.error(
                    "Unable to find text for the element list. No elements found for the locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to return text for elements. Following Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()
        return elementText2

    def getAttribute(self, locator, attributeType, element=None):
        elementAttribute = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                elementAttribute = element.get_attribute(attributeType)
                self.cl.info("Value of Attribute :: " + attributeType + " is " + str(elementAttribute))
            else:
                self.cl.error(
                    "Unable to get the value of attribute " + attributeType + ". No element was found for locator :: " + str(
                        locator))
        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(
                    e))
            print_stack()
        return elementAttribute

    # def getAttributeList(self, locator, attributeType, elements=None):
    #     element_attribute = []
    #
    #     try:
    #         if locator:
    #             elements = self.findElements(locator)
    #         if len(elements) > 0:
    #             for item in elements:
    #                 elementAttribute = item.get_attribute(attributeType)
    #                 element_attribute.append(elementAttribute)
    #                 self.cl.info("Value of attribute")
    #         self.cl.info("Attribute list is :: " + str(element_attribute))
    #
    #
    #     except Exception as e:
    #         self.cl.error("Unable to find the value of attribute for element : " + str(
    #             locator) + " exception :: " + str(e))
    #         print_stack()
    #     return element_attribute

    def get_value_of_css_property(self, locator, attributeType, element=None):
        cssAttributeProperty = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                cssAttributeProperty = element.value_of_css_property(property_name=attributeType)
                self.cl.info("Value of CSS Attribute :: " + attributeType + " is " + cssAttributeProperty)
            # if attributeType == 'Color': formatted_name = Color.from_string(cssAttributeProperty).hex self.cl.info(
            # "Value of CSS Attribute :: " + attributeType + " in HEX format is " + cssAttributeProperty) return
            # formatted_name
            else:
                self.cl.error("Unable to find the value of css property for element. No element was found for the "
                              "locator :: " + str(locator))
        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(
                    e))
            print_stack()
        return cssAttributeProperty

    def waitToClickElement(self, locator, time=2, poll=0.2):
        element = None
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[ElementNotInteractableException, ElementNotVisibleException,
                                                     NoSuchElementException, TimeoutException,
                                                     StaleElementReferenceException, ElementClickInterceptedException])
            self.cl.info(
                "Waiting to click on element : " + str(locator) + "for time " + str(time) + "sec")
            element = wait.until(ec.element_to_be_clickable(locator))
            self.cl.info("Element is Available for action")

        except Exception as e:
            self.cl.error("Unable to find the element " + str(
                e.__class__.__name__) + str(e))
            print_stack()
        return element

    def waitForIframe(self, locator, index, time=10, poll=0.5):
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchFrameException, NoSuchElementException, TimeoutException])
            self.cl.info("Waiting to find : " + str(locator["locatorValue"]) + "with index position:: " + str(
                index) + "for time " + str(
                time) + "sec")
            wait.until(
                ec.frame_to_be_available_and_switch_to_it((self.driver.find_elements_by_tag_name(locator)[index])))
            self.cl.info("iFrame is Available for switching")

        except Exception as e:
            self.cl.error("Unable to find the iframe. Following Exception occurred " + '. ' + str(
                e.__class__.__name__) + str(e))

    def elementClear(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                if self.enableScreenshot:
                    self.saveScreenshots()

            if element:
                element.clear()
                self.cl.info("Cleared Element : " + str(element))
                if self.enableScreenshot:
                    self.saveScreenshots()
            else:
                self.cl.error("Unable to clear the element. No element found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Unable to clear element. Exception :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def saveScreenshots(self):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]  # fetch the current TestName
        new_name = test_name.split("::")
        filename = new_name[-1] + "_" + self.util.generate_date_time() + ".png"
        screenshotDirectory = "..//screenshots//" + str(datetime.date.today()) + "//"
        relativeFilename = screenshotDirectory + filename

        currentDirectory = os.path.dirname(__file__)
        destinationPath = os.path.join(currentDirectory, relativeFilename)

        destinationFolder = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            self.driver.save_screenshot(destinationPath)
            self.cl.info("### Screenshot saved at path: " + destinationPath)
        except Exception as e:
            self.cl.error("### Exception Occurred " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def getInnerText(self, locator, element=None):
        innerText = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                innerText = element.get_attribute("innerText")
                self.cl.info("InnerText of element is " + str(innerText))
            else:
                self.cl.error(
                    "Unable to get innerText of element. No element was found for locator :: " + str(
                        locator))
        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(
                    e))
            print_stack()
        return innerText

    def isElementDisplayed(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)

            if element:
                result = element.is_displayed()
                if result:
                    self.cl.info("Element is displayed for locator :: " + str(locator))
                    if self.enableScreenshot:
                        self.saveScreenshots()
                else:
                    self.cl.info("Element is not displayed for locator :: " + str(locator))
            else:
                self.cl.error("Element is not displayed. Unable to find element with locator :: " + str(locator))
                result = False

        except Exception as e:
            self.cl.error(
                "Element is not displayed with locator :: " + str(locator) + " Exception occurred :: " + str(e))
            print_stack()
            result = False
        return result

    def scrollingVertical(self, direction):
        direction = direction.lower()
        try:
            if direction == "up":
                self.driver.execute_script("window.scrollBy(0,-1000);")
                self.cl.info("Scrolling the screen up")

            if direction == "down":
                self.driver.execute_script("window.scrollBy(0,700);")
                self.cl.info("Scrolling the screen down")

        except Exception as e:
            self.cl.error("Exception occurred when trying to scroll the screen :: " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def scrollingHorizontal(self, direction):
        direction = direction.lower()
        try:
            if direction == "left":
                self.driver.execute_script("window.scrollBy(-600,0);")
                if self.enableScreenshot:
                    self.saveScreenshots()
                self.cl.info("Scrolling the screen up")

            if direction == "right":
                self.driver.execute_script("window.scrollBy(1100,0);")
                if self.enableScreenshot:
                    self.saveScreenshots()
                self.cl.info("Scrolling the screen down")

        except Exception as e:
            self.cl.error("Exception occurred when trying to scroll the screen :: " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def switchFrame(self, value):
        try:
            self.driver.switch_to.frame(value)
            self.cl.info("Switched to Iframe :: " + str(value))

        except Exception as e:
            self.cl.error("Error while switching to Iframe" + ". Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def switchParentIframe(self):
        try:
            self.driver.switch_to.parent_frame()
            self.cl.info("Switch to Parent iFrame")
        except Exception as e:
            self.cl.error("Unable to switch  to Parent Frame. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def exitIframe(self):
        try:
            self.driver.switch_to.default_content()
            self.cl.info("Switched to default content. Iframe closed")

        except Exception as e:
            self.cl.error("Error while switching to Default Content. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    # def elementSendSpecial(self, locator, message,element=None):
    #     try:
    #         element = self.findElement(locator)
    #         if element:
    #             for items in message:
    #                 element.send_keys(items)
    #         self.cl.info("Text : " + message + " entered on locator: " + str(locator))
    #
    #
    #     except Exception as e:
    #         self.cl.info(
    #             "Unable to send the message on locator: " + str(
    #                 locator["locatorValue"]) + ". Following Exception occurred :: " + str(e))
    #         print_stack()

    def slider(self, locator, XCORD, YCORD, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.saveScreenshots()
                self.actions.drag_and_drop_by_offset(source=element, xoffset=XCORD, yoffset=YCORD).perform()
                self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to perform slider operation on element. No element was found for locator " + str(locator))
        except Exception as e:
            self.cl.error("Exception occurred during sliding. Following Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def doubleClick(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.saveScreenshots()
                self.actions.double_click(element).perform()
                self.cl.info("Double Clicked on :: " + str(element))
            else:
                self.cl.error(
                    "Unable to perform double click on element. No element was found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Exception occurred during Double Click. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack()

    def browserRefresh(self):
        try:
            self.driver.refresh()
            self.cl.info("Refreshing the current window")
        except Exception as e:
            self.cl.error("Unable to refresh the browser. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))

    def currentBrowserWindow(self):
        current_window = None
        try:
            current_window = self.driver.current_window_handle
            self.cl.info("The current window is :: " + str(current_window))

        except Exception as e:
            self.cl.error('Unable to get the current window. Exception Occurred :: ' + str(
                e.__class__.__name__) + str(e))

        return current_window

    def allBrowserWindow(self):
        all_window = None
        try:
            all_window = self.driver.window_handles
            self.cl.info("All available Window's are :: " + str(all_window))

        except Exception as e:
            self.cl.info('Unable to get all the windows. Exception Occurred :: ' + str(
                e.__class__.__name__) + str(e))
        return all_window

    #
    def switchWindow(self, windowNumber: int):
        try:
            allWindow = self.allBrowserWindow()
            self.driver.switch_to.window(allWindow[windowNumber])
            self.cl.info("Switched to new window :: " + str(allWindow[windowNumber]))
        except Exception as e:
            self.cl.info("Unable to switch to new window. Following Exception occurred :: " + str(
                e.__class__.__name__) + " "+ str(e))

    #
    # def switch_to_parent_window(self):
    #     try:
    #         all_window_available = self.all_window_handles()
    # 
    #         for items in all_window_available:
    #             if items == all_windows[0]:
    #                 self.driver.switch_to.window(items)
    #                 self.cl.info("Switched to window :: " + str(items))
    # 
    #     except Exception as e:
    #         self.cl.info("Unable to  to new window. Following Exception occurred :: " + str(e))

    def browserBack(self):
        self.driver.back()

    def browserForward(self):
        self.driver.forward()

    # def action(self):
    #     try:
    #         self.actions.key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
    #         # self.actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    #
    #     except Exception as e:
    #         self.cl.info("Unable to press ENTER key. Following Exception occurred :: " + str(e))
    #
    # def enter(self):
    #     try:
    #         self.actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    #         self.cl.info("Pressed ENTER")
    #     except Exception as e:
    #         self.cl.info("Unable to press ENTER key. Following Exception occurred :: " + str(e))

    # def close_new_window(self):
    #     try:
    #         self.actions.key_down(Keys.CONTROL).send_keys('W').perform()
    #         self.cl.info("Pressing CTRL + W to close the new window")
    #     except Exception as e:
    #         self.cl.error("Unable to perform Action :: CTRL + W. Following Exception occurred :: " + str(e))
    #         print_stack()

    def js_element_click(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.driver.execute_script("arguments[0].click();", element)
            else:
                self.cl.error("Unable to click on element. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to click on element :: " + str(element) + ". Following Exception occurred :: " + str(
                    e.__class__.__name__) + str(e))

    def js_select_list(self, locator, message):
        try:
            element = self.findElement(locator)
            self.driver.execute_script("arguments[0].removeAttribute('readonly','readonly');", element)
            element.send_keys(message)
            self.cl.info("Sending message :: " + str(message) + "locator :: " + str(locator["locatorValue"]))

        except Exception as e:
            self.cl.error("Exception Occurred. Following Exception :: " + str(e))
            print_stack()

    def stopPageLoading(self):
        try:
            self.driver.execute_script("return window.stop")
            self.cl.info("Page load stop")
        except Exception as e:
            self.cl.error("Unable to stop the page load. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))

    # def js_double_click(self,locator,locatorType):
    #     try:
    #         element = self.findElement(locator,locatorType)
    #         self.driver.execute_script("var evt = document.createEvent('MouseEvents');"+
    #         "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);"+
    #         "arguments[0].dispatchEvent(evt);", element);

    #         self.cl.info("Double clicked element :: " + str(element))

    #     except:
    #         raise Exception
    #         self.cl.info("Unable to Double click element :: " + str(element))

    def rightClick(self, locator, element=None):

        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.actions.context_click(element).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
                self.saveScreenshots()

            else:
                self.cl.error(
                    "Unable to perform right click on element. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to right click on element " + str(element) + ". Following Exception Occurred :: " + str(
                    e.__class__.__name__) + " " + str(e))


    def assertTitle(self, expectedTitle):
        actualTile = self.getTitle()
        assert_that(actualTile).is_equal_to(expectedTitle)

    def assertTitleContains(self, titleSubString):
        result = None
        try:
            result = WebDriverWait(self.driver,11,0.2).until(ec.title_contains(titleSubString))
            self.cl.info("Title of the Page contains text :: " + str(titleSubString))

        except Exception as e:
            self.cl.error("Title of the Page does not contains text :: " + str(titleSubString) + ". Following Exception occurred :: " + str(
                    e.__class__.__name__) + " " + str(e))
        finally:
            assert_that(result).is_true()


    def assertElementDisplayed(self, locator, element=None):
        assert_that(self.isElementDisplayed(locator, element)).is_true()

    def assertText(self,locator, expectedText, element=None):
        text = self.getText(locator, element)
        assert_that(text).is_equal_to(expectedText)

    def assertTextContains(self, textSubString, locator, element=None):
        text = self.getText(locator, element)
        assert_that(text).contains_ignoring_case(textSubString)
