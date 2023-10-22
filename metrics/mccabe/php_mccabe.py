from . import AbstractMcCabe


class PhpMcCabe(AbstractMcCabe):

    def __init__(self, code: str):
        super().__init__(code, 'php')
