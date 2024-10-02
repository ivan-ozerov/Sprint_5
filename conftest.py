import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import helper

# фикстура с вебдрайвером хрома
@pytest.fixture
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()

# фикстура с корректными кредами
@pytest.fixture
def correct_credentials():

    email = f"pirozok_s_kartoshkoi{random.randint(0, 1000)}@mail.ru"
    login = "Artemii"
    password = f"pirozok_s_kartoshkoi{random.randint(0, 1000)}"
    correct_credentials = {
        'email' : email,
        'login' : login,
        'password' : password
    }
    return correct_credentials

# фикстура регистрации
@pytest.fixture
def registration(chrome_driver, correct_credentials):

    chrome_driver.get(helper.REGISTRATION_PAGE_URL)

    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_NAME_INPUT_FIELD)))
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_EMAIL_INPUT_FIELD)))
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD)))
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_REGISTRATION_BUTTON)))

    chrome_driver.find_element(*Locators.REGISTRATION_PAGE_NAME_INPUT_FIELD).send_keys(correct_credentials['login'])
    chrome_driver.find_element(*Locators.REGISTRATION_PAGE_EMAIL_INPUT_FIELD).send_keys(correct_credentials['email'])
    chrome_driver.find_element(*Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD).send_keys(correct_credentials['password'])
    chrome_driver.find_element(*Locators.REGISTRATION_PAGE_REGISTRATION_BUTTON).click()

    WebDriverWait(chrome_driver, 10).until(EC.url_to_be(helper.LOGIN_PAGE_URL))

# фикстура аутентификации
@pytest.fixture
def login(registration, chrome_driver, correct_credentials):

    WebDriverWait(chrome_driver, 3).until(EC.url_to_be(helper.LOGIN_PAGE_URL))

    chrome_driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT_FIELD).send_keys(correct_credentials['email'])
    chrome_driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT_FIELD).send_keys(correct_credentials['password'])
    chrome_driver.find_element(*Locators.LOGIN_PAGE_LOGIN_BUTTON).click()

    WebDriverWait(chrome_driver, 3).until(EC.url_to_be(helper.MAIN_PAGE_URL))
