from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
from locators import Locators

class TestMainPage():

    def test_constructor_enter_from_profile_page_by_logo_button(self, chrome_driver, login):

        chrome_driver.find_element(*Locators.HEADER_TO_PERSONAL_PAGE_LINK).click()

        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.HEADER_TO_MAIN_PAGE_APP_LOGO_LINK))

        chrome_driver.find_element(*Locators.HEADER_TO_MAIN_PAGE_APP_LOGO_LINK).click()

        WebDriverWait(chrome_driver,3).until(EC.url_to_be(helper.MAIN_PAGE_URL))
        WebDriverWait(chrome_driver,3).until(EC.visibility_of_element_located(Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_ACTIVE_STATE_LINK))

        assert 'link_active' in chrome_driver.find_element(*Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK).get_attribute('class')


    def test_constructor_enter_from_profile_page_by_constructor_button(self, chrome_driver, login):

        chrome_driver.find_element(*Locators.HEADER_TO_PERSONAL_PAGE_LINK).click()

        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK))

        chrome_driver.find_element(*Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK).click()

        WebDriverWait(chrome_driver,3).until(EC.url_to_be(helper.MAIN_PAGE_URL))
        WebDriverWait(chrome_driver,3).until(EC.visibility_of_element_located(Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_ACTIVE_STATE_LINK))

        assert 'link_active' in chrome_driver.find_element(*Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK).get_attribute('class')


        
