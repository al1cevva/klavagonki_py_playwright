def sanitize_letter(letter: str) -> str:
    """
    :param letter: Буква
    :return: Кириллическую букву
    """
    letters_map = {
        'o': 'о',
        'O': 'О',
        'e': 'е',
        'E': 'Е',
        'a': 'а',
        'A': 'А',
        'H': 'Н',
        'K': 'К',
        'x': 'х',
        'X': 'Х',
        'c': 'с',
        'C': 'С',
        'B': 'В',
        'M': 'М'
    }
    if letter in letters_map:
        return letters_map[letter]
    return letter
