from . import AbstractHalstead


class CsharpHalstead(AbstractHalstead):

    def __init__(self, code: str, count_func_call: bool = False):
        super().__init__(code, count_func_call, 'csharp')
