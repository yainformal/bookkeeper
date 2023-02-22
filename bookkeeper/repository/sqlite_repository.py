"""
Модуль описывает репозиторий использующий в качестве СУБД SQLite
"""
from abc import ABC

from bookkeeper.repository.abstract_repository import AbstractRepository, T

from itertools import count
from typing import Any
from inspect import get_annotations
import sqlite3 as sql


# noinspection PyMethodParameters
class SQliteRepository(AbstractRepository[T], ABC):
    """
   Репозиторий хранящий данные приложения с использованием СУБД SQLite.
    """

    def __init__(db_file: str, self, cls: type) -> None:
        db_file.table_name = None
        db_file.fields = None
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop('pk')

    def add(self, obj: T) -> int:
        names = ', '.join(self.fields.keys())
        p = ', '.join('?' * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]

        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(f'INSERT INTO {self.table_name} ({names}) VALUES ({p})', values)
            obj.pk = cur.lastrowid
        con.close()
        return obj.pk

    def get(self, pk: int) -> T | None:
        pass

    # TODO: добавить функцию get с поддержкой необходимых типов

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        pass # TODO: Реализовать метод get all



    def delete(self, pk: int) -> None:
        self.fields.pop(pk)

    def update(self, obj: T) -> None:
        if obj.pk == 0:
            raise ValueError('attempt to update object with unknown primary key')

        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f"UPDATE {self.table_name} SET ({obj.pk}) = ({obj})")
        con.close()

