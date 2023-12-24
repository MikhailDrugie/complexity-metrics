import ast

from . import AbstractHalstead


class PythonHalstead(AbstractHalstead):

    def __init__(self, code: str, count_func_call: bool = False):
        super().__init__(code, count_func_call, 'python')
        self.language_operators = {
            'arith': ['+', '-', '*', '**', '/', '//', '%'],
            'compare': ['<', '>', '<=', '>=', '==', '!='],
            'assign': ['=', '+=', '-=', '/=', '*=', '%=', '**=', '//='],
            'logic': ['and', 'or', 'not', 'is', 'in', 'not in', 'is not'],
            'bit': ['&', '|', '^', '~', '<<', '>>'],
            'loop': ['for', 'while'],
            'condition': ['if', 'elif', 'else'],
            'func': ['def', 'async def', 'lambda'],
            'class': ['class'],
            'return': ['return', 'yield', 'await'],
            'import': ['import']
        }
        self.statement_separator = "\n"

    def _get_operands(self):
        tree = ast.parse(self.code)

        for _node in ast.walk(tree):
            self.__traverse(_node)

    def __traverse(self, node):
        if isinstance(node, (ast.Num, ast.Str)):
            k = node.n if isinstance(node, ast.Num) else node.s
            self.operands['const'][k] = 1 if k not in self.operands['const'].keys() \
                else self.operands['const'][k] + 1
        elif isinstance(node, ast.Name):
            k = node.id
            self.operands['var'][k] = 1 if k not in self.operands['var'].keys() \
                else self.operands['var'][k] + 1
