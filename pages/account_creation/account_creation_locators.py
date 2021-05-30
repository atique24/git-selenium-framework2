from selenium.webdriver.common.by import By


# locators
account ={"locatorType":By.XPATH,"locatorValue":"//a/span[text()='Account']"}
register = {"locatorType":By.LINK_TEXT,"locatorValue":"Register"}
firstname = {"locatorType":By.ID,"locatorValue":"firstname"}
lastname = {"locatorType":By.ID,"locatorValue":"lastname"}
email_address = {"locatorType":By.ID,"locatorValue":"email_address"}
password_loc = {"locatorType":By.ID,"locatorValue":"password"}
confirmation = {"locatorType":By.ID,"locatorValue":"confirmation"}
checkbox = {"locatorType":By.ID,"locatorValue":"is_subscribed"}
register2 = {"locatorType":By.XPATH,"locatorValue":"//button[@title='Register']"}
success_message = {"locatorType":By.XPATH,"locatorValue":"//span[text()='Thank you for registering with Main Website Store.']"}
tv = {"locatorType":By.LINK_TEXT,"locatorValue":"TV"}
add_to_wishlist = {"locatorType":By.XPATH,"locatorValue":"//a[@title='LG LCD']//following-sibling::div/child::div/ul/li/a"}
share_wishlist = {"locatorType":By.XPATH,"locatorValue":"//span[text()='Share Wishlist']"}
emailaddress_wishlist = {"locatorType":By.ID,"locatorValue":"email_address"}
message_wishlist = {"locatorType":By.ID,"locatorValue":"message"}
message_success_sharelist = {"locatorType":By.XPATH,"locatorValue":"//span[text()='Your Wishlist has been shared.']"}

