import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    get_x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    result = calc(get_x)

    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(result)

    checkbox = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    radiobutton.click()

    submit = browser.find_element(By.XPATH, '//button[@class="btn btn-default"]')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

