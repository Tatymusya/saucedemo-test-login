import pytest
from utils.config import APP_URL
from playwright.sync_api import Page, Browser
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def browser_page(browser: Browser) -> Page:
    try:
        context = browser.new_context(
            base_url=f"{APP_URL}/"
        )

        browser_page = context.new_page()
        LoginPage(page=browser_page)
        yield browser_page

        browser.close()
    except Exception as err:
        pytest.exit("Error: " + f'{err}')


@pytest.fixture(scope='function')
def login_page(browser_page: Page) -> LoginPage:
    return LoginPage(browser_page)
