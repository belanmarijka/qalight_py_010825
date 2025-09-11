from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Firefox()

# Відкриття веб-
url="http://localhost/scroll_frame.html"
driver.get(url)
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)  # Зачекайте трохи після прокрутки вниз

# Прокрутка вгору
driver.execute_script("window.scrollTo(0, 0);")
sleep(1)  # Зачекайте трохи після прокрутки вгору
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(0, last_height, 500):
    driver.execute_script(f"window.scrollTo(0, {i});")
    sleep(0.5)
driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))

button = driver.find_element(By.ID, "myButton")
button.click()
sleep(1)
button.click()





sleep(5)
# Закриття браузера
driver.quit()