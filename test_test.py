from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898"])
def test_collect_statement(browser, link):
    link2 = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link2)
    browser.implicitly_wait(15)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_class_name.send_keys(answer) ("textarea.string-quiz__textarea.ember-text-area.ember-view")  # поле для ввода результата
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    res_text = browser.find_element_by_class_name("smart-hints_hint")
    assert res_text == 'Correct!', f"Not equal to Correct!, only {res_text}"


