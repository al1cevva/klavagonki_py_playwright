import allure
from pages.quick_game_page import QuickGamePage
from playwright.sync_api import expect, Page


@allure.feature('Quick game')
@allure.story('Start quick game and check results')
def test_quick_game(page: Page):
    with allure.step('Go to quick game'):
        quick_game = QuickGamePage(page)
        # Close game rules
        quick_game.close_rules()
        expect(quick_game.close_rules_btn, "Правила игры не были закрыты").not_to_be_visible()
    with allure.step('Start game'):
        # Start game
        quick_game.start_game()
    with allure.step('Insert text'):
        # Insert text
        quick_game.insert_text()
    with allure.step('Check results'):
        # Check results
        quick_game.get_game_result()
