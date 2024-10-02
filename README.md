Данный проект призван покрыть автотестами веб-сайт https://stellarburgers.nomoreparties.site/.

В данном проекте в качестве тестового фреймворка используется Pytest, в качестве библиотеки автоматизации e2e тестов - Selenium Webdriver.

Для запуска тестов нужно прописать в консоль команду:

```
pytest
```

находясь в корневой директории, или, если нужны отдельные файлы - 

```
pytest tests/<file_name>
```

Описание файлов и директорий:
helper.py - вспомогательный файл с url-ами нужных страниц, использующихся в тестах
locators.py - файл с локаторами, использующимися в тестах
conftest.py - файл с фикстурами
tests/ - основная директория с тестами, каждый из которых проверяет функциональность, описанную ниже:  
    test_login.py - аутентификация на сайте с разных url-ов
    test_constructor.py - конструктор 
    test_logout.py - логаут 
    test_main_page.py - главная страница
    test_profile_page.py - личный кабинет
    test_registration.py - регистрация


