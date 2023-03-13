"""
Виджет -- таблица отображения списка расходов
"""

from typing import List
from PySide6.QtWidgets import QVBoxLayout, QTableWidget, QWidget, QTableWidgetItem, QPushButton
from bookkeeper.models.expense import Expense
from bookkeeper.repository.abstract_repository import T


class ResentExpensesWidget(QWidget):
    cls: type[T]

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Список расходов")

        self.table_view = QTableWidget(4, 4)
        self.table_view.setHorizontalHeaderLabels(['Дата', 'Категория', 'Сумма', 'Комментарий'])

        self.expense_del_button = QPushButton('Удалить строку')

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.expense_del_button)
        self.setLayout(layout)

    def set_expenses(self, expenses):
        # Очищаем список расходов
        pass

    def display_expenses(self, expenses: List[Expense], category_repo):
        self.table_view.setRowCount(len(expenses))
        self.table_view.setColumnCount(4)

        for i, expense in enumerate(expenses):
            amount_item = QTableWidgetItem(str(expense.amount))
            category_item = QTableWidgetItem("{}".format(category_repo.get(expense.category).name))
            date_item = QTableWidgetItem(expense.expense_date)
            comment_item = QTableWidgetItem(expense.comment)
            self.table_view.setItem(i, 0, date_item)
            self.table_view.setItem(i, 1, category_item)
            self.table_view.setItem(i, 2, amount_item)
            self.table_view.setItem(i, 3, comment_item)
            self.table_view.resizeColumnsToContents()
            self.table_view.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
            self.table_view.setMaximumHeight(self.table_view.rowHeight(1) * 6)

        self.table_view.cellClicked.connect(self.on_cell_clicked)

    def on_cell_clicked(self):
        # получаем данные о выделенной строке
        selected_row_data = self.table_view.currentRow()
        return selected_row_data




