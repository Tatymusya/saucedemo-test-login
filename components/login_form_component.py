from components.base_component import BaseComponent
from playwright.sync_api import Page
from locators.login_page_locators import *
from elements.input import Input
from elements.title import Title
from elements.button import Button


class LoginFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.username_input = Input(
            page, locator=LOGIN_FIELD_TEST_ID, name='username'
        )

        self.password_input = Input(
            page, locator=PASSWORD_FIELD_TEST_ID, name='password'
        )

        self.validation_message = Title(
            page, locator=VALIDATION_MESSAGE_TEST_ID, name='validation'
        )

        self.validation_button_close = Button(
            page, locator=VALIDATION_BUTTON_CLOSE_TEST_ID, name='validation button close'
        )

    def fill_fields(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.username_input.should_have_value(username)

        self.password_input.fill(password)
        self.password_input.should_have_value(password)

    def check_enabled(self, username: str, password: str) -> None:
        self.username_input.should_be_visible()
        self.username_input.should_be_enabled()
        self.username_input.should_have_value(username)

        self.password_input.should_be_visible()
        self.password_input.should_be_enabled()
        self.password_input.should_have_value(password)

    def should_validation_button_close(self):
        self.validation_button_close.should_be_visible()

    def should_validation_when_user_missing_system(self):
        self.validation_message.should_be_visible()
        self.validation_message.should_have_text(VALIDATION_MESSAGE['missing_in_system'])
        self.should_validation_button_close()

    def should_validation_when_user_locked_out(self):
        self.validation_message.should_be_visible()
        self.validation_message.should_have_text(VALIDATION_MESSAGE['locked_out_user'])
        self.should_validation_button_close()

    def should_validation_when_username_empty(self):
        self.validation_message.should_be_visible()
        self.validation_message.should_have_text(VALIDATION_MESSAGE['empty_username'])
        self.should_validation_button_close()

    def should_validation_when_password_empty(self):
        self.validation_message.should_be_visible()
        self.validation_message.should_have_text(VALIDATION_MESSAGE['empty_password'])
        self.should_validation_button_close()

    def validation_button_close_click(self):
        self.validation_button_close.click()
        self.validation_message.should_be_not_visible()
