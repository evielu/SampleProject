import pytest
from page_objects.home_page import HomePage
from page_objects.join_now import JoinNow
from page_objects import common
from utilities.constants import ErrorMessages


@pytest.mark.regression
def test_join_now_roles(driver):
    # Check the different roles exist
    common.find_element(driver, HomePage.JOIN_NOW).click()
    student = common.find_element(driver, JoinNow.STUDENT_ROLE).text
    assert student == 'Student'
    teacher = common.find_element(driver, JoinNow.K12_ROLE).text
    assert teacher == 'K-12 Teacher'
    principal = common.find_element(driver, JoinNow.PRINCIPAL_ROLE).text
    assert principal == 'K-12 School Administrator'
    caregiver = common.find_element(driver, JoinNow.CAREGIVER_ROLE).text
    assert caregiver == 'Parent, Tutor, or Caregiver'


@pytest.mark.regression
def test_blank_principal_fields(driver):
    # TODO: Place these in a common utilities class
    # Click on join now for principal role
    common.find_element(driver, HomePage.JOIN_NOW).click()
    common.find_element(driver, JoinNow.PRINCIPAL_ROLE).click()
    # click sign up without filling out any fields and validate errors
    common.find_element(driver, JoinNow.SIGN_UP_BTN).click()
    # check errors match the expected error messages
    first_name_error = common.find_element(driver, JoinNow.FIRST_NAME_ERROR).text
    assert first_name_error == ErrorMessages.FIRST_NAME_REQUIRED
    last_name_error = common.find_element(driver, JoinNow.LAST_NAME_ERROR).text
    assert last_name_error == ErrorMessages.LAST_NAME_REQUIRED
    email_error = common.find_element(driver, JoinNow.EMAIL_ERROR).text
    assert email_error == ErrorMessages.EMAIL_REQUIRED
    password_error = common.find_element(driver, JoinNow.PASSWORD_ERROR).text
    assert password_error == ErrorMessages.PASSWORD_INVALID_ERR


@pytest.mark.regression
def test_principal_invalid_email_format(driver):
    # TODO: Place these in a common utilities class
    common.find_element(driver, HomePage.JOIN_NOW).click()
    common.find_element(driver, JoinNow.PRINCIPAL_ROLE).click()
    common.find_element(driver, JoinNow.SIGN_UP_BTN).click()
    # Validate invalid email address error
    common.find_element(driver, JoinNow.EMAIL).send_keys('abc')
    email_error = common.find_element(driver, JoinNow.EMAIL_ERROR).text
    assert email_error == ErrorMessages.EMAIL_INVALID


@pytest.mark.regression
def test_student_blank_code(driver):
    # TODO: Place these in a common utilities class
    common.find_element(driver, HomePage.JOIN_NOW).click()
    common.find_element(driver, JoinNow.STUDENT_ROLE).click()
    common.find_element(driver, JoinNow.STUDENT_JOIN_NEXT_BTN).click()
    # Validate invalid email address error
    code_error = common.find_element(driver, JoinNow.BLANK_CODE_ERROR).text
    assert code_error == ErrorMessages.CLASS_CODE_ERROR

