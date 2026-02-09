import allure
from playwright.sync_api import expect
from elements.base_element import BaseElement


class InteractiveElement(BaseElement):

    @property
    def type_of(self) -> str:
        return 'interactive_element'

    def hover(self) -> None:
        with allure.step(f'Установка события: hover на элементе {self.type_of}'):
            locator = self.get_locator()
            locator.hover()

    def press_enter(self) -> None:
        with allure.step(f'Установка события: нажатия Enter на элементе {self.type_of}'):
            locator = self.get_locator()
            locator.press('Enter')

    def should_be_enabled(self) -> None:
        with allure.step(f'Проверяем что элемент {self.type_of} может быть активирован'):
            locator = self.get_locator()
            expect(locator).to_be_enabled()

    def should_be_disabled(self) -> None:
        with allure.step(f'Проверяем что элемент {self.type_of} не может быть активирован'):
            locator = self.get_locator()
            expect(locator).to_be_disabled()
