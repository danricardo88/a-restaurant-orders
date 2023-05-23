import pandas as pd
from src.services.inventory_control import InventoryMapping
from src.services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        dishes = self.menu_data.dishes
        if restriction is None:
            filtered_dishes = dishes
        else:
            filtered_dishes = [
                dish
                for dish in dishes
                if restriction not in dish.get_restrictions()
            ]

        menu = pd.DataFrame(
            columns=['dish_name', 'ingredients', 'price', 'restrictions'])
        for dish in filtered_dishes:
            ingredients = ", ".join([str(ingredient)
                                    for ingredient
                                    in dish.get_ingredients()])
            restrictions = ", ".join([str(restriction)
                                     for restriction
                                     in dish.get_restrictions()])
            menu = menu.append({
                'dish_name': dish.name,
                'ingredients': ingredients,
                'price': dish.price,
                'restrictions': restrictions
            }, ignore_index=True)

        return menu

    def compare_dishes(self, given_dish, expected_dish):
        return (
            given_dish['dish_name'] == expected_dish.name
            and given_dish['ingredients'] == ", ".join(
                [str(ingredient)
                 for ingredient
                 in expected_dish.get_ingredients(

                )])
            and given_dish['price'] == expected_dish.price
            and given_dish['restrictions'] == ", ".join(
                [str(restriction)
                 for restriction
                 in expected_dish.get_restrictions(

                )])
        )
