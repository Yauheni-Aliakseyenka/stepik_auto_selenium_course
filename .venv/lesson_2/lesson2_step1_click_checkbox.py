from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
time.sleep(1)
link = 'https://suninjuly.github.io/math.html'

try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    value = calc(x_element.text)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(value)
    time.sleep(1)

    check1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    check1.click()
    check2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    check2.click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

