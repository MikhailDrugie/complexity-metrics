from ..abstract import AbstractMetrics


class AbstractMcCabe(AbstractMetrics):

    def __init__(self, code: str):
        super().__init__(code)

    def execute(self) -> dict:
        pass
