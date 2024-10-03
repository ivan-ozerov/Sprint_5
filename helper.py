from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# main page
MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'

# login page
LOGIN_PAGE_URL = MAIN_PAGE_URL + 'login'

# profile page
PROFILE_PAGE_URL = MAIN_PAGE_URL + 'account/profile'

# registration page
REGISTRATION_PAGE_URL = MAIN_PAGE_URL + 'register'

# password recovery page
PASSWORD_RECOVERY_PAGE_URL = MAIN_PAGE_URL + 'forgot-password'