from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

browser = webdriver.Chrome()
time.sleep(2)
fake = Faker()
word = fake.word()

try:
    browser.get('http://suninjuly.github.io/huge_form.html')
    time.sleep(2)
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys(word)

    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

