import pytest
from PySide6.QtCore import QDate
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QLabel, QComboBox, QDateEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

from bookkeeper.repository.sqlite_repository import SQliteRepository
from bookkeeper.models.category import Category
from bookkeeper.view.add_expense_widget import AddExpenseWidget


path = '/Users/mikhailgubanov/Yandex.Disk.localized/bookkeeper/auto_test.db'
cat_repo = SQliteRepository[Category](path, Category)


@pytest.fixture
def add_expense_widget(qtbot):
    widget = AddExpenseWidget()
    qtbot.addWidget(widget)
    return widget


def test_add_expense_widget_controls(add_expense_widget):
    assert isinstance(add_expense_widget.amount_lable, QLabel)
    assert isinstance(add_expense_widget.amount_edit, QLineEdit)
    assert isinstance(add_expense_widget.category_lable, QLabel)
    assert isinstance(add_expense_widget.category_edit, QComboBox)
    assert isinstance(add_expense_widget.datetime_lable, QLabel)
    assert isinstance(add_expense_widget.datetime_edit, QDateEdit)
    assert isinstance(add_expense_widget.comment_lable, QLabel)
    assert isinstance(add_expense_widget.comment_edit, QLineEdit)
    assert isinstance(add_expense_widget.edit_button, QPushButton)
    assert isinstance(add_expense_widget.add_button, QPushButton)


def test_add_expense_widget_amount_validator(add_expense_widget):
    assert isinstance(add_expense_widget.amount_edit.validator(), QIntValidator)
    assert add_expense_widget.amount_edit.validator().bottom() == 0
    assert add_expense_widget.amount_edit.validator().top() == 100000000


def test_add_expense_widget_categories(add_expense_widget):
    categories = cat_repo.get_all()
    assert add_expense_widget.category_edit.count() == len(categories)
    for i in range(add_expense_widget.category_edit.count()):
        assert add_expense_widget.category_edit.itemText(i) == categories[i].name


def test_add_expense_widget_datetime_edit(add_expense_widget):
    assert add_expense_widget.datetime_edit.date() == QDate.currentDate()


def test_add_expense_widget_add_button(add_expense_widget):
    assert add_expense_widget.add_button.text() == "Добавить"


def test_add_expense_widget_layout(add_expense_widget):
    assert isinstance(add_expense_widget.layout(), QVBoxLayout)
    assert isinstance(add_expense_widget.amount_lable.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.amount_edit.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.category_lable.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.category_edit.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.datetime_lable.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.datetime_edit.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.comment_lable.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.comment_edit.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.edit_button.layout(), QHBoxLayout)
    assert isinstance(add_expense_widget.add_button.layout(), QHBoxLayout)
