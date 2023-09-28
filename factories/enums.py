from enum import Enum
from metrics import *


class HalsteadEnum(Enum):
    py = PythonHalstead
    php = PhpHalstead
    cs = CsharpHalstead


class McCabeEnum(Enum):
    py = PythonMcCabe
    php = PhpMcCabe
    cs = CsharpMcCabe
