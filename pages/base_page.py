import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url_page: str) -> None:
        with allure.step(f'Открываем страницу: {url_page}'):
            self.page.goto(url_page, wait_until='networkidle')

    def reload_page(self) -> None:
        with allure.step(f'Перезагружаем страницу: {self.page}'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: str):
        with allure.step(f'Проверяем что URL страницы соответствует: {expected_url}'):
            expect(self.page).to_have_url(expected_url)
