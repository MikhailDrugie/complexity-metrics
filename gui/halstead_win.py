from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget

from . import AbstractWindow
from metrics_factories import HalsteadFactory


class MainWindow(AbstractWindow):

    def __init__(self):
        super(MainWindow, self).__init__(app_name="Halstead's complexity metrics")
        self._factory = HalsteadFactory()

        self.set_basic()
        self.set_layout()

    def __set_operators_widget(self, table_widget: QTableWidget, operators: dict):
        for i, key_value in enumerate(operators.items()):
            operators_table = QTableWidget(self)
            operators_table.setRowCount(1)
            operators_table.setColumnCount(2)
            operators_table.verticalHeader().setVisible(False)
            operators_table.horizontalHeader().setVisible(False)
            operators_table.setItem(0, 0, QTableWidgetItem(key_value[0]))
            operators_table.setItem(0, 1, QTableWidgetItem(str(key_value[1])))
            table_widget.setCellWidget(i + 1, 0, operators_table)

    def __set_operands_header(self, table_widget: QTableWidget):
        operands_head_table = QTableWidget(self)
        operands_head_table.setRowCount(1)
        operands_head_table.setColumnCount(3)
        operands_head_table.verticalHeader().setVisible(False)
        operands_head_table.horizontalHeader().setVisible(False)
        operands_head_table.setItem(0, 0, QTableWidgetItem('Константы'))
        operands_head_table.setItem(0, 2, QTableWidgetItem('Переменные'))
        table_widget.setCellWidget(1, 1, operands_head_table)

    def __set_operands_widget(self, table_widget: QTableWidget, operands: dict):
        for i in range(max(len(operands['var']), len(operands['const']))):
            inner_table = QTableWidget(self)
            inner_table.setRowCount(1)
            inner_table.setColumnCount(4)
            inner_table.verticalHeader().setVisible(False)
            inner_table.horizontalHeader().setVisible(False)
            var_row = list(operands['var'].items())[i] \
                if i < len(operands['var']) else ('', '')
            const_row = list(operands['const'].items())[i] \
                if i < len(operands['const']) else ('', '')
            row = const_row + var_row
            for ind, it in enumerate(row):
                inner_table.setItem(0, ind, QTableWidgetItem(str(it)))
            table_widget.setCellWidget(i + 2, 1, inner_table)

    def populate_table(self, table_widget, data):
        num_rows = max(len(data['operators']), len(data['operands']['var']), len(data['operands']['const'])) + 2
        num_cols = 2
        table_widget.setRowCount(num_rows)
        table_widget.setColumnCount(num_cols)
        table_widget.setItem(0, 0, QTableWidgetItem('Операторы'))
        table_widget.setItem(0, 1, QTableWidgetItem('Операнды'))
        table_widget.setColumnWidth(0, 203)
        table_widget.setColumnWidth(1, 406)
        self.__set_operators_widget(table_widget, data['operators'])
        self.__set_operands_header(table_widget)
        self.__set_operands_widget(table_widget, data['operands'])

    def get_general_info(self, data):
        return {
            "Число уникальных операторов (n1)": data['uniq_operators'],
            "Число уникальных операндов (n2)": data['uniq_operands'],
            "Общее число операторов (N1)": data['total_operators'],
            "Общее число операндов (N2)": data['total_operands'],
            "Алфавит (n)": data['alphabet'],
            "Экспериментальна длина программы (Nэ)": data['exp_length'],
            "Теоретическая длина программы (Nт)": data['theo_length'],
            "Объём программы (V)": data['vol'],
            "Потенциальный объём (V*)": data['pot_vol'],
            "Уровень программы (L)": data['lvl'],
            "Сложность программы (S)": data['soph'],
            "Ожидание уровня программы (L^)": data['est_lvl'],
            "Интеллект программы (I)": data['int'],
            "Работа по программированию (Е)": data['prog_work'],
            "Время кодирования (T)": data['cod_time'],
            "Ожидаемое время кодирования (T^)": data['est_cod_time'],
            "Уровень языка программирования (Lam)": data['prog_lang_lvl'],
            "Уровень ошибок (В)": data['bug_lvl']
        }
