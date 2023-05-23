import pandas as pd
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load(source_path)

    def load(self, source_path: str):
        data = pd.read_csv(source_path).itertuples(index=False)

        for row in data:
            name, price, ingredient, amount = row
            instancia = Dish(name, float(price))

            if self.novo_d(instancia):
                self.adiciona_igredientes(instancia, ingredient, amount)
                self.dishes.add(instancia)
            else:
                existing_dish = self.pega(instancia)
                self.adiciona_igredientes(existing_dish, ingredient, amount)

    def novo_d(self, instancia: Dish) -> bool:
        return instancia not in self.dishes

    def adiciona_igredientes(self, dish:
                             Dish, ingredient: str, amount: int):
        dish.add_ingredient_dependency(Ingredient(ingredient), int(amount))

    def pega(self, instancia: Dish) -> Dish:
        for dish in self.dishes:
            if dish == instancia:
                return dish
