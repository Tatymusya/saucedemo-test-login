import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.heading import Heading
from locators.catalog_page_locators import CATALOG_TITLE
from utils.config import APP_CATALOG_URL


class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, current_url=APP_CATALOG_URL)
        self.page = page

        self.title_page = Heading(
            page, locator=CATALOG_TITLE['test_id'], name=CATALOG_TITLE['text']
        )

    def check_visible_catalog_title(self) -> None:
        with allure.step('Проверяем что заголовок страницы каталога товаров видимый'):
            expect(self.title_page).should_be_visible()
            expect(self.title_page).should_have_text(CATALOG_TITLE['text'])
        
