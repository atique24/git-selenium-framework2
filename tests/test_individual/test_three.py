import pytest

from pages.page_three.three_page import ThreePage
from tests.base_test import BaseTest
from assertpy import assert_that

class TestThree(BaseTest):

    @pytest.fixture(autouse=True)
    def pageObject(self):
        self.three = ThreePage(self.driver)


    def test_three(self):
        self.three.click_login_link()
        self.three.enter_msisdn()
        self.three.click_next_button()
        self.three.assertElementDisplayed(self.three.errorMessage)
        self.three.click_link_gender()
        self.three.assertTitleContains("Terms1")
