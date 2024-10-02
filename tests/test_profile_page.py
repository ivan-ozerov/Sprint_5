from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
from locators import Locators

class TestPersonalPage():

    def test_profile_page_enter_from_main_page(self, chrome_driver, login):

        chrome_driver.get(helper.MAIN_PAGE_URL)

        chrome_driver.find_element(*Locators.HEADER_TO_PERSONAL_PAGE_LINK).click()

        WebDriverWait(chrome_driver, 3).until(EC.url_to_be(helper.PROFILE_PAGE_URL))

        assert chrome_driver.current_url == helper.PROFILE_PAGE_URL

    