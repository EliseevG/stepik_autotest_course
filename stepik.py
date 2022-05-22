import time
import math
import lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(x))))
  # return int(x)+int(y)


   # Optional argument, if not specified will search path.

#maximize browser


try:
    browser = webdriver.Chrome('C:/Users/User/Desktop/AutoTest/chromedriver.exe')
    browser.get("http://suninjuly.github.io/huge_form.html")
    browser.maximize_window()
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("а")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

