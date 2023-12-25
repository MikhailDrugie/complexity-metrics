import math
import re
from ..abstract import AbstractMetrics


class AbstractHalstead(AbstractMetrics):
    language_operators: dict = {}
    language_datatypes: list = []

    statement_separator: str | None = None

    # η1
    operators: dict = {}
    # η2
    operands: dict = {
        'const': {},
        'var': {}
    }
    '''
        Число уникальных операторов (n1):
        Число уникальных операндов (n2):
        Общее число операторов (N1):
        Общее число операндов (N2):
        Алфавит (n): 	n1+n2
        Экспериментальна длина программы (Nэ): 	N1+N2
        Теоретическая длина программы (Nт): 	n1∙log2(n1) + n2∙log2(n2)
        Объём программы (V): 	Nэ∙log2(n)
        Потенциальный объём (V*): 	(N1*+N2*)∙log2(n1* + n2*) = 11.6 
        Уровень программы (L): 	V* / V (от 0 до 1)
        Сложность программы (S): 	L-1
        Ожидание уровня программы (L^):	(2/n1)∙(n2/N2)
        Интеллект программы (I):	L^ ∙ V
        Работа по программированию (Е):	V∙S ≡ V/L
        Время кодирования (T):	E/St (St – число Страуда от 5 до 20, берем 10)
        Ожидаемое время кодирования (T^):	n1∙N2 ∙ N∙log2(n) / (2∙St∙n2)
        Уровень языка программирования (Lam):	(V*)∙(V*)/V
        Уровень ошибок (В):	V / 3000
        '''
    n1 = None
    n2 = None
    _n1 = None
    _n2 = None
    n = None
    _n = None
    n_e = None
    n_t = None
    v = None
    _v = None
    l = None
    s = None
    _l = None
    i = None
    e = None
    t = None
    _t = None
    l_am = None
    b = None
    s_t = 10



    def __init__(self, code: str, count_func_call: bool = False, language: str | None = None):
        super().__init__(code, language)
        self.count_func_call = count_func_call

    def _get_code_statements(self):
        if not self.statement_separator:
            raise ValueError("Statement separator is not assigned!")
        return self.code.strip().split(self.statement_separator)

    def _get_operators(self):
        for operator_type, operators in self.language_operators.items():
            for operator in operators:
                pattern = self.pattern_generator.get_pattern(operator_type, operator)
                matches = re.findall(pattern, self.code, re.MULTILINE)
                amount = len([match[0] for match in matches if match[0]])
                self.operators[operator] = amount if amount > 0 else None
        self.operators = {key: value for key, value in self.operators.items() if value}

    def _get_operands(self):
        """Operands implementation in child classes"""
        pass

    def __traverse(self, *args, **kwargs):
        """Traverse parsed code nodes for operands via external packages"""
        pass

    def parse_code(self) -> None:
        """
        parses {code} and fills up {operators} and {operands}
        """
        self._get_operators()
        self._get_operands()

    def _calc_metrics(self):
        self.n1 = len(self.operators)
        self.n2 = len(self.operands['var']) + len(self.operands['const'])
        self._n1 = sum([i for i in self.operators.values()])
        self._n2 = sum([i for i in self.operands['var'].values()]) + sum([i for i in self.operands['const'].values()])
        self.n = self.n1 + self.n2
        self._n = self._n1 + self._n2
        self.n_e = self._n1 + self._n2
        self.n_t = self.n1 * math.log2(self.n1) + self.n2 * math.log2(self.n2)
        self.v = self.n_e * math.log2(self.n)
        self._v = (self._n1 + self._n2) * math.log2(self.n1 + self.n2)
        self.l = self._v / self.v
        self.s = pow(self.l, -1)
        self._l = (2 / self.n1) * (self.n2 / self._n2)
        self.i = self._l * self.v
        self.e = self.v * self.s
        self.t = self.e / self.s_t
        self._t = self.n1 * self._n2 * self._n * math.log2(self.n) / (2 * self.s_t * self.n2)
        self.l_am = (self._v ** 2) / self.v
        self.b = self.v / 3000

    def execute(self) -> dict:
        self.parse_code()
        self._calc_metrics()
        return {
            'statements': self._get_code_statements(),
            'operators': self.operators,
            'operands': self.operands,
            'uniq_operators': self.n1,
            'uniq_operands': self.n2,
            'total_operators': self._n1,
            'total_operands': self._n2,
            'alphabet': self.n,
            'exp_length': self.n_e,
            'theo_length': self.n_t,
            'vol': self.v,
            'pot_vol': self._v,
            'lvl': self.l,
            'soph': self.s,
            'est_lvl': self._l,
            'int': self.i,
            'prog_work': self.e,
            'cod_time': self.t,
            'est_cod_time': self._t,
            'prog_lang_lvl': self.l_am,
            'bug_lvl': self.b
        }

    def clear(self):
        self.operators = {}
        self.operands = {}
