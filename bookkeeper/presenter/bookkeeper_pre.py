from datetime import datetime

from setuptools.config._validate_pyproject import ValidationError

from bookkeeper.view.abstract_view import AbstractView
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.models.budget import Budget
from bookkeeper.repository.sqlite_repository import SQliteRepository


class Bookkeeper:
    def __init__(self, view: AbstractView, exp_repo, category_repo):
        self.view = view
        # self.category_repo = category_repo.get(Category)
        self.exp_repo = exp_repo
        self.category_repo = category_repo
        # self.cats = self.category_repo.get_all()
        # self.view.register_cat_modifier(self.modify_cat)

        # Вычитываем передаваемые сигналы с кнопки add_button виджета add_expense
        self.view.add_button.clicked.connect(self.add_expenses)
        self.view.add_button.clicked.connect(self.clear_add_expense_fields)

    def modify_cat(self, cat: Category) -> None:
        pass
        # self.category_repo.update(cat)
        # self.view.set_category_list()

    def add_cat(self, name, parent):
        if name in [c.name for c in self.cats]:
            raise ValidationError(
                f'Категория {name} уже существует')

        cat = Category(name, parent)
        self.category_repo.add(cat)
        self.cats.append(cat)
        self.view.set_category_list()

    def del_cat(self):
        pass

    def add_expenses(self):
        expense_date = self.view.datetime_edit.text()
        amount = self.view.amount_edit.text()
        name = self.view.category_edit.currentText()
        cat = self.category_repo.get_all({'name': name})[0]
        comment = self.view.comment_edit.text()
        added_date = datetime.now()
        expense = Expense(int(amount), cat.pk, expense_date, added_date, comment)
        self.exp_repo.add(expense)
        print(expense)  # TODO: удалить после отладки

    def del_expenses(self, ):
        pass

    def update_expenses(self):
        pass

    def clear_add_expense_fields(self):
        self.view.amount_edit.clear()
        self.view.comment_edit.clear()
