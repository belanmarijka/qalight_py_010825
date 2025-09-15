
class CustomCondition:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)  # Знаходимо елемент
            return element.is_displayed()  # Перевіряємо, чи елемент відображається
        except:
            return False  # Якщо елемент не знайдено або

# element = WebDriverWait(driver, 10).until(CustomCondition((By.CSS_SELECTOR, "div.some-class")))