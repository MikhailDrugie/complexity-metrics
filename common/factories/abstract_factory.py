from enum import Enum
from .factory_helper import FactoryHelper


class AbstractFactory:

    enum: Enum | None = None

    def __init__(self):
        self.helper = FactoryHelper

    def get_class(self, lang: str):
        return self.helper.get_attribute(self.enum, lang)
