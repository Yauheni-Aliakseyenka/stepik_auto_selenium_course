from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
time.sleep(1)

try:
    browser.get(link)
    time.sleep(1)
    button = browser.find_element(By.ID, 'submit_button')
    button.click()
    time.sleep(2)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()


