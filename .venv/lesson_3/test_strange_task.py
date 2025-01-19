import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

answer = math.log(int(time.time()))
link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_open_link(browser: webdriver.Chrome):
    browser.get(link)
    WebDriverWait(browser, timeout=15).until(ec.visibility_of_element_located((By.ID, 'ember471')))
    browser.find_element(By.ID, "ember471").click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "btn-google").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[name = 'identifier']").send_keys('alekseenka.evv@gmail.com')
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'AjY5Oe').click()
    time.sleep(4)









