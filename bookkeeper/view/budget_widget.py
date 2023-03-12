from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QVBoxLayout, QLabel, QWidget


class BudgetView(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Бюджет")
        self.budget_lable = QLabel('Бюджет')

        # Create the table widget with 4 columns and 3 rows
        self.table = QTableWidget(3, 4)
        self.table.setHorizontalHeaderLabels(['Период', 'Лимит', 'Расходы', 'Остаток'])

        # Populate the table with data
        self.table.setItem(0, 0, QTableWidgetItem('День'))
        self.table.setItem(0, 1, QTableWidgetItem('1000'))
        self.table.setItem(0, 2, QTableWidgetItem('500'))
        self.table.setItem(0, 3, QTableWidgetItem('500'))

        self.table.setItem(1, 0, QTableWidgetItem('Неделя'))
        self.table.setItem(1, 1, QTableWidgetItem('7000'))
        self.table.setItem(1, 2, QTableWidgetItem('4000'))
        self.table.setItem(1, 3, QTableWidgetItem('3000'))

        self.table.setItem(2, 0, QTableWidgetItem('Месяц'))
        self.table.setItem(2, 1, QTableWidgetItem('30000'))
        self.table.setItem(2, 2, QTableWidgetItem('20000'))
        self.table.setItem(2, 3, QTableWidgetItem('10000'))

        layout = QVBoxLayout()
        layout.addWidget(self.budget_lable)
        layout.addWidget(self.table)
        self.table.resizeColumnsToContents()
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)

        self.table.itemChanged.connect(self.update_data)

        self.setLayout(layout)

    def update_data(self, item):

        if item.column() in (1, 2):
            income_item = self.table.item(item.row(), 1)
            expense_item = self.table.item(item.row(), 2)
            if income_item is not None and expense_item is not None:
                income = int(income_item.text())
                expense = int(expense_item.text())
                balance = income - expense
                balance_item = self.table.item(item.row(), 3)
                if balance_item is None:
                    balance_item = QTableWidgetItem()
                    self.table.setItem(item.row(), 3, balance_item)
                balance_item.setText(str(balance))
