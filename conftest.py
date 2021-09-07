import pytest
from selenium import webdriver
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(executable_path=DRIVER_BIN)
    driver.get('https://newsela.com/')
    driver.maximize_window()
    #  request.cls.driver = driver

    yield driver
    driver.close()

