from tests.ingredient_test_data import Ingredient, ingredient_dataset, i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16

def test_get_all_ingredient_dataset():
    assert ingredient_dataset().get_all() == [i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16]

def test_get_by_id_is_i_07():
    assert ingredient_dataset().get_by_id(4908) is i_07

def test_get_by_id_is_i_09():
    assert ingredient_dataset().get_by_id(4910) is i_09

def test_get_by_id_nonexistent_id():
    assert ingredient_dataset().get_by_id(9797) is None

def test_get_by_name_is_i_06():
    assert ingredient_dataset().get_by_name("Matcha Powder") is i_06

def test_get_by_name_is_i_10():
    assert ingredient_dataset().get_by_name("Whipped Cream") is i_10

def test_get_by_name_nonexistent_name():
    assert ingredient_dataset().get_by_name("Soy Milk") is None

def test_add_ingredient():
    i_17 = Ingredient(
        "Condensed Milk",
        12.99,
        50,
        "oz",
    )
    data = ingredient_dataset()
    data.add(i_17)
    assert data.get_by_id(4918) is i_17

def test_update_existing_ingredient():
    i_18 = Ingredient(
        "Strawberry Preserves",
        7.99,
        12,
        "oz",
    )
    data = ingredient_dataset()
    data.update(4917, i_18)
    assert data.get_by_name("Strawberry Preserves") and not data.get_by_name("Lavendar Syrup")

def test_update_nonexistent_ingredient():
    i_19 = Ingredient(
        "Sweet Potato Paste",
        12.65,
        17,
        "oz"
    )
    data = ingredient_dataset()
    assert data.update(9494, i_19) is None

def test_delete_existing_ingredient():
    assert ingredient_dataset().delete(4906)

def test_delete_nonexistent_ingredient():
    assert ingredient_dataset().delete(9393) is False