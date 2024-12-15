import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class TestAbs(unittest.TestCase):
    def set_up(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def fill_form(self, link):
        self.browser.get(link)
        f_name = self.browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        f_name.send_keys('John')
        l_name = self.browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        l_name.send_keys('Doe')
        email = self.browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('test@test.com')

    def test_1(self):
        self.set_up()
        link1 = "http://suninjuly.github.io/registration1.html"
        self.fill_form(link1)
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        wel_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        text = wel_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", text, 'Success test_1')

    def test_2(self):
        self.set_up()
        link2 = "http://suninjuly.github.io/registration2.html"
        self.fill_form(link2)
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        wel_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        text = wel_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", text, 'Success test_2')


if __name__ == "__main__":
    pytest.main()
