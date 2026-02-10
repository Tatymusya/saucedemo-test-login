import pytest
import allure
from utils.config import APP_URL, APP_CATALOG_URL
from pages.login_page import LoginPage
from utils.login_validation_mode import LoginValidationMode


@allure.epic('Sauce Demo тесты')
@allure.feature('Авторизация')
class TestLogin:
    @staticmethod
    def prepare_fields(login_page: LoginPage, username: str, password: str) -> None:
        login_page.login_form.check_enabled()
        login_page.login_form.fill_fields(
            username,
            password
        )

    @staticmethod
    def setup_login(login_page: LoginPage, username: str, password: str) -> None:
        login_page.open_page(APP_URL)
        TestLogin.prepare_fields(login_page, username, password)

    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 1: Успешная авторизация по клику на кнопке Login')
    @allure.story('Позитивный сценарий')
    @allure.tag('positive')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('standard_user', 'secret_sauce'),
        ]
    )
    def test_successful_by_click(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.click_login_button()
        login_page.check_current_url(APP_CATALOG_URL)

    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 2: Успешная авторизация по нажатию Enter на кнопке Login')
    @allure.story('Позитивный сценарий')
    @allure.tag('positive')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('standard_user', 'secret_sauce'),
        ]
    )
    def test_successful_by_press_enter(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.press_enter_login_button()
        login_page.check_current_url(APP_CATALOG_URL)

    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 3: Успешная авторизация при проблемах с сетью')
    @allure.story('Позитивный сценарий')
    @allure.tag('positive')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('performance_glitch_user', 'secret_sauce')
        ]
    )
    def test_successful_when_performance_glitch_by_click(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.click_login_button()
        login_page.page.wait_for_load_state('domcontentloaded')
        login_page.check_current_url(APP_CATALOG_URL)

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 4: Неуспешная авторизация если пользователь заблокирован')
    @allure.story('Негативный сценарий')
    @allure.tag('negative')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('locked_out_user', 'secret_sauce')
        ]
    )
    def test_failed_user_locked_up_by_click(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.click_login_button()
        login_page.check_current_url(APP_URL)
        login_page.should_validation_message_is_visible(mode=LoginValidationMode.LOCKED_UP_USER)

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 5: Неуспешная авторизация если пользователь отсутствует в базе данных')
    @allure.story('Негативный сценарий')
    @allure.tag('negative')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('missing_user', 'secret_sauce'),
        ]
    )
    def test_failed_user_missing_by_click(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.click_login_button()
        login_page.check_current_url(APP_URL)
        login_page.should_validation_message_is_visible(LoginValidationMode.MISSING_IN_SYSTEM_USER)

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 6: Неуспешная авторизация если поле username пустое')
    @allure.story('Негативный сценарий')
    @allure.tag('negative')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('', 'secret_sauce')
        ]
    )
    def test_failed_username_empty_by_click(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.click_login_button()
        login_page.check_current_url(APP_URL)
        login_page.should_validation_message_is_visible(LoginValidationMode.EMPTY_USERNAME)

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.all
    @allure.title('Тест 7: Неуспешная авторизация если поле password пустое')
    @allure.story('Негативный сценарий')
    @allure.tag('negative')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'username, password',
        [
            ('standard_user', '')
        ]
    )
    def test_failed_password_empty_by_click(
            self,
            login_page: LoginPage,
            username: str,
            password: str
    ) -> None:
        self.username = username
        self.password = password
        TestLogin.setup_login(login_page, self.username, self.password)

        login_page.click_login_button()
        login_page.check_current_url(APP_URL)
        login_page.should_validation_message_is_visible(LoginValidationMode.EMPTY_PASSWORD)
