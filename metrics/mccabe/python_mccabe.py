from . import AbstractMcCabe


class PythonMcCabe(AbstractMcCabe):

    def __init__(self, code: str):
        super().__init__(code, 'python')
