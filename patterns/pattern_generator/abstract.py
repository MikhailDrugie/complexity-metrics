from abc import ABC, abstractmethod


def letters_pattern(_str: str) -> str:
    return rf'\b{_str}\b'


class AbstractPatterns(ABC):
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
