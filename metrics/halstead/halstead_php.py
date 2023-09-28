from . import AbstractHalstead


class PhpHalstead(AbstractHalstead):

    def __init__(self, code: str):
        super().__init__(code)
