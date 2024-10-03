from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
from locators import Locators


class TestRegistration:
   # регистрация с корректными данными
   def test_registration_page_correct_credentials(self, chrome_driver, correct_credentials):

      chrome_driver.get(helper.REGISTRATION_PAGE_URL)

      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_NAME_INPUT_FIELD)))
      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_EMAIL_INPUT_FIELD)))
      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD)))
      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_REGISTRATION_BUTTON)))

      name_input_field = chrome_driver.find_element(*Locators.REGISTRATION_PAGE_NAME_INPUT_FIELD)
      email_input_field = chrome_driver.find_element(*Locators.REGISTRATION_PAGE_EMAIL_INPUT_FIELD)
      password_input_field = chrome_driver.find_element(*Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD)
      submit_button = chrome_driver.find_element(*Locators.REGISTRATION_PAGE_REGISTRATION_BUTTON)

      name_input_field.send_keys(correct_credentials['login'])
      email_input_field.send_keys(correct_credentials['email'])
      password_input_field.send_keys(correct_credentials['password'])
      submit_button.click()

      WebDriverWait(chrome_driver, 10).until(EC.url_to_be(helper.LOGIN_PAGE_URL))

      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE_EMAIL_INPUT_FIELD)))
      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE_PASSWORD_INPUT_FIELD)))
      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE_LOGIN_BUTTON)))

      email_input_field = chrome_driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT_FIELD)
      password_input_field = chrome_driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT_FIELD)
      login_button = chrome_driver.find_element(*Locators.LOGIN_PAGE_LOGIN_BUTTON)

      email_input_field.send_keys(correct_credentials['email'])
      password_input_field.send_keys(correct_credentials['password'])
      login_button.click()

      WebDriverWait(chrome_driver, 10).until(EC.url_to_be(helper.MAIN_PAGE_URL))
      
      assert chrome_driver.current_url == helper.MAIN_PAGE_URL


   # проверка вывода ошибки при длине пароля <6 символов 
   def test_registration_page_wrong_password(self, chrome_driver):
      chrome_driver.get(helper.REGISTRATION_PAGE_URL)

      password = "12345"

      WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD)))

      password_input_field =  chrome_driver.find_element(*Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD)
      email_input_field =  chrome_driver.find_element(*Locators.REGISTRATION_PAGE_EMAIL_INPUT_FIELD)

      password_input_field.send_keys(password)
      email_input_field.click()

      WebDriverWait(chrome_driver,5).until(EC.visibility_of_element_located(Locators.REGISTRATION_PAGE_INCORRECT_PASSWORD_ERROR_MESSAGE))

      assert chrome_driver.find_element(*Locators.REGISTRATION_PAGE_INCORRECT_PASSWORD_ERROR_MESSAGE).is_displayed()

