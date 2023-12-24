from . import AbstractPatterns
from patterns.re_patterns import py_re


class PythonPatterns(AbstractPatterns):
    arith = py_re.special_symbol_pattern
    compare = py_re.special_symbol_pattern
    assign = py_re.special_symbol_pattern
    bit = py_re.special_symbol_pattern
    logic = py_re.logic_pattern
