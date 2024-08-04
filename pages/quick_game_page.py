from utils.sanitize_letter import sanitize_letter as sl


class QuickGamePage:
    def __init__(self, page):
        self.page = page
        self.start_game_btn = page.get_by_text('Начать игру')
        self.close_rules_btn = page.locator('//*[@id="howtoplay"]//*[@value="Закрыть"]')

        self.highlighted_text = page.locator('//*[@id="typefocus"]')
        self.after_focus = page.locator('//*[@id="afterfocus"]')
        self.text_input = page.locator('//*[@id="typeplayblock"]//input[@type="text"]')

        self.speed_result = page.locator('//div[@class="player you ng-scope"]//div[@class="stats"]/div[2]/span[1]')

    def goto(self, url):
        self.page.goto(url)

    def close_rules(self):
        self.close_rules_btn.click()

    def start_game(self):
        if self.start_game_btn.is_visible():
            self.start_game_btn.click()

    def insert_text(self):
        self.highlighted_text.click(timeout=60_000)
        while self.highlighted_text.is_visible():
            highlight = self.highlighted_text.inner_text()
            after_text = self.after_focus.inner_text()
            for letter in highlight:
                sanitized_letter = sl(letter)
                self.text_input.type(sanitized_letter)
            if after_text == '.':
                self.text_input.press('.')
                break
            self.text_input.press('Space')

    def get_game_result(self):
        res = self.speed_result.text_content()
        print(res)
