from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def webelement(driver, xpath:str, timeout:float = 10):
    """Find, wait and return webelement if presence of page    
    """
    try:
        element = WebDriverWait(driver, timeout=timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
            )
    except TimeoutException:
        element = None
        raise NoSuchElementException(f"Element for locator {xpath} not presence on page for {timeout} sec ")
    return element


def fill_input(driver, xpath:str, text:str):
    """Fill text to input field on page
    """
    input_field = webelement(driver, xpath)
    input_field.clear()
    input_field.send_keys(text)
