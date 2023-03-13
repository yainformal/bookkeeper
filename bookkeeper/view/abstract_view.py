"""
Класс реализует методы абстрактного интерфейса
"""

from typing import Protocol



class AbstractView(Protocol):

    def __init__(self):
        self.table_view = None
        self.expense_del_button = None
        self.table_widget = None
        self.cellClicked = None
        self.edit_button = None
        self.add_button = None
        self.amount_edit = None

    def set_category_list(self):
        pass

    def register_cat_modifier(self):
        pass

    def datetime_edit(self):
        pass

    def category_edit(self):
        """
        Функция работы с полем выбора категорий
        @return:
        @rtype:
        """
        pass

    def comment_edit(self) -> object:
        """
        Возвращает значения поля комментарий
        @return:
        @rtype:
        """
        pass

    def display_expenses(self, expenses):
        """
        Отобращение данных о расходах в режиме онлайн
        @param expenses:
        @type expenses:
        @return:
        @rtype:
        """
        pass

    def display_categories(self, categories, category_repo):
        """
        Отображение данных из репозитория категории в режиме онлайн
        @param categories:
        @type categories:
        @param category_repo:
        @type category_repo:
        @return:
        @rtype:
        """
        pass