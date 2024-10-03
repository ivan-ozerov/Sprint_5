from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
from locators import Locators

class TestLogout:

    def test_logout_from_personal_page(self, chrome_driver, login):

        chrome_driver.find_element(*Locators.HEADER_TO_PERSONAL_PAGE_LINK).click()

        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_PAGE_LOGOUT_BUTTON))

        chrome_driver.find_element(*Locators.PROFILE_PAGE_LOGOUT_BUTTON).click()

        WebDriverWait(chrome_driver, 3).until(EC.url_to_be(helper.LOGIN_PAGE_URL))

        assert chrome_driver.current_url == helper.LOGIN_PAGE_URL