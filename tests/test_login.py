from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
from locators import Locators


class TestLogin():

    # вход с главной страницы
    def test_login_from_main_page(self, registration, chrome_driver, correct_credentials):

        chrome_driver.get(helper.MAIN_PAGE_URL)

        chrome_driver.find_element(*Locators.MAIN_PAGE_TO_LOGIN_PAGE_LINK).click()

        self.login_with_correct_credentials(chrome_driver, correct_credentials)

        assert chrome_driver.current_url == helper.MAIN_PAGE_URL
        
    # вход при клике на Личный кабинет
    def test_login_after_click_on_personal_page_button(self, registration, chrome_driver, correct_credentials):

        chrome_driver.get(helper.MAIN_PAGE_URL)

        chrome_driver.find_element(*Locators.HEADER_TO_PERSONAL_PAGE_LINK).click()

        self.login_with_correct_credentials(chrome_driver, correct_credentials)

        assert chrome_driver.current_url == helper.MAIN_PAGE_URL


    # вход при клике на ссылку на странице регистрации
    def test_login_from_registration_page(self, registration, chrome_driver, correct_credentials):

        chrome_driver.get(helper.REGISTRATION_PAGE_URL)

        chrome_driver.find_element(*Locators.REGISTRATION_PAGE_TO_LOGIN_PAGE_LINK).click()

        self.login_with_correct_credentials(chrome_driver, correct_credentials)

        assert chrome_driver.current_url == helper.MAIN_PAGE_URL


    # вход при клике на ссылку на странице восстановления пароля
    def test_login_from_password_recovery_page(self, registration, chrome_driver, correct_credentials):

        chrome_driver.get(helper.PASSWORD_RECOVERY_PAGE_URL)

        chrome_driver.find_element(*Locators.PASSWORD_RECOVERY_PAGE_TO_LOGIN_PAGE_LINK).click()

        self.login_with_correct_credentials(chrome_driver, correct_credentials)

        assert chrome_driver.current_url == helper.MAIN_PAGE_URL


    def login_with_correct_credentials(self, chrome_driver, correct_credentials):
        
        WebDriverWait(chrome_driver, 3).until(EC.url_to_be(helper.LOGIN_PAGE_URL))

        chrome_driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT_FIELD).send_keys(correct_credentials['email'])
        chrome_driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT_FIELD).send_keys(correct_credentials['password'])
        chrome_driver.find_element(*Locators.LOGIN_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(chrome_driver, 3).until(EC.url_to_be(helper.MAIN_PAGE_URL))
