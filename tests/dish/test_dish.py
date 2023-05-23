from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    tomato = Ingredient("Tomato")
    cheese = Ingredient("Cheese")
    onion = Ingredient("Onion")
    lettuce = Ingredient("Lettuce")
    chicken = Ingredient("Chicken")
    pasta = Ingredient("Pasta")

    spaghetti = create("Spaghetti", 10.99, {
        tomato: 2,
        cheese: 1,
        onion: 1
    })

    salad = create("Salad", 8.99, {
        lettuce: 1,
        tomato: 2,
        onion: 1
    })

    grilled = create("Grilled Chicken", 12.99, {
        chicken: 1,
        lettuce: 1,
        tomato: 1
    })

    lasagna = create("Lasagna", 15.99, {
        pasta: 3,
        tomato: 2,
        cheese: 2
    })

    dish_properties(spaghetti, "Spaghetti", 10.99)
    dish_properties(salad, "Salad", 8.99)
    dish_properties(grilled, "Grilled Chicken", 12.99)
    dish_properties(lasagna, "Lasagna", 15.99)

    assertrepr(spaghetti, "Dish('Spaghetti', R$10.99)")
    assertrepr(salad, "Dish('Salad', R$8.99)")
    assertrepr(grilled, "Dish('Grilled Chicken', R$12.99)")
    assertrepr(lasagna, "Dish('Lasagna', R$15.99)")

    asserthashequality(spaghetti, spaghetti, True)
    asserthashequality(spaghetti, salad, False)

    assertdish_equality(spaghetti, spaghetti, True)
    assertdish_equality(spaghetti, salad, False)

    assertrestrictions(spaghetti, set())
    assertrestrictions(salad, set())
    assertrestrictions(grilled, set())
    assertrestrictions(lasagna, set())

    assertingredients(spaghetti, {tomato, cheese, onion})
    assertingredients(salad, {lettuce, tomato, onion})
    assertingredients(grilled, {chicken, lettuce, tomato})
    assertingredients(lasagna, {pasta, tomato, cheese})

    assert_invalid_creation("Spaghetti", "10.99", TypeError)
    assert_invalid_creation("Salad", -5.0, ValueError)


def create(name, price, recipe):
    dish = Dish(name, price)
    for ingredient, quantity in recipe.items():
        dish.add_ingredient_dependency(ingredient, quantity)
    return dish


def dish_properties(dish, expected_name, expected_price):
    assert dish.name == expected_name
    assert dish.price == expected_price


def assertrepr(dish, expected_repr):
    assert repr(dish) == expected_repr


def asserthashequality(dish11, dish22, expected_result):
    assert (hash(dish11) == hash(dish22)) == expected_result


def assertdish_equality(dish11, dish22, expected_result):
    assert (dish11 == dish22) == expected_result


def assertrestrictions(dish, expected_restrictions):
    assert dish.get_restrictions() == expected_restrictions


def assertingredients(dish, expected_ingredients):
    assert dish.get_ingredients() == expected_ingredients


def assert_invalid_creation(name, price, expected_exception):
    with pytest.raises(expected_exception):
        Dish(name, price)


test_dish()
