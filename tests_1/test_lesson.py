from datetime import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from tests.lesson_18 import sum_func


#
# kg = 99
# flag = False
# if kg == 100:
#     flag == True
#
#
# @pytest.fixture(autouse=True)
# def driver_init():
#     print("Chrome started")
#     yield
#     print("Chrome exit")
#
#
# # @pytest.mark.parametrize("Current result,result", [(sum_func([1, 3, 5, 10])), 19), (sum_func([1, 2, 3])), 5])
#
# @pytest.mark.parametrize("current_result,result",
#                          [(sum_func([1, 2, 3, 4, 5, 6, 78]), 99),
#                           (sum_func((6, 34)), 40)])
# def test_1(driver_init, current_result, result):
#     print("Test start")
#     assert current_result == result, f"Result should be {result}, but has {current_result}"
#     print("Test finish")
#
#
# @pytest.mark.parametrize("current_result,result",
#                          [(sum_func([1, 2, 3, 4, 5, 6, 78]), 99),
#                           (sum_func((6, 34)), 40)])
# @pytest.mark.tag_1
# def test_1(driver_init, current_result, result):
#     print("Test start")
#     assert current_result == result, f"Result should be {result}, but has {current_result}"
#     print("Test finish")

@pytest.fixture(autouse=True, scope="function")

def driver_1():
    print("\nstart browser for test..")
    browser = driver
    browser.get('ya.ru')
    time.sleep(5)
    yield browser
    print("\nquit browser..")
    # browser.quit()