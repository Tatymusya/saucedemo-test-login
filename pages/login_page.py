import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from components.login_form_component import LoginFormComponent
from elements.button import Button
from elements.input import Input
from elements.title import Title
from locators.login_page_locators import *
from utils.login_validation_mode import LoginValidationMode


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.login_form = LoginFormComponent(page)

        self.submit_input = Input(
            page, locator=LOGIN_BUTTON_TEST_ID, name='submit'
        )

        self.error_message = Title(
            page, locator=VALIDATION_MESSAGE_TEST_ID, name='error message'
        )

        self.error_close_button = Button(
            page, locator=VALIDATION_BUTTON_CLOSE_TEST_ID, name='error close button'
        )

    def click_login_button(self) -> None:
        self.submit_input.click()

    def press_enter_login_button(self) -> None:
        self.submit_input.press_enter()

    def should_validation_message_is_visible(self, mode: LoginValidationMode) -> None:
        with allure.step('Проверяем какое валидационное сообщение показывается из-за ошибки ввода'):
            if mode == LoginValidationMode.EMPTY_USERNAME:
                self.login_form.should_validation_when_username_empty()
            elif mode == LoginValidationMode.EMPTY_PASSWORD:
                self.login_form.should_validation_when_password_empty()
            elif mode == LoginValidationMode.LOCKED_UP_USER:
                self.login_form.should_validation_when_user_locked_out()
            else:
                self.login_form.should_validation_when_user_missing_system()
