# SauceDemo Login Tests
Автоматизированные UI-тесты авторизации на сайте [https://www.saucedemo.com/](https://www.saucedemo.com/).
Saucedemo.com — это демо-сайт, созданный компанией Sauce Labs, который используется для практики автоматизированного тестирования. 
---
## Технологический стек

- Python 3.10
- Playwright
- Pytest
- Page Object Model
- Page Components
- Page Factory
- Allure
- Docker
---
## Структура проекта
```bash
saucedemo-test-login/
├── components/            # реализация паттерна: PageComponent
│   ├── __init__.py
│   ├── base_component.py
│   └── login_form_component.py
├── elements/              # реализация паттерна: PageFactory
│   ├── __init__.py
│   ├── base_element.py
│   ├── button.py
│   ├── input.py
│   ├── interactive_element.py
│   └── title.py
├── fixtures/              # код, который запускается перед запуском тестов
│   ├── __init__.py
│   ├── browser.py
│   ├── pages.py
│   └── settings.py
├── locators/              # конфиг локаторов для поиска элементов на странице
│   ├── __init__.py
│   ├── catalog_page_locators.py
│   └── login_page_locators.py
├── pages/                 # реализация паттерна: PageObject
│   ├── __init__.py
│   ├── base_page.py
│   ├── catalog_page.py
│   └── login_page.py
├── tests/                 # Тесты
│   ├── __init__.py
│   └── test_login.py
├── utils/                 # конфиги приложения и etc
│   ├── __init__.py
│   ├── config.py
│   ├── input_type_mode.py
│   └── login_validation_mode.py
├── conftest.py            # Конфигурация общих фикстур и настроек pytest
├── pytest.ini             # Конфигурация pytest
├── .gitignore             # Конфигурация git игнорируемых файлов и каталогов
├── requirements.txt       # Зависимости Python
├── Dockerfile             # Docker конфигурация
├── .env                   # Глобальная конфигурация
└── README.md              # Документация
```
---
## Тесты
Проект включает 7 тестовых сценариев авторизации:

### Позитивный сценарий
- **test_successful_by_click** - Успешный логин с пользователем <ins>standard_user</ins> по клику
- **test_successful_by_press_enter** - Успешный логин с пользователем <ins>standard_user</ins> по нажатию на клавишу Enter
- **test_successful_when_performance_glitch_by_click** - Логин пользователем <ins>performance_glitch_user</ins> с проверкой задержек по клику на кнопке

### Негативный сценарий
- **test_failed_user_locked_up_by_click** - Неуспешный логин заблокированного пользователя <ins>locked_out_user</ins> по клику
- **test_failed_user_missing_by_click** - Неуспешный логин заблокированного пользователя, которого нет в системе, по клику
- **test_failed_username_empty_by_click** - Неуспешный логин с пустым полем username, по клику
- **test_failed_password_empty_by_click** - Неуспешный логин с пустым полем password, по клику
---
## Установка и запуск
### Локальный запуск
#### Предварительные требования

- Python 3.10+
- pip

#### Шаги установки
1. **Клонировать репозиторий**
    ```bash
    git clone git@github.com:Tatymusya/saucedemo-test-login.git
    cd saucedemo-test-login
    ```
2. **Создать виртуальное окружение**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows
    ```
3. **Установить зависимости и браузеры для Playwright**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```
4. **Установить Allure (если еще не установлен)**
    ##### Mac:
    ```bash
    brew install allure
    ```
    ##### Linux:
    ```bash
    sudo apt-add-repository ppa:qameta/allure
    sudo apt-get update
    sudo apt-get install allure
    ```
    ##### Windows:
    ```bash
    npm install -g allure
    ```
   ###### либо
    ```bash
    scoop install allure
    ```
5. **Запуск тестов**
    Все тесты по-умолчанию запускаются с подробным выводом (флаг -v).
   ##### Всех тестов:
   ```bash
   pytest
   ```
   ##### Указываем браузерный движок:
   ```bash
   pytest --browser-name=[browser_name=("chromium", "firefox", "webkit")]
   ```
   ##### Запуск конкретного теста:
   ```bash
   pytest -k "test_failed_password_empty_by_click"
   ```
   ##### Запуск позитивных сценариев тестов:
   ```bash
   pytest -k "positive"
   ```
   ##### Запуск негативных сценариев тестов:
   ```bash
   pytest -k "negative"
   ```
   ##### Запуск с генерацией отчета:
   ```bash
   pytest -k "negative" --alluredir=allure-results
   ```
   ##### Просмотр отчета
    ```bash
   allure serve allure-results
    ```
    ##### Или создать статический HTML отчет:
    ```bash
   allure generate allure-results -o allure-report --clean
    ```
    ##### Открыть статический HTML отчет:
    ```bash
   allure open allure-report
    ```
---
### Запуск в Docker
#### Предварительные требования

- Docker

#### Шаги запуска
1. **Клонировать репозиторий**
    ```bash
    git clone git@github.com:Tatymusya/saucedemo-test-login.git
    cd saucedemo-test-login
    ```
2. **Собрать Docker образ**
    ```bash
    docker build -t saucedemo-test-login .
    ```
3. **Запустить тесты в контейнере**
    ```bash
    docker run --rm saucedemo-test-login
    ```
4. **Запустить тесты и сохранить результаты Allure**
    ```bash
    docker run --rm -v $(pwd)/allure-results:/app/allure-results saucedemo-test-login
    ```
5. **Запустить тесты и сохранить результаты Allure**
    ```bash
    docker run --rm -v $(pwd)/allure-results:/app/allure-results saucedemo-test-login
    ```
   ###### Для Windows PowerShell:
    ```bash
    docker run --rm -v ${PWD}/allure-results:/app/allure-results saucedemo-test-login
    ```
6. **Просмотреть отчет:**
    ```bash
    allure serve allure-results
    ```