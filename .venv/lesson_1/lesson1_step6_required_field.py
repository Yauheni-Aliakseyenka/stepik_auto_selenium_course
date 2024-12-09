from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
time.sleep(1)

try:
    browser.get(link)
    time.sleep(1)
    f_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    f_name.send_keys('John')
    l_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    l_name.send_keys('Doe')
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email.send_keys('test@test.com')

    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    wel_text_elt = browser.find_element(By.TAG_NAME, "h1")
    wel_text = wel_text_elt.text #вытаскиваем текст из элемента

    assert "Congratulations! You have successfully registered!" == wel_text

finally:
    time.sleep(10)
    browser.quit()



