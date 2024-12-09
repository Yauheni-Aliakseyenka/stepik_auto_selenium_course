from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
time.sleep(1)
link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(link)
    treasure = browser.find_element(By.ID, 'treasure')
    value = calc(treasure.get_attribute('valuex'))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(value)
    time.sleep(1)

    check1 = browser.find_element(By.ID, 'robotCheckbox')
    check1.click()
    check2 = browser.find_element(By.ID, 'robotsRule')
    check2.click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

