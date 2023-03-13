from PySide6.QtCore import Signal, QDate
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLineEdit, QLabel, QWidget, QHBoxLayout, \
    QComboBox, QDateEdit

from bookkeeper.repository.sqlite_repository import SQliteRepository
from bookkeeper.models.category import Category


path = '/Users/mikhailgubanov/Yandex.Disk.localized/bookkeeper/bookkeeper/data_test.db'
cat_repo = SQliteRepository[Category](path, Category)


class AddExpenseWidget(QWidget):
    add_expense = Signal(str, str, int)  # TODO: дописать сигнал на добавление расходов

    def __init__(self):
        super().__init__()

        self.amount_lable = QLabel("Сумма:")
        self.amount_edit = QLineEdit()

        # Создаем валида тор для ввода положительных дробных чисел
        amount_validator = QIntValidator(0, 100000000)
        self.amount_edit.setValidator(amount_validator)

        self.category_lable = QLabel("Категория:")
        self.category_edit = QComboBox()

        # Добавляем категории в выпадающий список.   #TODO: Изменить ссылки на репозиторий
        categories = cat_repo.get_all()
        for category in categories:
            self.category_edit.addItem(category.name)

        self.datetime_lable = QLabel("Дата:")
        self.datetime_edit = QDateEdit()
        self.datetime_edit.setDate(QDate.currentDate())

        self.comment_lable = QLabel("Комментарий:")
        self.comment_edit = QLineEdit()

        self.edit_button = QPushButton('Категории')

        self.add_button = QPushButton("Добавить")

        category_layout = QHBoxLayout()
        category_layout.addWidget(self.category_edit)
        category_layout.addWidget(self.edit_button)

        layout = QVBoxLayout()
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_lable)
        amount_layout.addWidget(self.amount_edit)

        layout.addLayout(category_layout)
        layout.addLayout(amount_layout)
        layout.addWidget(self.datetime_lable)
        layout.addWidget(self.datetime_edit)
        layout.addWidget(self.comment_lable)
        layout.addWidget(self.comment_edit)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
