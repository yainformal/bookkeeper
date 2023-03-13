"""
Библиотека виджетов для приложения bookkeeper
"""

from bookkeeper.presenter.bookkeeper_pre import Bookkeeper
from bookkeeper.view.add_expense_widget import AddExpenseWidget
from bookkeeper.view.budget_widget import BudgetView
from bookkeeper.view.category_edit_widget import CategoryEditWidget
from bookkeeper.view.resent_expenses_widget import ResentExpensesWidget
from bookkeeper.view.toggle_window import toggle_window
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFormLayout, QComboBox
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.repository.sqlite_repository import SQliteRepository
from PySide6.QtCore import  Signal

path = '/Users/mikhailgubanov/Yandex.Disk.localized/bookkeeper/bookkeeper/data_test.db'


class BudgetUpdate(QWidget):
    """
    Виджет для добавления лимита расходов
    """
    budget_updated = Signal(str, str, float)

    def __init__(self):
        super().__init__()

        self.category_combo = QComboBox()
        self.category_combo.addItems(['День', 'Неделя', 'Месяц'])

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText('Лимит')

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self._save_budget)

        layout = QFormLayout()
        layout.addRow('Категория:', self.category_combo)
        layout.addRow('Сумма:', self.amount_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)


class MainWidget(QWidget):
    """
    Класс реализует функциональность предварительной сборки основного виджета
    """

    def __init__(self):
        super().__init__()

        self.add_expense_widget = AddExpenseWidget()
        self.resent_expenses_widget = ResentExpensesWidget()
        self.category_edit_view = CategoryEditWidget()
        self.exp_repo = SQliteRepository[Expense](path, Expense)
        self.category_repo = SQliteRepository[Category](path, Category)
        self.presenter = Bookkeeper(self.add_expense_widget, self.resent_expenses_widget, self.category_edit_view,
                                    self.exp_repo, self.category_repo)

        self.budget_view = BudgetView()

        layout = QVBoxLayout()
        layout.addWidget(self.add_expense_widget)
        layout.addWidget(self.budget_view)

        expense_view_button = QPushButton('Список расходов')
        expense_view_button.clicked.connect(
            lambda checked: toggle_window(self.resent_expenses_widget))

        layout.addWidget(expense_view_button)

        self.setLayout(layout)
