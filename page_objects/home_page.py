from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Home page Locators
    WHATS_NEW = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[1]/div[1]/div')
    WHATS_NEW_MENU_ITEMS = (By.XPATH, '//header/div/nav/div[1]/div[2]/a')
    CONTENT = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[2]/div[1]/a')
    PRODUCTS = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[3]/div[1]/div')
    SOLUTIONS = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[4]/div[1]/div')
    TRAINING = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[5]/div[1]/div')
    RESOURCES = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[6]/div[1]/a')
    COMPANY = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[7]/div[1]/a')
    CONTACT = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/a[2]')
    LEARNING_FOUND = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/nav/div[1]/div[2]/a[1]')

    STUDENT_CODE_INPUT = (By.ID, 'class-code-input')
    STUDENT_CODE_GO_BTN = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/div/form/button')
    STUDENT_CODE_ERROR = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/header/div/div/form/div')

    JOIN_NOW = (By.XPATH, '//a[@data-qa-selector="unauth_homepage_join"]')
    SIGN_IN = (By.XPATH, '//a[@data-qa-selector="sign_in_button_masthead]')

    LEARN_MORE = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[1]/div/div[1]/a')





