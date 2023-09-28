from ..abstract import AbstractMetrics


class AbstractHalstead(AbstractMetrics):

    language_operators = []

    # η1
    operators: dict = {}
    # η2
    operands: dict = {}

    def __init__(self, code: str):
        super().__init__(code)

    def parse_code(self) -> None:
        """
        parses {code} and fills up {operators} and {operands}
        """
        pass

    def execute(self) -> dict:
        return {'code_lines': self.code.strip().split('\n')}
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
