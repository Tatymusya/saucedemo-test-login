from elements.interactive_element import InteractiveElement


class Button(InteractiveElement):

    @property
    def type_of(self) -> str:
        return 'button'
