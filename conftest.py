import pytest
from playwright.sync_api import Page
from pages.menu_page import MenuPage


@pytest.fixture(autouse=True)
def before_each(page: Page):
    menu_page = MenuPage(page)
    menu_page.goto("https://klavogonki.ru/")
    menu_page.quick_game_btn.click()
    yield
