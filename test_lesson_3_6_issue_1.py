from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest



@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_collect_statement(browser, link):
    link2 = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link2)
    browser.implicitly_wait(5)
    res_field = browser.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view")  # поле для ввода результата
    answer = str(math.log(int(time.time())))
    res_field.send_keys(answer)  # ввод значения в поле
    button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    res_text = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    assert res_text == 'Correct!', \
        f"Not equal to expected result, only '{res_text}'"


# красивый запуск pytest -s -v --tb=line test_lesson_3_6_issue_1.py