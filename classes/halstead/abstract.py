from abc import ABC, abstractmethod


class AbstractHalstead(ABC):

    def __init__(self, code: str):
        self.code = code
