import allure
from playwright.sync_api import expect
from elements.interactive_element import InteractiveElement


class Input(InteractiveElement):

    @property
    def type_of(self) -> str:
        return 'input'

    def fill(self, value: str, validate_value=False) -> None:
        with allure.step(f'Заполняем поле {self.type_of} значением'):
            locator = self.get_locator()
            locator.fill(value)

            if validate_value:
                self.should_have_value(value)

    def should_have_value(self, value: str) -> None:
        with allure.step(f'Проверяем что value поля {self.type_of} имеет значением'):
            locator = self.get_locator()
            expect(locator).to_have_value(value)
