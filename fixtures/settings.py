import pytest
from utils.config import TEST_ID_ATTRIBUTE


@pytest.fixture(scope='session', autouse=True)
def set_playwright_test_id(playwright):
    playwright.selectors.set_test_id_attribute(TEST_ID_ATTRIBUTE)
