import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return 'base_element'

    def get_locator(self, nth: int = 0) -> Locator:
        locator = self.locator
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self) -> None:
        with allure.step(f'Событие: клик на элементе {self.type_of}'):
            locator = self.get_locator()
            locator.click()

    def should_be_visible(self) -> None:
        with allure.step(f'Проверяем что элемент {self.type_of} видимый'):
            locator = self.get_locator()
            expect(locator).to_be_visible()

    def should_be_not_visible(self) -> None:
        with allure.step(f'Проверяем что элемент {self.type_of} скрыт'):
            locator = self.get_locator()
            expect(locator).to_be_hidden()

    def should_have_text(self, text: str) -> None:
        with allure.step(f'Проверяем что элемент {self.type_of} имеет дочерний текстовый узел'):
            locator = self.get_locator()
            expect(locator).to_have_text(text)
