import time
import pytest
from page_objects.home_page import HomePage
from page_objects import common
from utilities.constants import ErrorMessages, MenuItems


@pytest.mark.regression
def test_title(driver):
    assert 'Online Education Platform for Content | Newsela | Newsela' in driver.title


@pytest.mark.regression
def test_menu_items(driver):
    # Validate values in Header menu exists
    menu_item_one = common.find_element(driver, HomePage.WHATS_NEW)
    assert menu_item_one.text == MenuItems.WHATS_NEW

    menu_item_two = common.find_element(driver, HomePage.CONTENT)
    assert menu_item_two.text == MenuItems.CONTENT

    menu_item_three = common.find_element(driver, HomePage.PRODUCTS)
    assert menu_item_three.text == MenuItems.PRODUCTS

    menu_item_four = common.find_element(driver, HomePage.SOLUTIONS)
    assert menu_item_four.text == MenuItems.SOLUTIONS

    menu_item_five = common.find_element(driver, HomePage.TRAINING)
    assert menu_item_five.text == MenuItems.TRAINING

    menu_item_six = common.find_element(driver, HomePage.RESOURCES)
    assert menu_item_six.text == MenuItems.RESOURCES

    menu_item_seven = common.find_element(driver, HomePage.COMPANY)
    assert menu_item_seven.text == MenuItems.COMPANY

    menu_item_eight = common.find_element(driver, HomePage.CONTACT)
    assert menu_item_eight.text == MenuItems.CONTACT


@pytest.mark.regression
def test_whats_new_menu_link(driver):
    # validate the what's new dropdown menu
    menu_item_one = common.find_element(driver, HomePage.WHATS_NEW)
    menu_item_one.click()
    menu_item_one_values = common.find_elements(driver, HomePage.WHATS_NEW_MENU_ITEMS)
    # Validate there are 3 menu items in What's New
    count = len(menu_item_one_values)
    assert count == 3
    if menu_item_one_values is not None:
        for menu_item in menu_item_one_values:
            print(menu_item.text)
    # Open first menu item in the dropdown for What's New
    menu_item_one_values[0].click()
    time.sleep(2)
    # check newly opened tab
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert 'Learning Found' in driver.title


@pytest.mark.regression
def test_enter_invalid_class_code(driver):
    # Validate inputting invalid student code gives error
    common.find_element(driver, HomePage.STUDENT_CODE_INPUT).send_keys(123)
    common.find_element(driver, HomePage.STUDENT_CODE_GO_BTN).click()
    time.sleep(2)
    error = common.find_element(driver, HomePage.STUDENT_CODE_ERROR).text
    assert error == ErrorMessages.INVALID_CODE_ERROR


@pytest.mark.regression
def test_click_learn_more_button(driver):
    # Validate clicking on the Learn More button takes you to Learning Found page
    common.find_element(driver, HomePage.LEARN_MORE).click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    assert 'Learning Found' in driver.title

