from ..abstract import AbstractMetrics


class AbstractHalstead(AbstractMetrics):

    def __init__(self, code: str):
        super().__init__(code)

    def execute(self) -> dict:
        return {'test': 'result'}
        pass
