from elements.base_element import BaseElement


class Title(BaseElement):

    @property
    def type_of(self) -> str:
        return 'title'
