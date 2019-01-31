import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

element = browser.find_element_by_tag_name('body')

def notSoQuick():
    for i in range(100):
        element.send_keys(Keys.UP)
        # time.sleep(0.1)
        element.send_keys(Keys.RIGHT)
        # time.sleep(0.1)
        element.send_keys(Keys.DOWN)
        # time.sleep(0.1)
        element.send_keys(Keys.LEFT)
        # time.sleep(0.1)

def superQuick():
    for i in range(100):
        element.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)

# notSoQuick()
superQuick()