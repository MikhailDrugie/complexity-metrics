from . import AbstractHalstead


class CsharpHalstead(AbstractHalstead):

    def __init__(self, code: str):
        super().__init__(code)
