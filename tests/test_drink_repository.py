from tests.drink_test_data import Drink, drink_dataset, d_00, d_01, d_02, d_03, d_04, d_05, d_06, d_07, d_08, d_09, i_00, i_01, i_02, i_03, i_04, i_05, i_06, i_07, i_08, i_09, i_10, i_11, i_12, i_13, i_14, i_15, i_16

def test_get_all_drink_dataset():
    assert drink_dataset().get_all() == [d_00, d_01, d_02, d_03, d_04, d_05, d_06, d_07, d_08, d_09]

def test_get_by_id_is_d_00():
    assert drink_dataset().get_by_id(1301) is d_00

def test_get_by_id_is_d_09():
    assert drink_dataset().get_by_id(1310) is d_09

def test_get_by_id_nonexistent_drink():
    assert drink_dataset().get_by_id(9696) is None

def test_get_by_name_is_d_01():
    assert drink_dataset().get_by_name("Vanilla Latte") is d_01

def test_get_by_name_is_d_08():
    assert drink_dataset().get_by_name("Iced Americano") is d_08

def test_get_by_name_nonexistent_drink():
    assert drink_dataset().get_by_name(9797) is None

def test_add_drink():
    d_10 = Drink(
        "Iced Vanilla Cold Brew",
        [i_02, i_03, i_05, i_09],
        0.85,
        2.53,
        3.00,
    )
    data = drink_dataset()
    data.add(d_10)
    assert data.get_by_id(1311) is d_10