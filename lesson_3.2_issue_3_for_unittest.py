from selenium import webdriver
import unittest
import time
from time import sleep


class TestAbs(unittest.TestCase):
    def test_no_bug(self):  # тест без бага. Все то же самое что в уроке 1.6, только без try и finally
        browser = webdriver.Chrome()
        browser.get(link1)
        browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element_by_class_name("form-control.third").send_keys("ivanov@gmail.com")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(10)
        browser.quit()

    def test_with_bug(self):  # тест c багом. Все то же самое что в уроке 1.6, только без try и finally
        browser = webdriver.Chrome()
        browser.get(link2)
        browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element_by_class_name("form-control.third").send_keys("ivanov@gmail.com")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(10)
        browser.quit()


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
if __name__ == "__main__":
    unittest.main()
