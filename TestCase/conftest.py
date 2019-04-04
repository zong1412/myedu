from selenium import webdriver
import pytest
import os
import time

@pytest.fixture(scope="session")
def driver():
    # 打开浏览器
    # 确定chromedriver.exe的位置
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    print(driver_path)
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(8)  # 设置隐式时间等待
    yield driver
    driver.quit()