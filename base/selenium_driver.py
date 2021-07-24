from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from utilities.customlogger import custom_logger
import logging
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
from selenium.webdriver.support.color import Color
from utilities.util import Utilities


# noinspection PyBroadException
class SeleniumDriver:
    cl = custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.util = Utilities()

    def ByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial link":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "class":
            return By.CLASS_NAME

        else:
            self.cl.info("Invalid Locatortype " + str(locatorType))

    def findElement(self, locator, timeout=10, poll_frequency=0.2):
        element = None
        try:
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.2)
            element = wait.until(EC.presence_of_element_located(locator))
            self.cl.info(
                "Waiting for time :: " + str(timeout) + " seconds to find the element for locator :: " + str(
                    locator))

            # element = self.driver.find_element(locator["locatorType"], locator["locatorValue"])
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
            self.cl.info(
                "Element found for locatorValue :: " + str(locator))

        except Exception as e:
            self.cl.info("Element could not be found for :: " + str(locator) + ' ' + str(e))
            print_stack()
        return element

    def findElements(self, locator):
        element = []
        try:
            element = self.driver.find_elements(*locator)
            if len(element) > 0:
                self.cl.info("Element found for locator :: " + str(locator))

            else:
                self.cl.info(
                    "Elements not found for locator :: " + str(locator) + ". Empty List returned " + str(element))


        except Exception as e:
            self.cl.warning(
                "Element could not be found for :: " + str(locator) + '' + str(e))
            print_stack()
        return element

    def selectFromDropdown(self, locator, value, selectByValue=False, selectByVisibleText=False, selectByIndex=False):
        try:
            element = self.findElement(locator)
            sel = Select(element)

            if selectByValue:
                sel.select_by_value(value)
                self.cl.info("Selected element with Name " + str(value) + " from the drop down using Value")

            elif selectByVisibleText:
                sel.select_by_visible_text(value)
                self.cl.info("Selected element with value " + str(value) + " from the drop down using Visible Text")

            elif selectByIndex:
                sel.select_by_index(value)
                self.cl.info("Selected element with index " + str(value) + " from the drop down using Index position")

            else:
                self.cl.error("Please select Value or text or index")

        except Exception as e:
            self.cl.warning("Unable to select element from the dropdown. Exception occurred :: " + str(e))
            print_stack()

    def elementClick(self, locator):
        try:
            element = self.findElement(locator)
            element.click()
            self.cl.info("Clicked on Element : " + str(element))

        except Exception as e:
            self.cl.info("Unable to click the element: " + str(locator) + ". Exception occurred :: " + str(e))
            print_stack()

    def elementSend(self, locator, message):
        try:
            element = self.findElement(locator)
            element.clear()
            element.send_keys(message)
            self.cl.info("Text : " + str(message) + " entered on locator: " + str(locator))
        except Exception as e:
            self.cl.info(
                "Unable to send the message on locator: " + str(locator) + "Exception :: " + str(e))
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getText(self, locator):
        element_text = None
        try:
            element = self.findElement(locator)
            element_text = element.text
            self.cl.info("Text of the element : " + str(locator) + " is " + element_text)
            return element_text
        except Exception as e:
            self.cl.info(
                "Unable to find the text for element : " + str(
                    locator) + ". Following Exception occurred :: " + str(e))
            print_stack()
        return element_text

    def getTextElementList(self, locator):
        elementText = []
        elementText2 = []
        try:
            element = self.findElements(locator)
            for item in element:
                itemtext = item.text
                elementText.append(itemtext)

            elementText2 = list(filter(None, elementText))
            self.cl.info(elementText2)
            return elementText2

        except Exception as e:
            self.cl.info("Unable to return text for elements. Following Exception occurred :: " + str(e))
            print_stack()
        return elementText2

    def getAttribute(self, locator, attributeType):
        elementAttribute = None
        try:
            element = self.findElement(locator)
            elementAttribute = element.get_attribute(attributeType)
            self.cl.info("Value of Attribute :: " + attributeType + " is " + str(elementAttribute))
            return elementAttribute
        except Exception as e:
            self.cl.info(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following exception occurred :: " + str(
                    e))
            print_stack()
        return elementAttribute

    def getAttributelist(self, locator, attributeType):
        element_attribute = []

        try:
            element = self.findElements(locator)
            for item in element:
                elementAttribute = item.get_attribute(attributeType)
                element_attribute.append(elementAttribute)
                self.cl.info("Value of Attribute :: " + attributeType + " is " + elementAttribute)
            return element_attribute

        except Exception as e:
            self.cl.info("Unable to find the value of attribute for element : " + str(
                locator) + " exception :: " + str(e))
            print_stack()
        return element_attribute

    def get_value_of_css_property(self, locator, attributeType):
        cssAttributeProperty = None
        try:
            element = self.findElement(locator)
            cssAttributeProperty = element.value_of_css_property(property_name=attributeType)
            self.cl.info("Value of CSS Attribute :: " + attributeType + " is " + cssAttributeProperty)
            if attributeType == 'Color':
                formatted_name = Color.from_string(cssAttributeProperty).hex
                self.cl.info("Value of CSS Attribute :: " + attributeType + " in HEX format is " + cssAttributeProperty)
                return formatted_name
            else:
                return cssAttributeProperty

        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following Exception occurred :: " + str(
                    e))
            print_stack()
        return cssAttributeProperty

    def explicitwait(self, locator, time=2, poll=0.2):
        element = None
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[ElementNotInteractableException, ElementNotVisibleException,
                                                     NoSuchElementException, TimeoutException,
                                                     StaleElementReferenceException, ElementClickInterceptedException])
            self.cl.info(
                "Waiting to click on element : " + str(locator) + "for time " + str(time) + "sec")
            element = wait.until(EC.element_to_be_clickable(locator))
            self.cl.info("Element is Available for action")

        except:
            self.cl.error("Unable to find the element")
            print_stack()
        return element

    def explicit_wait_for_iframe(self, locator, index, time, poll):
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchFrameException, NoSuchElementException, TimeoutException])
            self.cl.info("Waiting to find : " + str(locator["locatorValue"]) + "with index position:: " + str(
                index) + "for time " + str(
                time) + "sec")
            element = wait.until(
                EC.frame_to_be_available_and_switch_to_it((self.driver.find_elements_by_tag_name(locator)[index])))
            self.cl.info("iFrame is Available for switching")

        except TimeoutException:
            self.cl.error("Unable to find the iframe")

    def isElementPresent(self, locator):
        try:
            element = self.findElements(locator)
            self.cl.info(element)
            if len(element) > 0:
                self.cl.info("Element with locator " + str(locator) + " is present")
                return True
            else:
                self.cl.info("Element with locator " + str(locator) + " is not present")
                return False

        except Exception as e:
            self.cl.info("exception occurred :: " + str(e))
            print_stack()
            return False

    def elementClear(self, locator):
        element = None
        try:
            element = self.findElement(locator)
            element.clear()
            self.cl.info("Cleared Element : " + str(element))

        except Exception as e:
            self.cl.info("Unable to find element. Exception :: " + str(e))
            print_stack()

    def saveScreenshots(self):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]  # fetch the current testname
        new_name = test_name.split("::")
        filename = new_name[-1] + "_" + self.util.generate_date_time() + ".png"
        screenshotDirectory = "..//screenshots//"
        relativeFilename = screenshotDirectory + filename

        currentDirectory = os.path.dirname(__file__)
        destinationPath = os.path.join(currentDirectory, relativeFilename)

        destinationFolder = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            self.driver.save_screenshot(destinationPath)
            self.cl.info("### Screenshot saved at path: " + destinationPath)
        except:
            self.cl.warning("### Exception Occurred")
            print_stack()

    def isElementDisplayed(self, locator):
        element = None
        element = self.findElement(locator)
        result = None
        try:
            result = element.is_displayed()
            if result is True:
                self.cl.info("Element is displayed with locator :: " + str(locator))

            else:
                self.cl.info("Element is not displayed with locator :: " + str(locator))

        except Exception as e:
            self.cl.warning("Exception occurred while executing isElementDisplayed :: exception occurred :: " + str(e))
            print_stack()
        return result

    def wait_presence_of_element_located(self, locator, timeout, poll):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll)
            element = wait.until(EC.presence_of_element_located(locator))


        except Exception as e:
            self.cl.info("Unable to find element." + str(e))

    def scrollingVertical(self, direction):
        direction = direction.lower()
        try:
            if direction == "up":
                self.driver.execute_script("window.scrollBy(0,-1000);")
                self.cl.info("Scrolling the screen up")

            if direction == "down":
                self.driver.execute_script("window.scrollBy(0,700);")
                self.cl.info("Scrolling the screen down")

        except:
            self.cl.warning("Exception occurred when trying to scroll the screen")
            print_stack()

    def scrollingHorizontal(self, direction):
        direction = direction.lower()
        try:
            if direction == "left":
                self.driver.execute_script("window.scrollBy(-600,0);")
                self.cl.info("Scrolling the screen up")

            if direction == "right":
                self.driver.execute_script("window.scrollBy(1100,0);")
                self.cl.info("Scrolling the screen down")

        except:
            self.cl.warning("Exception occured when trying to scroll the screen")
            print_stack()

    def switchFrame(self, value):
        try:
            self.driver.switch_to.frame(value)
            self.cl.info("Switched to Iframe :: " + str(value))

        except Exception as e:
            self.cl.error("Error while switching to Iframe" + ". Following Exception occurred :: " + str(e))
            print_stack()

    def switchParentFrame(self):
        try:
            self.driver.switch_to.parent_frame()
        except Exception as e:
            self.cl.info("Unable to  to Parent Frame. Following Exception occurred :: " + str(e))
            print_stack()

    def switch_default_content(self):
        try:
            self.driver.switch_to.default_content()
            self.cl.info("Switched to default content")

        except Exception as e:
            self.cl.error("Error while switching to Default Content. Exception occurred :: " + str(e))
            print_stack()

    def elementSendSpecial(self, locator, message):
        try:
            element = self.findElement(locator)
            for items in message:
                element.send_keys(items)
            self.cl.info("Text : " + message + " entered on locator: " + str(locator["locatorValue"]))
        except Exception as e:
            self.cl.info(
                "Unable to send the message on locator: " + str(
                    locator["locatorValue"]) + ". Following Exception occurred :: " + str(e))
            print_stack()

    def slider(self, locator, xcord, ycord):
        try:
            element = self.findElement(locator)
            self.actions.drag_and_drop_by_offset(source=element, xoffset=xcord, yoffset=ycord).perform()
        except Exception as e:
            self.cl.info("Exception occurred during sliding. Following Exception occurred :: " + str(e))
            print_stack()

    def double_clickk(self, locator):
        try:
            element = self.findElement(locator)
            self.actions.double_click(element).perform()
            self.cl.info("Double Clicked on :: " + str(element))
        except Exception as e:
            self.cl.info("Exception occurred during Double Click. Following Exception occurred :: " + str(e))
            print_stack()

    def browserRefresh(self):
        self.driver.refresh()

    def current_handle_window(self):
        current_window = None
        try:
            current_window = self.driver.current_window_handle
            self.cl.info("The current window handle is :: " + str(current_window))
            # return current_window

        except Exception as e:
            self.cl.info('Unable to get the current window. Exception Occurred :: ' + str(e))
        return current_window

    # def all_window_handles(self):
    #     all_window_available = None
    #     try:
    #         all_window_available = self.driver.window_handles
    #         self.cl.info("All available Window's are :: " + str(all_handles))
    # 
    #     except Exception as e:
    #         self.cl.info('Unable to get all the windows. Exception Occured :: ' + str(e))
    #     return all_window_available
    # 
    # def switching_to_window(self):
    #     try:
    #         current_window = self.current_handle_window()
    #         all_window_available = self.all_window_handles()
    # 
    #         for items in all_window_available:
    #             if items != current_window:
    #                 self.driver.switch_to.window(items)
    #                 self.cl.info("Switched to window :: " + str(items))
    # 
    #     except Exception as e:
    #         self.cl.info("Unable to switch to new window. Following Exception occurred :: " + str(e))
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

    def browserback(self):
        self.driver.back()

    def browserForward(self):
        self.driver.forward()

    def action(self):
        try:
            self.actions.key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
            # self.actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        except Exception as e:
            self.cl.info("Unable to press ENTER key. Following Exception occurred :: " + str(e))

    def enter(self):
        try:
            self.actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            self.cl.info("Pressed ENTER")
        except Exception as e:
            self.cl.info("Unable to press ENTER key. Following Exception occurred :: " + str(e))

    def close_new_window(self):
        try:
            self.actions.key_down(Keys.CONTROL).send_keys('W').perform()
            self.cl.info("Pressing CTRL + W to close the new window")
        except Exception as e:
            self.cl.info("Unable to perform Action :: CTRL + W. Following Exception occurred :: " + str(e))
            print_stack()

    def js_element_click(self, locator, element=None):
        element = None
        try:
            element = self.findElement(locator)
            self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            self.cl.info(
                "Unable to click on element :: " + str(element) + ". Following Exception occurred :: " + str(e))

    def js_select_list(self, locator, message):
        try:
            element = self.findElement(locator)
            self.driver.execute_script("arguments[0].removeAttribute('readonly','readonly');", element)
            element.send_keys(message)
            self.cl.info("Sending message :: " + str(message) + "locator :: " + str(locator["locatorValue"]))

        except Exception as e:
            self.cl.info("Exception Occurred. Following Exception :: " + str(e))
            print_stack()

    def stop_page_load(self):
        try:
            self.driver.execute_script("return window.stop")
            self.cl.info("Page load stop")
        except Exception as e:
            self.cl.info("Unable to stop the page load. Following Exception occurred :: " + str(e))

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

    def right_clickk(self, locator):
        element = None
        try:
            element = self.findElement(locator)
            self.actions.context_click(element).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

        except Exception as e:
            self.cl.info(
                "Unable to right click on element " + str(element) + ". Following Exception Occurred :: " + str(e))

    def driver_get(self, url):
        self.driver.get(url)
