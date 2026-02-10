import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, current_url: str):
        self.page = page
        self.current_url = current_url

    def open_page(self, url_page: str) -> None:
        with allure.step(f'Открываем страницу: {url_page}'):
            self.page.goto(url_page, wait_until='networkidle')
            self.current_url = self.page.url

    def reload_page(self) -> None:
        with allure.step(f'Перезагружаем страницу: {self.page}'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: str):
        if self.current_url == expected_url:
            with allure.step(f'Проверяем что URL страницы соответствует: {expected_url}, переход не произошел'):
                expect(self.page).to_have_url(expected_url)
        else:
            with allure.step(f'Проверяем что URL страницы соответствует: {expected_url}, переход произошел'):
                expect(self.page).to_have_url(expected_url)
