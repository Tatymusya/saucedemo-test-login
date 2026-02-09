import os
from dotenv_vault import load_dotenv
from playwright.sync_api import sync_playwright, expect

load_dotenv()

with sync_playwright() as playwright:
    playwright.selectors.set_test_id_attribute('data-test')
    chromium = playwright.firefox.launch(headless=False)
    page = chromium.new_page()
    url = os.getenv('APP_URL')
    page.goto(url, wait_until='domcontentloaded')

    new_title = 'This is func'
    page.evaluate(
        """
        (text) => {
            const title_page = document.querySelector('.login_logo')
            title_page.textContent = text
        }
        """,
        new_title
    )

    login_field = page.get_by_test_id('username')
    login_field.focus()

    for char in 'standard_user':
        page.keyboard.type(char)

    page.keyboard.press('ControlOrMeta+A')

    password_field = page.get_by_test_id('password')
    password_field.fill('secret_sauce')

    login_button = page.get_by_test_id('login-button')
    login_button.click()

    # block_error = page.get_by_test_id('error')
    # expect(block_error).to_be_visible()
    # expect(block_error).to_have_text('Epic sadface: Username and password do not match any user in this service')

    page.wait_for_timeout(5000)
