import time
import pyperclip
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'),'100'))
    browser.find_element(By.ID, 'book').click()
    number = browser.find_element(By.ID, 'input_value').text
    value = calc(number)

    input_req = browser.find_element(By.ID, 'answer')
    input_req.send_keys(value)

    browser.find_element(By.ID, "solve").click()

    copy_code(browser)

finally:
    browser.quit()



