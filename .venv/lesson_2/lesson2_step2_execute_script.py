from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(1)
link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser.get(link)
    number = browser.find_element(By.ID, 'input_value').text
    value = calc(number)

    input_req = browser.find_element(By.ID, 'answer')
    input_req.send_keys(value)

    browser.execute_script("window.scrollBy(0, 100);")

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