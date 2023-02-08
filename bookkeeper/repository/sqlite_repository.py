"""
Модуль описывает репозиторий использующий в качестве СУБД SQLite
"""

from bookkeeper.repository.abstract_repository import AbstractRepository, T

from itertools import count
from typing import Any
from inspect import get_annotations
import sqlite3 as sql


class SQliteRepository(AbstractRepository[T]):
    """
   Репозиторий хранящий данные приложения с использованием СУБД SQLite.
    """

    def __init__(db_file: str, self, cls: type) -> None:
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

    def delete(self, obj: T) -> None:
        self.fields.pop(pk)
