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


def logic_pattern(_str: str) -> str:
    patterns = {
        'is': r'\bis(?!\s+not\b)\b',
        'not': r'(?<!\bis\s)\bnot(?!\s+in)\b',
        'in': r'(?<!\bnot\s)\bin\b',
        'is not': r'\bis\s+not\b',
        'not in': r'\bnot\s+in\b'
    }
    pattern = patterns[_str] if _str in patterns.keys() else rf'\b{_str}\b'
    return combined_pattern(pattern)
