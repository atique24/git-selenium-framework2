import pytest
from selenium.webdriver.common.by import By

from base.SeleniumBase import SeleniumBase
from tests.base_test import BaseTest


class TestPractisePage(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = SeleniumBase(self.driver)

    def test_one(self, oneTimeSetup):
        self.driver.visit("https://courses.letskodeit.com/practice")
        self.driver.elementClick(locator=(By.ID, "bmwradio"))
        self.driver.elementSend(locator=(By.ID, "name"), message="Atique")
        self.driver.selectByIndex(locator=(By.ID, "multiple-select-example"), value=1)
        self.driver.wait_and_switch_Iframe(locator=(By.ID, "courses-iframe"))
        self.driver.isElementDisplayed(locator=(By.LINK_TEXT, "HOME"))
        self.driver.exitIframe()
        self.driver.wait_and_switch_Iframe(index=0)
        self.driver.isElementDisplayed(locator=(By.LINK_TEXT, "HOME"))

