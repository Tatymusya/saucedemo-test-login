import allure
from playwright.sync_api import expect
from elements.interactive_element import InteractiveElement
from utils.input_type_mode import InputTypeMode


class Input(InteractiveElement):
    def __init__(self, page, locator, name, type_input: InputTypeMode = InputTypeMode.TEXT) -> None:
        super().__init__(page, locator, name)
        self.type_input = type_input

    @property
    def type_of(self) -> str:
        type_name = self.type_input.value
        return f'input_type_{type_name}'

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
