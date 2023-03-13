from datetime import datetime
from typing import List

from PySide6 import QtCore
from PySide6.QtCore import Slot
from setuptools.config._validate_pyproject import ValidationError

from bookkeeper.view.abstract_view import AbstractView
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.models.budget import Budget
from bookkeeper.repository.sqlite_repository import SQliteRepository
from bookkeeper.view.toggle_window import toggle_window


class Bookkeeper:
    repo_changed = QtCore.Signal(list)

    def __init__(self, view: AbstractView, resent_expense_view: AbstractView, category_edit_view: AbstractView,
                 exp_repo, category_repo):
        self.view = view
        self.resent_expense_view = resent_expense_view
        self.category_edit_view = category_edit_view

        self.exp_repo = exp_repo
        self.category_repo = category_repo
        # self.cats = self.category_repo.get_all()
        # self.view.register_cat_modifier(self.modify_cat)

        # Вычитываем передаваемые сигналы с кнопки add_button виджета add_expense
        self.view.add_button.clicked.connect(self.add_expenses)
        self.view.add_button.clicked.connect(self.clear_add_expense_fields)

        self.view.edit_button.clicked.connect(
            lambda checked: toggle_window(self.category_edit_view))

        # подписываемся на изменения в блоке расходы
        self.exp_repo.repo_changed.connect(self.listen_update_exp)

        # Получаем текущий список расходов и отображаем его в представлении
        expenses = self.exp_repo.get_all()
        self.resent_expense_view.display_expenses(expenses, self.category_repo)

        # Подписываемся чтение в репозитории категории. Репозиторий с категориями передаем для отображения данных.
        self.category_repo.repo_changed.connect(self.listen_update_cat)
        categories = self.category_repo.get_all()
        self.category_edit_view.display_categories(categories, self.category_repo)

    # онлайн обновление таблицы с категориями
    def listen_update_cat(self) -> List[Category]:
        categories = self.category_repo.get_all()
        self.category_edit_view.display_categories(categories, self.category_repo)

    # функция отвечает за онлайн обновление таблицы расходов
    def listen_update_exp(self) -> List[Expense]:
        expenses = self.exp_repo.get_all()
        self.resent_expense_view.display_expenses(expenses, self.category_repo)

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
