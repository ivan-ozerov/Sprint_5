from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper
import time
from locators import Locators

class TestConstructor:

    # проверка того, что секция "Булки" выбраны по дефолту
    def test_constructor_buns_active_by_default(self, chrome_driver, login):

        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_CONSTRUCTOR_BUNS_BUTTON))


    # проверка переключения на секцию "Соусы"
    def test_constructor_switch_to_section_sauces(self, chrome_driver, login):

        chrome_driver.find_element(*Locators.MAIN_PAGE_CONSTRUCTOR_SAUCE_BUTTON).click()
        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_CONSTRUCTOR_SAUCE_ELEMENT))

    # проверка переключения на секцию "Начинки"
    def test_constructor_switch_to_section_fillings(self, chrome_driver, login):

        chrome_driver.find_element(*Locators.MAIN_PAGE_CONSTRUCTOR_FILLINGS_BUTTON).click()
        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_CONSTRUCTOR_FILLING_ELEMENT))

    # проверка переключения на секцию "Булки"
    def test_constructor_switch_to_section_buns(self, chrome_driver, login):

        chrome_driver.find_element(*Locators.MAIN_PAGE_CONSTRUCTOR_FILLINGS_BUTTON).click()
        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_CONSTRUCTOR_FILLING_ELEMENT))
        
        WebDriverWait(chrome_driver, 3).until(EC.element_to_be_clickable(Locators.MAIN_PAGE_CONSTRUCTOR_BUNS_BUTTON))
        chrome_driver.find_element(*Locators.MAIN_PAGE_CONSTRUCTOR_BUNS_BUTTON).click()
        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_CONSTRUCTOR_BUN_ELEMENT))
