from enum import Enum


class InputTypeMode(Enum):
    TEXT = 'text'
    SUBMIT = 'submit'
    PASSWORD = 'password'
    EMAIL = 'email'
    NUMBER = 'number'
    HIDDEN = 'hidden'
