from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
time.sleep(2)

try:
    browser.get('http://suninjuly.github.io/find_xpath_form')
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys('Word')

    time.sleep(1)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()