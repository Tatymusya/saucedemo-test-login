from enum import Enum


class LoginValidationMode(Enum):
    LOCKED_UP_USER = 1
    EMPTY_USERNAME = 2
    EMPTY_PASSWORD = 3
    MISSING_IN_SYSTEM_USER = 4
