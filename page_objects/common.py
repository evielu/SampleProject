from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

TIME_OUT = 20


# find elements, more ways to find elements can be added later

def find_element(driver, locator):
    try:
        web_element = WebDriverWait(driver, TIME_OUT).until(
            ec.presence_of_element_located(locator))
        if web_element is not False:
            web_element.locator = locator
            return web_element
    except TimeoutException:
        return None


def find_elements(driver, locator):
    try:
        web_elements = WebDriverWait(driver, TIME_OUT).until(
            ec.visibility_of_all_elements_located(locator))
        return web_elements
    except TimeoutException:
        return None
