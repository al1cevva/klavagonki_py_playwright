from pages.quick_game_page import QuickGamePage
from playwright.sync_api import expect, Page


def test_quick_game(page: Page):
    quick_game = QuickGamePage(page)
    # Close game rules
    quick_game.close_rules()
    expect(quick_game.close_rules_btn, "Правила игры не были закрыты").not_to_be_visible()
    # Start game
    quick_game.start_game()
    # Insert text
    quick_game.insert_text()
    # Check results
    quick_game.get_game_result()




