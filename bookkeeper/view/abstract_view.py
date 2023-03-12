from typing import Protocol

from bookkeeper.models.category import Category


class AbstractView(Protocol):

    def set_category_list(self):
        pass

    def register_cat_modifier(self):
        pass


    
    
