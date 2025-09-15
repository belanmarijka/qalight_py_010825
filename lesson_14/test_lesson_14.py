# expect conditions
# EXplicit for EXpected
# IMplicit for IMaginary

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_14.processing_elements import webelement, fill_input

# Ініціалізація веб-драйвера для Chrome
def test_example_implicitly_wait():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10) # seconds
    driver.get("https://www.example.com")
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert heading.text == "Example Domain"
    driver.close()


def test_example_with_explicit_wait():
    driver = webdriver.Firefox()
    driver.get("https://www.example.com")
    heading = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"
    driver.close()


def test_example_with_use_webelement(driver):
    # driver = webdriver.Firefox()
    # driver.get("https://www.example.com")
    heading = webelement(driver, '//h1')
    assert heading.text == "Example Domain"
    # driver.close()

# presence_of_element_located 
# visibility_of_element_located
# element_to_be_clickable
# text_to_be_present_in_element
