class MenuPage:
    def __init__(self, page):
        self.page = page
        self.quick_game_btn = page.get_by_text('Быстрый старт')

    def goto(self, url):
        self.page.goto(url)
