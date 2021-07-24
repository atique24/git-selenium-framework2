from selenium.webdriver.common.by import By

mobile = {"locatorType":By.LINK_TEXT,"locatorValue":"MOBILE"}
sort = {"locatorType":By.XPATH,"locatorValue":"//select[@title='Sort By']"}
Iphone = {"locatorType":By.LINK_TEXT,"locatorValue":"IPHONE"}
samsung = {"locatorType":By.LINK_TEXT,"locatorValue":"SAMSUNG GALAXY"}
sony = {"locatorType":By.LINK_TEXT,"locatorValue":"SONY XPERIA"}
expected_list1 = ['IPHONE', 'SAMSUNG GALAXY', 'SONY XPERIA']
expected_list2 = ['SONY XPERIA', 'SAMSUNG GALAXY', 'IPHONE']
tv = {"locatorType":By.LINK_TEXT,"locatorValue":"TV"}
grid_view = {"locatorType":By.XPATH,"locatorValue":"//strong[@title='Grid']"}
list_view = {"locatorType":By.LINK_TEXT,"locatorValue":"List"}
value = {"locatorType":By.XPATH,"locatorValue":"//span[@id='product-price-1']/child::span"}
add_to_cart = {"locatorType":By.XPATH,"locatorValue":"//a[@title='Xperia']//following-sibling::div//span[text()='Add to Cart']"}
cart_quantity = {"locatorType":By.XPATH,"locatorValue":"//input[@data-cart-item-id='MOB001' and @title='Qty']"}
update = {"locatorType":By.XPATH,"locatorValue":"//button[@title='Update']/span/span"}
error = {"locatorType":By.XPATH,"locatorValue":"//span[text()='Some of the products cannot be ordered in requested quantity.']"}
compare_xperia = {"locatorType":By.XPATH,"locatorValue":"//a[@title='Xperia']//following-sibling::div/child::div/child::div/child::ul/li/a[text()='Add to Compare']"}
compare_button = {"locatorType":By.XPATH,"locatorValue":"//span[text()='Compare']"}
iphone_new = {"locatorType":By.XPATH,"locatorValue":"//a[text()='IPhone']"}
close_window = {"locatorType":By.XPATH,"locatorValue":"//span[text()='Close Window']"}