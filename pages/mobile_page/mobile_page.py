from base.base_page import BasePage
from utilities.util import Utilities
from utilities.customlogger import custom_logger
import logging
from utilities.util import Utilities




class MobilePage(BasePage):
    cl = custom_logger(logging.INFO)

    def __init__(self,driver):
        super(MobilePage, self).__init__(driver)
        self.driver = driver
        self.utill = Utilities()


    #locator
    _mobile = "MOBILE"
    _sort = "//select[@title='Sort By']"
    _Iphone = "IPHONE"
    _samsung = "SAMSUNG GALAXY"
    _sony = "SONY XPERIA"
    _expected_list1 = ['IPHONE', 'SAMSUNG GALAXY', 'SONY XPERIA']
    _expected_list2 = ['SONY XPERIA', 'SAMSUNG GALAXY', 'IPHONE']
    _tv = "TV"
    _grid_view = "//strong[@title='Grid']"
    _list_view = "List"
    _value = "//span[@id='product-price-1']/child::span"
    _add_to_cart = "//a[@title='Xperia']//following-sibling::div//span[text()='Add to Cart']"
    _cart_quantity = "//input[@data-cart-item-id='MOB001' and @title='Qty']"
    _update = "//button[@title='Update']/span/span"
    _error = "//span[text()='Some of the products cannot be ordered in requested quantity.']"
    _compare_xperia = "//a[@title='Xperia']//following-sibling::div/child::div/child::div/child::ul/li/a[text()='Add to Compare']"
    _compare_apple = "//a[@title='IPhone']//following-sibling::div/child::div/child::div/child::ul/li/a[text()='Add to Compare']"
    _compare_button = "//span[text()='Compare']"
    _iphone_new = "//a[text()='IPhone']"
    _close_window = "//span[text()='Close Window']"


    def mobile_tab(self):
        self.elementClick(self._mobile,"link")


    def sort_by_name(self):
        self.get_element_dropdown_value(locator=self._sort,locatorType="xpath",selectType='text',value="Name")

    def sort_by_price(self):
        self.get_element_dropdown_value(locator=self._sort,locatorType='xpath',selectType='text',value='Price')



    def sort_result_name(self):
        sort_result_list = [self.getText(self._Iphone,"link"),self.getText(self._samsung,"link"),self.getText(self._sony,"link")]
        print(sort_result_list)
        return self.utill.listcompare(expectedList=self._expected_list1,actualList=sort_result_list)

    def sort_result_price(self):
        sort_result_list = [self.getText(self._sony,"link"),self.getText(self._samsung,"link"),self.getText(self._Iphone,"link")]
        print(sort_result_list)
        return self.utill.listcompare(expectedList=self._expected_list2,actualList=sort_result_list)

    def add_to_cart(self):
        self.elementClick(self._add_to_cart,'xpath')

    def enter_cart_quantity_and_update(self):
        self.elementSend(self._cart_quantity,'xpath','1000')
        self.explicitwait(self._update,'xpath',20,0.1)
        self.elementClick(self._update,'xpath')
        return self.isElementDisplayed(self._error,'xpath')


    def click_tv_tab(self):
        self.elementClick(self._tv,'link')
        print('clicked on Tv')


    def click_list_view(self):
        self.elementClick(self._list_view,'link')


    def sony_price_grid_view(self):
        value1 = self.getText(self._value,'xpath')
        return value1

    def sony_price_list_view(self):
        value2 = self.getText(self._value,'xpath')
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
        return self.utill.verify_values(self.sony_price_list_view(),self.sony_price_grid_view())

    def verify_max_cart_error(self):
        self.add_to_cart()
        return self.enter_cart_quantity_and_update()

    def click_compare_(self):
        self.elementClick(self._compare_xperia,'xpath')
        self.elementClick(self._compare_apple,'xpath')
        self.elementClick(self._compare_button,'xpath')
        self.switching_to_window()
        result1 = self.isElementDisplayed(self._iphone_new,'xpath')
        self.elementClick(self._close_window,'xpath')
        return result1








