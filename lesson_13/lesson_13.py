# selenium, decoratorl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Firefox()

# Відкриття веб-
url="http://localhost"
driver.get(url)

# user_field = driver.find_element(By.ID, "username")
# pass_field = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login_button")

user_field = driver.find_element(By.XPATH, '//*[@id="username"]')
user_field.send_keys("example_username")

pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_field.send_keys("example_pass")

# login_button = driver.find_element(By.XPATH, '//*[@id="login_button"]')
# login_button.click()

li_elements = driver.find_elements(By.TAG_NAME, "li")
for li in li_elements:
    print(li.text)
paragaph_xpath = '//div[@class="example_div"]/p'
par = driver.find_element(By.XPATH, paragaph_xpath)
print(par.text)
#
gender_radio = driver.find_element(By.ID, "male")
gender_radio.click()
sleep(1)
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()
sleep(1)
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("США")
# Робота з веб-елементами і виконання дій на сторінці
sleep(5)
# Закриття браузера
driver.quit()