import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.title import Title
from locators.catalog_page_locators import CATALOG_TITLE


class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.title = Title(
            page, locator=CATALOG_TITLE.test_id, name=CATALOG_TITLE.text
        )

    def check_visible_catalog_title(self) -> None:
        with allure.step('Проверяем что заголовок страницы каталога товаров видимый'):
            expect(self.title).should_be_visible()
            expect(self.title).should_have_text(CATALOG_TITLE.text)
        
