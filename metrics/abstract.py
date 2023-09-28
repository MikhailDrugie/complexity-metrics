from abc import ABC, abstractmethod


class AbstractMetrics(ABC):

    def __init__(self, code: str):
        self.code = code

    @abstractmethod
    def execute(self) -> dict:
        pass
