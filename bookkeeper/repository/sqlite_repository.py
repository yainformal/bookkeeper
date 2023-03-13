"""
Модуль описывает репозиторий использующий в качестве СУБД SQLite
"""
import sqlite3 as sql
from inspect import get_annotations
from typing import Any, List
from abc import ABC
from bookkeeper.repository.abstract_repository import AbstractRepository, T
from PySide6.QtCore import QObject, Signal


# noinspection PyMethodParameters,PyUnreachableCode
class SQliteRepository(AbstractRepository[T], QObject):
    repo_changed = Signal(list)
    """
   Репозиторий хранящий данные приложения с использованием СУБД SQLite.
    """

    def __init__(self, db_file: str, cls: type) -> None:
        super().__init__()
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.class_name = cls
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop('pk')

        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            field = ', '.join([field for field in self.fields.keys()])
            primary_key = 'pk INTEGER PRIMARY KEY'
            foreign_key = 'FOREIGN KEY (category) REFERENCES category(pk)'

            if self.table_name != 'category':
                create_table = f'CREATE TABLE IF NOT EXISTS {self.table_name} ({field}, {primary_key}, {foreign_key})'
                cur.execute(create_table)

            else:
                create_table = f'CREATE TABLE IF NOT EXISTS {self.table_name} ({field}, {primary_key})'
                cur.execute(create_table)
        con.close()

    def add(self, obj: T) -> int:
        names = ', '.join(self.fields.keys())
        promote = ', '.join('?' * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'PRAGMA foreign_keys = ON')
            cur.execute(f'INSERT INTO {self.table_name} ({names}) VALUES ({promote})', values)
            obj.pk = cur.lastrowid
        con.close()
        self.repo_changed.emit(self.get_all())
        return obj.pk

    def get(self, pk: int) -> T | None:
        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_name} WHERE pk = {pk}')
            res = [cur.fetchone()]
        con.close()
        row = [self.class_name(*obj) for obj in res][0]
        return row

    def get_all(self, where: dict[str, Any] | None = None) -> list[list[Any]] | list[Any]:
        if where is None:
            with sql.connect(self.db_file) as con:
                cur = con.cursor()
                cur.execute(f'SELECT * FROM {self.table_name}')
                res = cur.fetchall()
            con.close()
            return [self.class_name(*obj) for obj in res]

        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            where_attr = ', '.join('{} = "{}"'.format(key, val) for key, val in where.items())
            # TODO: подумать как достать строку и избавиться от ""
            cur.execute(f'SELECT * FROM {self.table_name} WHERE {where_attr}')
            res = cur.fetchall()
        con.close()
        return [self.class_name(*obj) for obj in res]

    def delete(self, pk: int) -> None:
        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM {self.table_name} WHERE pk = {pk}")
        con.close()
        self.repo_changed.emit(self.get_all())

    def update(self, obj: T) -> None:
        if obj.pk == 0:
            raise ValueError('attempt to update object with unknown primary key')

        with sql.connect(self.db_file) as con:
            cur = con.cursor()
            update_obj = ', '.join('{} = {}'.format(key, val)
                                   for key, val in obj.__dict__.items()
                                   )
            cur.execute(f"UPDATE {self.table_name} SET {update_obj} WHERE pk = {obj.pk}")
        con.close()
        self.repo_changed.emit(self.get_all())
