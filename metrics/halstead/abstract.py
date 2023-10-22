import re
from ..abstract import AbstractMetrics


class AbstractHalstead(AbstractMetrics):
    language_operators: dict = {}

    statement_separator: str | None = None

    # η1
    operators: dict = {}
    # η2
    operands: dict = {}

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
                if amount > 0:
                    self.operators[operator] = amount

    def _get_operands(self):
        pass

    def parse_code(self) -> None:
        """
        parses {code} and fills up {operators} and {operands}
        """
        self._get_operators()
        pass

    def execute(self) -> dict:
        self.parse_code()
        return {
            'statements': self._get_code_statements(),
            'operators': self.operators
        }
        pass

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
