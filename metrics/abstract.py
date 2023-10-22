from abc import ABC, abstractmethod
from patterns import AbstractPatterns
from patterns.re_pattern_factory import PatternFactory


class AbstractMetrics(ABC):

    def __init__(self, code: str, language: str | None):
        self.code = code
        self.language = language
        self.pattern_generator: AbstractPatterns = PatternFactory().get_class(language)

    @abstractmethod
    def execute(self) -> dict:
        pass
