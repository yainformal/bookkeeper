"""
Модель бюджета
"""

from dataclasses import dataclass

@dataclass()
class Budget:
    period: str
    category: int
    amount: int
    pk: int = 0
"""
period - срок
category - категория расходов
limit - установленный по категории лимит
pk - id записи в БД 
"""


