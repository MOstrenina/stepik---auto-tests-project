from selenium import webdriver
import time
from time import sleep

import math

from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2").text
    x = int(x_element)
    y = int(y_element)
    s = str(x + y)

    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(s)

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



