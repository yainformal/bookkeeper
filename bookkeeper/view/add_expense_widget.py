from PySide6.QtCore import Signal, QDateTime
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QTableWidget, QLineEdit, QLabel, QWidget, QHBoxLayout, \
    QComboBox, QDateTimeEdit

from bookkeeper.view.bookkeepr_widgets import cat_repo
from bookkeeper.view.category_edit_widget import CategoryEditWidget
from bookkeeper.view.toggle_window import toggle_window


class AddExpenseWidget(QWidget):
    add_expense = Signal(str, str, int)  # TODO: дописать сигнал на добавление расходов

    def __init__(self):
        super().__init__()

        self.category_edit_window = CategoryEditWidget()

        self.add_expense = None  # TODO: переработать метод
        self.amount_lable = QLabel("Сумма:")
        self.amount_edit = QLineEdit()

        self.category_lable = QLabel("Категория:")
        self.category_edit = QComboBox()

        # Добавляем категории в выпадающий список.
        categories = cat_repo.get_all()
        for category in categories:
            self.category_edit.addItem(category.name)

        self.datetime_lable = QLabel("Дата:")
        self.datetime_edit = QDateTimeEdit()
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())

        self.comment_lable = QLabel("Комментарий")
        self.comment_edit = QLineEdit()

        self.edit_button = QPushButton('Категории')
        self.edit_button.clicked.connect(
            lambda checked: toggle_window(self.category_edit_window))

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_expense)  # TODO: доработать метод добавления данных в репозиторий

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
        layout.addWidget(self.add_button)

        self.setLayout(layout)

