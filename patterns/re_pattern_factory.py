from common.factories import AbstractFactory
from enum import Enum
from patterns.pattern_generator import *


class PatternGenerators(Enum):
    python = PythonPatterns
    php = PhpPatterns
    cs = CsharpPatterns


class PatternFactory(AbstractFactory):
    enum = PatternGenerators
