from . import AbstractHalstead


class PythonHalstead(AbstractHalstead):

    def __init__(self, code: str, count_func_call: bool = False):
        super().__init__(code, count_func_call)
        self.language_operators = {
            'arith': ['+', '-', '*', '**', '/', '//', '%'],
            'compare': ['<', '>', '<=', '>=', '==', '!='],
            'assign': ['=', '+=', '-=', '/=', '*=', '%=', '**=', '//='],
            'logic': ['and', 'or', 'not', 'is', 'in', 'not in', 'is not'],
            'bit': ['&', '|', '^', '~', '<<', '>>'],
            'loop': ['for', 'while'],
            'condition': ['if', 'elif', 'else'],
            'func': ['def', 'async def'],
            'class': ['class'],
            'return': ['return', 'yield'],
            'import': ['import']
        }
        self.statement_separator = "\n"
