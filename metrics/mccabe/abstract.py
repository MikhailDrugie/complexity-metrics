from ..abstract import AbstractMetrics


class AbstractMcCabe(AbstractMetrics):

    def __init__(self, code: str, language: str | None = None):
        super().__init__(code, language)

    def execute(self) -> dict:
        pass
