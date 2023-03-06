"""
Простой тестовый скрипт для терминала
"""

from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.models.budget import Budget
from bookkeeper.repository.sqlite_repository import SQliteRepository
#from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.utils import read_tree


#cat_repo = MemoryRepository[Category]()
#exp_repo = MemoryRepository[Expense]()

cat_repo = SQliteRepository[Category]('data_test.db', Category)
exp_repo = SQliteRepository[Expense]('data_test.db', Expense)
bgt_repo = SQliteRepository[Budget]('data_test.db', Budget)


cats= '''
продукты                           
    мясо
        сырое мясо
        мясные продукты
    сладости
книги
одежда
'''.splitlines()

#Category.create_from_tree(read_tree(cats), cat_repo)


while True:
    try:
        cmd = input('Введите команду $> ')
    except EOFError:
        break
    if not cmd:
        continue
    if cmd == 'категории':
        print(*cat_repo.get_all(), sep='\n')
    elif cmd == 'расходы':
        print(*exp_repo.get_all(), sep='\n')
    elif cmd == 'бюджет':
        print("модель не описана")
    elif cmd[0].isdecimal():
        amount, name = cmd.split(maxsplit=1)
        try:
            cat = cat_repo.get_all({'name': name})[0]
        except IndexError:
            print(f'категория {name} не найдена')
            continue
        exp = Expense(int(amount), cat.pk)
        exp_repo.add(exp)
        print(exp)

