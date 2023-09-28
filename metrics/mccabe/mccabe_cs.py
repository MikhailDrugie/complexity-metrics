from . import AbstractMcCabe


class CsharpMcCabe(AbstractMcCabe):

    def __init__(self, code: str):
        super().__init__(code)
