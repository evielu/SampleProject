from selenium import webdriver
from selenium.webdriver.common.by import By


class JoinNow:
    def __init__(self, driver):
        self.driver = driver

    # Join Now locators
    STUDENT_ROLE = (By.XPATH, '//button[@data-qa-selector="select_student_button"]')
    K12_ROLE = (By.XPATH, '//button[@data-qa-selector="select_teacher_button"]')
    PRINCIPAL_ROLE = (By.XPATH, '//button[@data-qa-selector="select_principal_button"]')
    CAREGIVER_ROLE = (By.XPATH, '//button[@data-qa-selector="select_caregiver_button"]')
    JOIN_NOW_HEADER = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/div[1]/h1')
    SIGN_UP_ROLE_HEADER = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/p[1]')
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    SIGN_UP_BTN = (By.XPATH, '//button[@data-qa-selector="sign_up_button"]')
    FIRST_NAME_ERROR = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/form/div/label[1]/span')
    LAST_NAME_ERROR = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/form/div/label[2]/span')
    EMAIL_ERROR = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/form/div/label[3]/span')
    PASSWORD_ERROR = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/form/div/label[4]/span')
    STUDENT_CLASS_CODE_INPUT = (By.XPATH, '//*[@id="classCode"]')
    BLANK_CODE_ERROR = (By.XPATH, '//*[@id="contentContainer"]/div/div/div/form/label/span/span[2]')
    STUDENT_JOIN_NEXT_BTN = (By.XPATH, '//button[@data-qa-selector="next_button"]')



