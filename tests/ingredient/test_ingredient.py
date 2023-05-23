from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Test constructor
    ingredient = Ingredient("carne")
    assert_ingredient(ingredient, "carne", [
                      Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED])

    assert_repr(ingredient, "Ingredient('carne')")

    ingredient21 = Ingredient("carne")
    ingredient32 = Ingredient("abóbora")
    assert_ingredient_equality(ingredient, ingredient21, True)
    assert_ingredient_equality(ingredient, ingredient32, False)

    assert_hash_equality(ingredient, ingredient21, True)
    assert_hash_equality(ingredient, ingredient32, False)


def assert_ingredient(ingredient, expected_name, expected_restrictions):
    assert ingredient.name == expected_name
    assert ingredient.restrictions == set(expected_restrictions)


def assert_repr(ingredient, expected_repr):
    assert repr(ingredient) == expected_repr


def assert_ingredient_equality(ingredient11, ingredient21, expected_result):
    assert (ingredient11 == ingredient21) == expected_result


def assert_hash_equality(ingredient11, ingredient21, expected_result):
    assert (hash(ingredient11) == hash(ingredient21)) == expected_result
