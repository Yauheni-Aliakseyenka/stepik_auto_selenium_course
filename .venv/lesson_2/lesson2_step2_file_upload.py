import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    fields = browser.find_elements(By.CLASS_NAME, 'form-control')
    for field in fields:
        field.send_keys('Text')

    upload_button = browser.find_element(By.CSS_SELECTOR, '[type="file"]')

    current_path = os.path.abspath(os.path.dirname(__file__))
    file_name = 'dataset_3380_5.txt'
    file_path = os.path.join(current_path, file_name)

    upload_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


