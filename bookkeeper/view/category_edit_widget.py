from typing import List

from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QTableWidget, QLineEdit, QLabel, QWidget, QHBoxLayout, \
    QTableWidgetItem

from bookkeeper.models import expense
from bookkeeper.models.category import Category


def add_cat():
    print("добавить")
    pass


def del_cat():
    print('удалить')
    pass


class CategoryEditWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.add_expense = None
        self.setWindowTitle("Редактирование категорий")

        self.category_edit_view = QTableWidget(2, 2)
        self.category_edit_view.setHorizontalHeaderLabels(['Категория', 'Родительская категория'])

        self.cat_lable = QLabel("Категория:")
        self.cat_edit = QLineEdit()
        self.sub_cat_lable = QLabel("Родительская категория")
        self.sub_cat_edit = QLineEdit()

        line_layout = QVBoxLayout()
        line_layout.addWidget(self.cat_lable)
        line_layout.addWidget(self.cat_edit)
        line_layout.addWidget(self.sub_cat_lable)
        line_layout.addWidget(self.sub_cat_edit)

        self.add_cat_button = QPushButton('Добавить')
        self.add_cat_button.clicked.connect(self.add_expense)  # TODO: вызвать метод добавления

        self.del_cat_button = QPushButton('Удалить')
        self.del_cat_button.clicked.connect(self.add_expense)  # TODO: вызвать метод удаления

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(self.add_cat_button)
        layout_btn.addWidget(self.del_cat_button)

        layout = QVBoxLayout()
        layout.addWidget(self.category_edit_view)
        self.category_edit_view.resizeColumnsToContents()
        self.category_edit_view.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        layout.addLayout(line_layout)
        layout.addLayout(layout_btn)

        self.setLayout(layout)

        # Подключение к сигналу
        self.category_edit_view.cellClicked.connect(self.on_cell_clicked)

    def on_cell_clicked(self, row, column):
        category_name = self.category_edit_view.item(row, column).text()
        parent_category_name = ""
        if self.category_edit_view.item(row, column + 1) is not None:
            parent_category_name = self.category_edit_view.item(row, column + 1).text()
        self.cat_edit.setText(category_name)
        self.sub_cat_edit.setText(parent_category_name)
        

    def display_categories(self, categories: List[Category], category_repo):
        self.category_edit_view.setRowCount(len(categories))
        self.category_edit_view.setColumnCount(2)

        for i, category in enumerate(categories):
            name_item = QTableWidgetItem(category.name)
            self.category_edit_view.setItem(i, 0, name_item)

            if category.parent is not None:
                sub_item = QTableWidgetItem("{}".format(category_repo.get(category.parent).name))
                self.category_edit_view.setItem(i, 1, sub_item)

            self.category_edit_view.resizeColumnsToContents()
            self.category_edit_view.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
            self.category_edit_view.setMaximumHeight(self.category_edit_view.rowHeight(1) * 6)

# TODO: посмотреть на реализацию и переделать реализацию
# TODO: прописать функциональность
