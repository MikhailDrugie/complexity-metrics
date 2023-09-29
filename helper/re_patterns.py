def edit_very_special_syms(_str: str) -> str:
    return ''.join([f'\\{sym}' if sym in '+*|^' else sym for sym in _str])


def special_symbol_pattern(_str: str) -> str:
    _str = edit_very_special_syms(_str)
    return rf'(?<![/*=\+\-\%\<\>!]){_str}(?![=/*\<\>])'


def letters_pattern(_str: str) -> str:
    return rf'\b{_str}\b'
