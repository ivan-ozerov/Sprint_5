 # type: ignore
from selenium import webdriver
from selenium.webdriver.common.by import By

class Locators:

    #header

    # лого сайта
    HEADER_TO_MAIN_PAGE_APP_LOGO_LINK = (By.XPATH, "//header//div[contains(@class, 'header__logo')]//a[@href='/']")
    # кнопка "Личный кабинет"
    HEADER_TO_PERSONAL_PAGE_LINK = (By.XPATH, "//header//a[@href='/account']")
    # кнопка "Конструктор"
    HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK = (By.XPATH, "//header//p[text()='Конструктор']/parent::a[@href='/']")
    # кнопка "Конструктор" в активном состоянии  
    HEADER_TO_MAIN_PAGE_CONSTRUCTOR_ACTIVE_STATE_LINK = (By.XPATH, "//header//p[text()='Конструктор']/parent::a[contains(@class,'link_active')]")


    #registration page

    # инпут "Имя" на странице регистрации
    REGISTRATION_PAGE_NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    # инпут "email" на странице регистрации
    REGISTRATION_PAGE_EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/parent::div/input")
    # инпут "Пароль" на странице регистрации
    REGISTRATION_PAGE_PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div/input")
    # кнопка "Зарегистрироваться" 
    REGISTRATION_PAGE_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # кнопка "Войти" на странице регистрации
    REGISTRATION_PAGE_TO_LOGIN_PAGE_LINK = (By.XPATH, "//a[text()='Войти' and @href='/login']")
    # ошибка при вводе пароля <6 символов
    REGISTRATION_PAGE_INCORRECT_PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error') and text()='Некорректный пароль']")

    #login page

    # инпут "Имя" на странице входа
    LOGIN_PAGE_NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    # инпут "email" на странице входа
    LOGIN_PAGE_EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/parent::div/input")
    # инпут "Пароль" на странице входа
    LOGIN_PAGE_PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div/input")
    # кнопка "Войти" на странице входа
    LOGIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # кнопка "Зарегистрироваться" на странице входа
    LOGIN_PAGE_TO_REGISTRATION_PAGE_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # кнопка "Восстановить пароль" на странице входа
    LOGIN_PAGE_TO_RESTORE_PASSWORD_PAGE_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


    #main page

    # кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_TO_LOGIN_PAGE_LINK = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # кнопка "Булки" на главной странице
    MAIN_PAGE_CONSTRUCTOR_BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::div")
    # кнопка "Соусы" на главной странице
    MAIN_PAGE_CONSTRUCTOR_SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::div")
    # кнопка "Начинки" на главной странице
    MAIN_PAGE_CONSTRUCTOR_FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::div")
    # элемент "Флюоресцентная булка R2-D3" в списке "Булки"
    MAIN_PAGE_CONSTRUCTOR_BUN_ELEMENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    # элемент "Соус традиционный галактический" в списке "Соусы"
    MAIN_PAGE_CONSTRUCTOR_SAUCE_ELEMENT = (By.XPATH, "//p[text()='Соус традиционный галактический']")
    # элемент "Мясо бессмертных моллюсков Protostomia" в списке "Начинки"
    MAIN_PAGE_CONSTRUCTOR_FILLING_ELEMENT = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")

    #profile page
 
    # кнопка "Выход" в Личном кабинете
    PROFILE_PAGE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    #password_recovery_page    

    # кнопка "Войти" на странице восстановления пароля
    PASSWORD_RECOVERY_PAGE_TO_LOGIN_PAGE_LINK = (By.XPATH, "//a[text()='Войти' and @href='/login']")
