def string_pattern() -> str:
    return r'(?:\'[^\'\\]*(?:\\.[^\'\\]*)*\'|"[^"\\]*(?:\\.[^"\\]*)*")'


def comment_pattern() -> str:
    return r'#.*$'


def combined_pattern(pattern: str) -> str:
    return f'({pattern})|({string_pattern()})|({comment_pattern()})'


def edit_very_special_syms(_str: str) -> str:
    return ''.join([f'\\{sym}' if sym in '+*|^' else sym for sym in _str])


def special_symbol_pattern(_str: str) -> str:
    """
    :param _str: what to find
    :return: combined pattern excluding strings and comments
    """
    _str = edit_very_special_syms(_str)
    return combined_pattern(rf'(?<![/*=\+\-\%\<\>!]){_str}(?![=/*\<\>\+\-])')


def letters_pattern(_str: str) -> str:
    return combined_pattern(rf'\b{_str}\b')
