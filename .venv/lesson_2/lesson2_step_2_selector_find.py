from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


browser = webdriver.Chrome()
time.sleep(1)
link = 'https://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text

    summa = str(int(num1)+int(num2))

    select = Select(browser.find_element(By.ID, 'dropdown'))
    time.sleep(1)
    select.select_by_value(summa)
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


