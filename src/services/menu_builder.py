import pandas as pd
from typing import Optional

from src.services.inventory_control import InventoryMapping
from src.services.menu_data import MenuData
from src.models.ingredient import Restriction


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

    def get_main_menu(
        self, restriction: Optional[Restriction] = None
    ) -> pd.DataFrame:
        # Lista para armazenar os pratos do menu
        items = []

        # Itera sobre os pratos do menu
        for menu in self.menu_data.dishes:
            # Verifica se a restrição é None ou não
            # está presente nas restrições do prato
            if restriction is None or restriction not in menu.get_restrictions(

            ):
                # Cria um dicionário para armazenar as informações do prato
                item = {}
                # Preenche as chaves do dicionário
                # com os valores correspondentes do prato
                item['dish_name'] = menu.name
                item['price'] = menu.price
                item['ingredients'] = menu.get_ingredients()
                item['restrictions'] = menu.get_restrictions()
                # Adiciona o dicionário à lista de pratos
                items.append(item)

        # Cria um DataFrame a partir da lista de pratos
        # ta complicado... requi ruim da gota
        return pd.DataFrame(items)
