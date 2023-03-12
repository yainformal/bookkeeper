from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QTableWidget, QLineEdit, QLabel, QWidget, QHBoxLayout


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

        self.model = QStandardItemModel()

        self.view = QTableWidget(3, 2)
        self.view.setHorizontalHeaderLabels(['Категория', 'Родительская категория'])
        # self.view.setModel(self.model) # TODO: получение и отображение данных о категории

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
        layout.addWidget(self.view)
        self.view.resizeColumnsToContents()
        self.view.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        layout.addLayout(line_layout)
        layout.addLayout(layout_btn)

        self.setLayout(layout)


# TODO: посмотреть на реализацию и переделать реализацию
