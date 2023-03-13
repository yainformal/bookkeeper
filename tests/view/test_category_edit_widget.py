import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtTest import QTest
from bookkeeper.view.category_edit_widget import CategoryEditWidget

from bookkeeper.models.category import Category

@pytest.fixture()
def test_display_categories():
    # Создаем список категорий, которые будем отображать
    categories = [
        Category(name='Категория 1'),
        Category(name='Категория 2', parent=1),
        Category(name='Категория 3'),
    ]

    # Создаем виджет и вызываем метод для отображения категорий
    app = QApplication([])
    widget = CategoryEditWidget()
    widget.display_categories(categories, None)

    # Проверяем, что категории отображены в таблице
    assert widget.category_edit_view.rowCount() == len(categories)

    # Проверяем, что для каждой категории отображается ее имя
    for i, category in enumerate(categories):
        assert widget.category_edit_view.item(i, 0).text() == category.name

    # Проверяем, что для категорий с родительской категорией отображается ее имя
    assert widget.category_edit_view.item(1, 1).text() == categories[0].name

    # Проверяем, что для категорий без родительской категории не отображается имя родительской категории
    assert widget.category_edit_view.item(0, 1) is None

    # Очищаем ресурсы приложения
    del widget
    del app


def test_add_category(qtbot):
    # Создаем виджет и подключаем его к qtbot для эмуляции пользовательского взаимодействия
    widget = CategoryEditWidget()
    qtbot.addWidget(widget)

    # Создаем и устанавливаем значения для полей ввода
    cat_name = 'Категория 1'
    sub_cat_name = 'Родительская категория'
    widget.cat_edit.setText(cat_name)
    widget.sub_cat_edit.setText(sub_cat_name)

    # Эмулируем нажатие на кнопку "Добавить"
    with qtbot.waitSignal(widget.add_cat_button.clicked):
        QTest.mouseClick(widget.add_cat_button, Qt.LeftButton)

    # Проверяем, что метод для добавления категории был вызван с правильными аргументами
    assert widget.add_expense.call_args == ((cat_name, sub_cat_name),)

    # Очищаем ресурсы
    del widget



