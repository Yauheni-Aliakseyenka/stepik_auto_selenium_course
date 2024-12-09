import time
import os
import pyperclip
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def copy_code(br):
    alert = br.switch_to.alert
    alert_text = alert.text
    code = alert_text.split(': ')[-1]
    pyperclip.copy(code)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    alert_1 = browser.switch_to.alert
    alert_1.accept()

    number = browser.find_element(By.ID, 'input_value').text
    value = calc(number)

    input_req = browser.find_element(By.ID, 'answer')
    input_req.send_keys(value)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    copy_code(browser)

finally:
    browser.quit()






