import datetime
import logging
import os
import time

from assertpy import assert_that
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utilities.customlogger import custom_logger
from traceback import print_stack
from utilities.util import Utilities


class SeleniumBase:
    enableScreenshot = False
    env = None
    cl = custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.util = Utilities()

    @classmethod
    def EnableScreenshotForTest(cls, screenshot):
        cls.enableScreenshot = screenshot

    @classmethod
    def setEnv(cls, env):
        if env.lower() == "sit":
            cls.env = "http://sit-"

        elif env.lower() == "staging":
            cls.env = "http://staging-"

        elif env.lower() == "preprod":
            cls.env = "http://preprod-"

        else:
            cls.env = "http://sit-"

    def visit(self, url):
        try:
            #url = self.env + url
            self.driver.get(url)
            element = self.driver.find_elements(By.TAG_NAME, 'title')
            if len(element) == 0:
                i = 0
                while i < 5:
                    if len(element) == 0:
                        i += 1
                        #time.sleep(2)
                        self.cl.info("Website is not loaded. Reloading the website for :: " + str(i) + 'st time')
                        self.driver.get(url)
                        element = self.driver.find_elements(By.TAG_NAME, 'title')
                    else:
                        self.cl.info("Website is loaded.")
                        break
            else:
                self.cl.info("Website is loaded.")
        except Exception as e:
            self.cl.error("Unable to open URL from :: " + str(url) + '. ' + "Exception Occurred :: " + str(
                e.__class__.__name__))
            raise e

    def findElement(self, locator, timeout=20, poll_frequency=0.2):
        element = None
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            # self.cl.info(
            #     "Waiting for " + str(timeout) + " seconds to find the element for locator :: " + str(
            #         locator))
            element = wait.until(ec.presence_of_element_located(locator))
            self.cl.info(
                "Element :: " + str(element.id) + " found for locator :: " + str(locator))

            # element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            #self.driver.execute_script("arguments[0].style.border='3px solid red'", element)


        except Exception as e:
            self.cl.error("No Element found for locator :: " + str(locator) + '. ' + "Exception Occurred :: " + str(
                e.__class__.__name__))
            print_stack(limit=5)
            raise e
        return element

    def findElements(self, locator):
        elements = []
        try:
            elements = self.driver.find_elements(*locator)
            if len(element) > 0:
                self.cl.info("Elements list returned::  " + str(elements) + " for locator :: " + str(locator))

            else:
                self.cl.info(
                    "Elements not found for locator :: " + str(locator) + ". Empty List returned " + str(elements))

        except Exception as e:
            self.cl.error(
                "Element could not be found for :: " + str(locator) + '. ' + str(
                    e.__class__.__name__) + ' ' + str(e))
            print_stack(limit=5)
            raise NoSuchElementException
        return elements

    def selectByIndex(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                sel = Select(element)
                sel.select_by_index(value)
                self.cl.info("Selected element with index " + str(value) + " from the drop down using Index position")
            else:
                self.cl.error("Unable to select element by Index. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to select element by Index. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def selectByVisibleText(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)

            if element:
                sel = Select(element)
                sel.select_by_visible_text(value)
                self.cl.info("Selected element with value " + str(value) + " from the drop down using Visible Text")

            else:
                self.cl.error(
                    "Unable to select element by Visible Text. No element was4 found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Unable to select element by Visible Text. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def selectByValue(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)

            if element:
                sel = Select(element)
                sel.select_by_value(value)
                self.cl.info("Selected element with Name " + str(value) + " from the drop down using Value")


            else:
                self.cl.error(
                    "Unable to select element by Visible Text. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to select element from the dropdown. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def visibilityOfElementLocated(self, locator, timeout=15, poll_frequency=0.2):
        element = None
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            self.cl.info(
                "Waiting for " + str(timeout) + " seconds for checking the element visibility :: " + str(
                    locator))
            element = wait.until(ec.visibility_of_element_located(locator))

            self.cl.info(
                "Element :: " + str(element.id) + " is visible on page for locator :: " + str(
                    locator) + ". Session_id :: " + str(
                    element.parent.session_id))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)


        except Exception as e:
            self.cl.error("Unable to find element with locator :: " + str(locator) + '. Exception occurred ' + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

        return element

    def elementClick(self, locator, element=None, force=None):
        try:
            if locator:
                element = self.findElement(locator)
                # wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.2)
                # element = wait.until(ec.element_to_be_clickable(locator))

            if element:
                if self.enableScreenshot:
                    if element.get_attribute(name="type") == "submit":
                    #if self.getAttribute(locator=None, element=element, attributeType="type") == "submit":
                        self.saveScreenshots()
                if force:
                    self.driver.execute_script("arguments[0].click();", element)
                    self.cl.info("Force clicked on Element :: " + str(element.id))
                else:
                    element.click()
                    self.cl.info("Clicked on Element : " + str(element.id))
            else:
                self.cl.error("Unable to click on locator. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to click the element :: " + str(locator) + ". Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def elementSend(self, locator, message, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                element.send_keys(message)
                self.cl.info("Text :: " + str(message) + " entered on element :: " + str(element.id))
            else:
                self.cl.error(
                    "Unable to send the message on the element. No Element found for the locator ::  " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to send the message on locator: " + str(locator) + "Exception :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def verifyExactTitle(self, expectedTitle, timeout=10, poll_frequency=0.2):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            result = wait.until(ec.title_is(expectedTitle))
            if result:
                self.cl.info("The actual title of the webpage is :: " + str(self.driver.title))
                self.cl.info("The expected title is :: " + str(expectedTitle))
                self.cl.info("Title Match")
            else:
                self.cl.info("Title doesnt match")

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current page title. Exception occurred :: " + str(
                    e.__class__.__name__) + str(e))
            result = False
            print_stack(limit=5)
            raise e
        return result

    def verifyTitleContains(self, title, timeout=15, poll_frequency=0.2):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            result = wait.until(ec.title_contains(title))
            if result:
                self.cl.info("'" + title + "'" + " is part of the page title :: " + str(self.driver.title))
            else:
                self.cl.info("Title of the page doesnt contain text :: " + title)

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current page title. Exception occurred :: " + str(
                    e.__class__.__name__) + str(e))
            result = False
            print_stack(limit=5)
            raise e
        return result

    def getElementText(self, locator, element=None):
        element_text = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                element_text = element.text.strip()
                element_text
                self.cl.info("Text of the element : " + str(element.id) + " is " + ' "' + element_text + '"')
                if self.enableScreenshot:
                    self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to find the text for element. No Element found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to find the text for element : " + str(
                    locator) + ". Following Exception occurred :: " + str(
                    e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

        return element_text

    def getElementsText(self, locator, elements=None):
        elementText = []
        try:
            if locator:
                elements = self.findElements(locator)
            if len(elements) > 0:
                elementText = [item.text for item in elements]
                self.cl.info("The TEXT for Elements are :: " + str(elementText))

            else:
                self.cl.error(
                    "Unable to find text for the element list. No elements found for the locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to return text for elements. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e
        return elementText

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
            print_stack(limit=5)
            raise e
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
    #         #print_stack(limit=5)
    #     return element_attribute


    # def pressSpaceKey(self, locator, element=None):
    #
    #     # self.actions.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    #     # self.actions.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    #
    #     try:
    #         if locator:
    #             element = self.findElement(locator)
    #         if element:
    #             element.send_keys(Keys.SPACE)
    #             self.cl.info("Clicked on element :: "+ str(element.id))
    #         else:
    #             self.cl.error("Unable to click on locator. No element was found for locator :: " + str(locator))
    #
    #     except Exception as e:
    #         self.cl.error("Unable to click the element :: " + str(locator) + ". Exception occurred :: " + str(
    #         e.__class__.__name__) + str(e))
    #         print_stack(limit=5)
    #         raise e

    def getValueOfCssProperty(self, locator, attributeType, element=None):
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
            print_stack(limit=5)
            raise e
        return cssAttributeProperty

    def waitToClickElement(self, locator, time=15, poll=0.2):
        element = None
        try:
            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[ElementNotInteractableException, ElementNotVisibleException,
                                                     NoSuchElementException, TimeoutException,
                                                     StaleElementReferenceException, ElementClickInterceptedException])
            self.cl.info(
                "Waiting to click on element :: " + str(locator) + " for time " + str(time) + " sec")
            element = wait.until(ec.element_to_be_clickable(locator))
            self.cl.info("Element :: " + str(element.id) + " is Available for action for locator :: " + str(locator))
            if self.enableScreenshot:
                if element.get_attribute(name="type") == "submit":
                    self.saveScreenshots()
            element.click()
            self.cl.info("Clicked on element :: " + str(element.id))

        except Exception as e:
            self.cl.error("Unable to find the element " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e
        return element

    def moveToElementAndClick(self, locator):
        try:
            element = self.findElement(locator)
            self.actions.move_to_element(element).click().perform()

        except Exception as e:
            self.cl.error("Unable to move to element and click the element " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def wait_and_switch_Iframe(self, locator=None, index=None, time=20, poll=0.2):
        try:
            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchFrameException, NoSuchElementException, TimeoutException])

            if (not locator and not index) or (locator and index):
                raise ValueError(" locator or index position is required")

            if self.enableScreenshot:
                self.saveScreenshots()

            if isinstance(locator, tuple):
                self.cl.info("Waiting to find iframe with :: " + str(locator) + " for time " + str(
                    time) + "sec")
                wait.until(ec.frame_to_be_available_and_switch_to_it(locator))
                self.cl.info("Switched to Iframe with locator :: " + str(locator))

            elif isinstance(index, int) and locator == None:
                self.cl.info("Waiting to find iframe with index position :: " + str(index) + " for time " + str(
                    time) + "sec")
                wait.until(
                    ec.frame_to_be_available_and_switch_to_it(self.driver.find_elements(By.TAG_NAME, "iframe")[index]))
                self.cl.info("Switched to Iframe with index position :: " + str(index))

            elif not locator and not index:
                raise ValueError("locator or index position is required")

            # self.cl.info("Waiting to find iframe with : " + str(locator) + "with index position:: " + str(
            #     index) + "for time " + str(
            #     time) + "sec")
            # wait.until(
            #     ec.frame_to_be_available_and_switch_to_it(locator))
            # self.cl.info("Switched to Iframe")


        except Exception as e:
            self.cl.error("Unable to find the iframe. Following Exception occurred " + '. ' + str(
                e.__class__.__name__) + str(e))
            print_stack()
            raise e

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
            print_stack(limit=5)
            raise e

    def full_screenshot_with_scroll(self, driver, save_path):
        from io import BytesIO
        from PIL import Image

        # initiate value

        save_path = save_path
        img_li = []  # to store image fragment
        offset = 0  # where to start

        # js to get height
        height = self.driver.execute_script(
            "return Math.max(" "document.documentElement.clientHeight, window.innerHeight);")

        # js to get the maximum scroll height
        # Ref--> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
        max_window_height = self.driver.execute_script(
            "return Math.max("
            "document.body.scrollHeight, "
            "document.body.offsetHeight, "
            "document.documentElement.clientHeight, "
            "document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight);"
        )

        # looping from top to bottom, append to img list
        # Ref--> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
        while offset < max_window_height:
            # Scroll to height
            driver.execute_script(f"window.scrollTo(0, {offset});")
            img = Image.open(BytesIO((self.driver.get_screenshot_as_png())))
            img_li.append(img)
            offset += height

        # In case it is not a perfect fit, the last image contains extra at the top.
        # Crop the screenshot at the top of last image.
        extra_height = offset - max_window_height
        if extra_height > 0 and len(img_li) > 1:
            pixel_ratio = driver.execute_script("return window.devicePixelRatio;")
            extra_height *= pixel_ratio
            last_image = img_li[-1]
            width, height = last_image.size
            box = (0, extra_height, width, height)
            img_li[-1] = last_image.crop(box)

        # Stitch image into one
        # Set up the full screen frame
        img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
        img_frame = Image.new("RGB", (img_li[0].size[0], img_frame_height))
        offset = 0
        for img_frag in img_li:
            img_frame.paste(img_frag, (0, offset))
            offset += img_frag.size[1]
        img_frame.save(save_path)

    def saveScreenshots(self):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]  # fetch the current TestName
        new_name = test_name.split("::")
        filename = new_name[-1] + "_" + self.util.generate_date_time() + ".png"
        screenshotDirectory = "..//logs//screenshots//" + str(datetime.date.today()) + "//" + new_name[-1] + "//"
        relativeFilename = screenshotDirectory + filename

        currentDirectory = os.path.dirname(__file__)
        destinationPath = os.path.join(currentDirectory, relativeFilename)

        destinationFolder = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            # self.driver.save_screenshot(destinationPath)
            self.full_screenshot_with_scroll(self.driver, destinationPath)
            self.cl.info("### Screenshot saved at path: " + destinationPath)
        except Exception as e:
            self.cl.error("### Exception Occurred " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

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
            print_stack(limit=5)
            raise e
        return innerText

    def isElementDisplayed(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                if self.enableScreenshot:
                    self.saveScreenshots()

            if element:
                result = element.is_displayed()
                if result:
                    if self.enableScreenshot:
                        self.saveScreenshots()
                    self.cl.info("Element is displayed for locator :: " + str(locator))

                else:
                    self.cl.error("Element is not displayed for locator :: " + str(locator))
            else:
                self.cl.error("Element is not displayed. Unable to find element with locator :: " + str(locator))
                result = False

        except Exception as e:
            self.cl.error(
                "Element is not displayed with locator :: " + str(locator) + " Exception occurred :: " + str(e))
            print_stack(limit=5)
            result = False
            raise e
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
            print_stack(limit=5)
            raise e

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
            print_stack(limit=5)
            raise e

    def switchFrame(self, value):
        try:
            self.driver.switch_to.frame(value)
            self.cl.info("Switched to Iframe :: " + str(value))

        except Exception as e:
            self.cl.error("Error while switching to Iframe" + ". Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def switchParentIframe(self):
        try:
            self.driver.switch_to.parent_frame()
            self.cl.info("Switch to Parent iFrame")
        except Exception as e:
            self.cl.error("Unable to switch  to Parent Frame. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def exitIframe(self):
        try:
            self.driver.switch_to.default_content()
            self.cl.info("Switched to default content. Iframe closed")

        except Exception as e:
            self.cl.error("Error while switching to Default Content. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

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
            print_stack(limit=5)
            raise e

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
            print_stack(limit=5)
            raise e

    def browserRefresh(self):
        try:
            self.driver.refresh()
            self.cl.info("Refreshing the current window")
        except Exception as e:
            self.cl.error("Unable to refresh the browser. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

    def currentBrowserWindow(self):
        current_window = None
        try:
            current_window = self.driver.current_window_handle
            self.cl.info("The current window is :: " + str(current_window))

        except Exception as e:
            self.cl.error('Unable to get the current window. Exception Occurred :: ' + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

        return current_window

    def allBrowserWindow(self):
        all_window = None
        try:
            all_window = self.driver.window_handles
            self.cl.info("All available Window's are :: " + str(all_window))

        except Exception as e:
            self.cl.info('Unable to get all the windows. Exception Occurred :: ' + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e
        return all_window

    def switchWindow(self, windowNumber: int):
        try:
            allWindow = self.allBrowserWindow()
            self.driver.switch_to.window(allWindow[windowNumber])
            self.cl.info("Switched to new window :: " + str(allWindow[windowNumber]))
        except Exception as e:
            self.cl.info("Unable to switch to new window. Following Exception occurred :: " + str(
                e.__class__.__name__) + " " + str(e))
            print_stack(limit=5)
            raise e

    def browserBack(self):
        self.driver.back()

    def browserForward(self):
        self.driver.forward()

    def pressSpaceBar(self):
        try:
            self.actions.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            # self.actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        except Exception as e:
            self.cl.info("Unable to press SpaceBar key. Following Exception occurred :: " + str(e))

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
    #         #print_stack(limit=5)

    def jsClick(self, locator, element=None):
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
            print_stack(limit=5)
            raise e

    def js_select_list(self, locator, message):
        try:
            element = self.findElement(locator)
            self.driver.execute_script("arguments[0].removeAttribute('readonly','readonly');", element)
            element.send_keys(message)
            self.cl.info("Sending message :: " + str(message) + "locator :: " + str(locator["locatorValue"]))

        except Exception as e:
            self.cl.error("Exception Occurred. Following Exception :: " + str(e))
            print_stack(limit=5)

    def stopPageLoading(self):
        try:
            self.driver.execute_script("return window.stop")
            self.cl.info("Page load stop")
        except Exception as e:
            self.cl.error("Unable to stop the page load. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            print_stack(limit=5)
            raise e

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
            print_stack(limit=5)
            raise e

    def getCurrentUrl(self):
        currentUrl = None
        try:
            currentUrl = self.driver.current_url
            print("Current Page URL is :: " + str(currentUrl))

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current URL. Following Exception Occurred :: " + str(
                    e.__class__.__name__) + " " + str(e))
            print_stack(limit=5)
            raise e
        return currentUrl

    def assertTitle(self, expectedTitle):
        actualTile = self.getTitle()
        assert_that(actualTile).is_equal_to(expectedTitle)

    def assertTitleContains(self, titleSubString):
        result = None
        try:
            result = WebDriverWait(self.driver, 15, 0.2).until(ec.title_contains(titleSubString))
            self.cl.info("The title of page is :: " + str(self.getTitle()))
            self.cl.info("Title of the Page contains text :: " + str(titleSubString))

        except Exception as e:
            self.cl.error("Title of the Page does not contains text :: " + str(
                titleSubString) + ". Following Exception occurred :: " + str(
                e.__class__.__name__) + " " + str(e))
        finally:
            assert_that(result).is_true()

    def assertElementDisplayed(self, locator, element=None):
        assert_that(self.isElementDisplayed(locator, element)).is_true()

    def assertText(self, locator, expectedText, element=None):
        text = self.getElementText(locator, element)
        assert_that(text).is_equal_to(expectedText)

    def assertTextContains(self, textSubString, locator, element=None):
        text = self.getElementText(locator, element)
        assert_that(text).contains_ignoring_case(textSubString)

    def getPageSource(self):
        return self.driver.page_source
