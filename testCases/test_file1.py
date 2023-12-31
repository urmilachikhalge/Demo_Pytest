import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


class Test_py:

    def test_sum_001(self):
        a = 2
        b = 4
        sum = a + b
        print("sum -- >" + str(sum))
        if sum == 6:
            assert True
        else:
            assert False

    def test_mul_002(self):
        a = 2
        b = 4
        mul = a * b
        print("mul -- >" + str(mul))
        if mul == 8:
            assert True
        else:
            assert False

    def test_credenceUrl_003(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        print(driver.title)
        if driver.title == "Credence":
            print("Your are at credence site")
            assert True
        else:
            print("Your are at wrong site")
            assert False
        driver.quit()

    def test_sum_004(self):
        a = 9
        b = 7
        sum = a + b
        print("sum_004 -- >" + str(sum))
        if sum == 16:
            assert True
        else:
            assert False
