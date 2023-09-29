from . import special_symbol_pattern, letters_pattern


class Patterns:
    arith = special_symbol_pattern
    compare = special_symbol_pattern
    assign = special_symbol_pattern
    bit = special_symbol_pattern
    other = letters_pattern

    @classmethod
    def get_pattern(cls, operator_type: str, operator: str) -> str:
        try:
            func_name = getattr(cls, operator_type)
        except AttributeError:
            func_name = None
        if func_name:
            return func_name(operator)
        return cls.other(operator)
