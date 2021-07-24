from base.base_page import BasePage
from utilities.util import Utilities
from utilities.customlogger import custom_logger
import logging
from utilities.util import Utilities
from pages.mobile_page.mobile_page_locators import *




class MobilePage(BasePage):
    cl = custom_logger(logging.INFO)

    def __init__(self,driver):
        super(MobilePage, self).__init__(driver)
        self.driver = driver
        self.utill = Utilities()


    def mobile_tab(self):
        self.elementClick(mobile)


    def sort_by_name(self):
        self.selectFromDropdown(locator=sort,selectByVisibleText=True,value="Name")

    def sort_by_price(self):
        self.selectFromDropdown(locator=sort,selectByVisibleText=True,value='Price')



    def sort_result_name(self):
        sort_result_list = [self.getText(Iphone),self.getText(samsung),self.getText(sony)]
        print(sort_result_list)
        return self.utill.listcompare(expectedList=expected_list1,actualList=sort_result_list)


    def sort_result_price(self):
        sort_result_list = [self.getText(sony),self.getText(samsung),self.getText(Iphone)]
        print(sort_result_list)
        return self.utill.listcompare(expectedList=expected_list2,actualList=sort_result_list)

    def add_to_cart(self):
        self.elementClick(add_to_cart)

    def enter_cart_quantity_and_update(self):
        self.elementSend(cart_quantity,'1000')
        #self.explicitwait(update,20,0.1)
        self.elementClick(update)
        return self.isElementDisplayed(error)


    def click_tv_tab(self):
        self.elementClick(tv)



    def click_list_view(self):
        self.elementClick(list_view)


    def sony_price_grid_view(self):
        value1 = self.getText(value)
        return value1

    def sony_price_list_view(self):
        value2 = self.getText(value)
        return value2


    def mobile_sort_by_name(self):
        self.mobile_tab()
        self.sort_by_name()
        return self.sort_result_name()

    def mobile_sort_by_price(self):
        self.mobile_tab()
        self.sort_by_price()
        return self.sort_result_price()

    def verify_price_different_view(self):
        self.click_list_view()
        value1 = self.sony_price_list_view()
        value2 = self.sony_price_grid_view()
        return self.utill.verify_value(value1,value2)

    def verify_max_cart_error(self):
        self.add_to_cart()
        return self.enter_cart_quantity_and_update()

    def click_compare_(self):
        self.elementClick(compare_xperia)
        self.elementClick(compare_apple)
        self.elementClick(compare_button)
        self.switching_to_window()
        result1 = self.isElementDisplayed(iphone_new)
        self.elementClick(close_window)
        return result1








