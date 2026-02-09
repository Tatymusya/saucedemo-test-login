import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption(
        '--browser-name', action='store', default='chromium', help='Browser: chromium, firefox, or webkit', type=str
    )


@pytest.fixture(scope='function')
def browser(request, playwright: Playwright):
    browser_name = request.config.getoption('--browser-name')
    browser_type = getattr(playwright, browser_name)
    browser = browser_type.launch(headless=True)
    return browser

