"""
Тесты для модели бюджета
"""
from dataclasses import asdict

import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.budget import Budget

@pytest.fixture
def repo():
    return MemoryRepository()

def test_create_object():
    c = Budget('month',2,100)
    assert c.period == 'month'
    assert c.category == 2
    assert c.pk == 0
    assert c.amount == 100

    c = Budget(period='month', category=2,amount=100,pk=3)
    assert c.period == 'month'
    assert c.category == 2
    assert c.amount == 100
    assert c.pk == 3

def test_eq():
    """
    class should implement __eq__ method
    """
    c1 = Budget(period='name', category=1,amount=100,pk=2)
    c2 = Budget(period='name', category=1,amount=100, pk=2)
    assert c1 == c2


def test_eq():
    """
    class should implement __eq__ method
    """
    c1 = Budget(period='name', category=1,amount=100,pk=2)
    c2 = Budget(period='day', category=1,amount=10, pk=2)
    assert c1 != c2

def test_can_add_to_repo(repo):
    e = Budget('day',1,4000)
    pk = repo.add(e)
    assert e.pk == pk

def test_budget_dict_conversion():
    budget = Budget(period="2022-01", category=1, amount=100)
    budget_dict = asdict(budget)
    assert budget_dict == {"period": "2022-01", "category": 1, "amount": 100, "pk": 0}

