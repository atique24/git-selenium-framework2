# Selenium Python Framework 

Selenium Python Framework based on Pytest and POM Design pattern.

✅ Supports Chrome, Firefox, Edge.
✅ Supports automatic screenshots, logs, Allure Report with failed screenshots.
✅ Automatic Driver Downloads based on the browser Version.
✅ Supports Parallel testing using pytest-xdist.
✅ Supports third party Testing Cloud providers like BrowserStack


# Installation
You can clone https://github.com/atique24/git-selenium-framework2.git.
Set ur application url to the baseUrl variable in datafiles//config.py. 
Provide the locators in tuple. For Eg (By.ID, "Some ID").
Create your page class and inherit the SeleniumBase class. 

Here are some common SeleniumBase methods that you might find in tests:
findElement(self, locator, timeout=10, poll_frequency=0.2)
findElements(self, locator)
selectByIndex(self, locator, value, element=None)
selectByVisibleText(self, locator, value, element=None)
selectByValue(self, locator, value, element=None)
elementClick(self, locator, element=None)
elementSend(self, locator, message, element=None)
getTitle(self)
getText(self, locator, element=None)
getTextElementList(self, locator, elements=None)
getAttribute(self, locator, attributeType, element=None)
waitToClickElement(self, locator, time=2, poll=0.2)
waitForIframe(self, locator, index, time=10, poll=0.5)
getInnerText(self, locator, element=None)
isElementDisplayed(self, locator, element=None)
switchFrame(self, value)
slider(self, locator, XCORD, YCORD, element=None)
doubleClick(self, locator, element=None)
rightClick(self, locator, element=None)

🔵 Here are more examples that you can run:
pytest tests\ --headless   # To run the browser in headless mode. By Default the browser will run in Headed mode.
pytest tests\ --screenshot # To enable screenshot capture. By Default it is set to Off. Screenshots will be captured only in case of failure and attached in the allure report.
pytest tests\ --browser Firefox # To launch Firefox browser. If --browser not specified, then Chrome browser is launched by default. For Edge use --browser Edge
pytest tests\ -n Auto --dist loadfile # This will create multiple browser sessions based on the cpu core. For Parallel testing.
pytest tests\ --html=TestReport\report.html # Simple html report.
pytest tests\ tests\  --alluredir=TestReport\  #Create files for Allure report. Then do allure serve alluredir\TestReport. Allure bat files needs to be download and stored in the path. Logs and Screenshot for failed tests will be attached to the allure report. 

🔵 Here are some useful command-line options that come with pytest:
-v  # Verbose mode. Prints the full name of each test run.
-q  # Quiet mode. Print fewer details in the console output when running tests.
-x  # Stop running the tests after the first failure is reached
--html=report.html  # Creates a detailed pytest-html report after tests finish.
--collect-only (Test Collection)
-n=NUM  # Multithread the tests using that many threads. (Parallel Testing)
-s  # See print statements. (Should be on by default with pytest.ini present.)
--junit-xml=report.xml  # Creates a junit-xml report after tests finish.
--pdb  # not supported
-m=MARKER  # Run tests with the tags


🔵 Logs and screenshots will get saved to the below paths :
screenshots/ today's date /
logs/ today's date / Automation.log

🔵 Supports DDT using JSON or CSV. Just put the file data file in //datafiles// folder. You can use @ddt from unitTest or @pytest.parameterize from pytest for Data Driven Testing. Please see the example Test.

🔵 Supports TestSuite creating using UnitTest Framework. Please see the examples in the Tests folder.

🔵 Supports Class Level SetUp and TearDown. Fresh browser session will be created for each TestClass.

🔵 Can use python default Assert or assertPy for Assertions.

