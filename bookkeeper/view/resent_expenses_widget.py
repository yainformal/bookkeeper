from inspect import get_annotations

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QVBoxLayout, QTableWidget, QWidget


class ResentExpensesWidget(QWidget):
    cls: type[T]

    def __init__(self, cls: type[T]) -> None:
        self.class_name = cls
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop('pk')
        super().__init__()

        self.setWindowTitle("Список расходов")

        self.model = QStandardItemModel()
        for idx, field in enumerate(self.fields.keys()):
            self.model.setHorizontalHeaderItem(idx, QStandardItem(field))

        self.table_view = QTableView(self)
        self.table_view.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        self.setLayout(layout)