from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
time.sleep(2)
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(2)
button = browser.find_element(By.ID, "submit_button")
