from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


max_retries = 3
all_exceptions = (TimeoutException, StaleElementReferenceException)


# Initialize selenium driver
def initialize_driver():
    """
    Initializes a headless Firefox driver for Selenium.

    Returns:
    - WebDriver: The initialized Selenium WebDriver.
    """
    options = Options()
    options.add_argument("-headless")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", "./pdfs")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

    driver = webdriver.Firefox(options=options)

    print("Firefox initialized in headless mode")
    return driver


# Get element with specific selector
def get_element(driver, by, value):
    """
    Retrieves an element identified by the specified method and value.

    Parameters:
    - driver (WebDriver): The Selenium WebDriver.
    - by (By): The method to locate the element (e.g., By.ID, By.XPATH, etc.).
    - value (str): The value used by the locator.

    Returns:
    - WebElement: The located WebElement.
    """
    for _ in range(max_retries):
        try:
            return WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((by, value))
            )

        except all_exceptions:
            print("Retrying")


# Get list of elements with specific selector
def get_list(driver, by, value):
    """
    Retrieves a list of elements identified by the specified method and value.

    Parameters:
    - driver (WebDriver): The Selenium WebDriver.
    - by (By): The method to locate the elements (e.g., By.ID, By.XPATH, etc.).
    - value (str): The value used by the locator.

    Returns:
    - List[WebElement]: The list of located WebElements.
    """
    for _ in range(max_retries):
        try:
            return WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((by, value))
            )
        except all_exceptions as e:
            print(f"Exception - {e} retrying")


# Click element with XPATH
def click_element_xpath(driver, value):
    """
    Clicks an element identified by XPath.

    Parameters:
    - driver (WebDriver): The Selenium WebDriver.
    - value (str): The XPath value to locate and click the element.
    """
    click_element(driver, By.XPATH, value)


# Get element with XPATH
def get_element_xpath(driver, value):
    """
    Retrieves an element identified by XPath.

    Parameters:
    - driver (WebDriver): The Selenium WebDriver.
    - value (str): The XPath value to locate the element.

    Returns:
    - WebElement: The located WebElement.
    """
    return get_element(driver, By.XPATH, value)
