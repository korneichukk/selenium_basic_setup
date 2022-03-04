from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
import ctypes
import json
import csv


def set_up_driver(headless=False):
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())

    if headless:
        options.add_argument('--headless')

    screen_size = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

    options.add_argument(f'window-size={screen_size[0]},{screen_size[1]}')
    options.add_argument('--disable-popup-blocking')

    from fake_useragent import UserAgent
    user_agent = UserAgent().random
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--enable-javascript')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(service=service, options=options)


if __name__ == '__main__':
    driver = set_up_driver()

    driver.maximize_window()
    driver.implicitly_wait(2)

