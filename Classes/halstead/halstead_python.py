from .abstract import AbstractHalstead


class PythonHalstead(AbstractHalstead):

    def __init__(self, code: str):
        super().__init__(code)
