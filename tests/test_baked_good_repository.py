from baked_good_test_data import baked_goods_dataset, bg_00, bg_01, bg_02, bg_03, bg_04, bg_05, bg_06, bg_07, bg_08, bg_09

def test_get_all_baked_goods_dataset():
    assert baked_goods_dataset().get_all() == [bg_00, bg_01, bg_02, bg_03, bg_04, bg_05, bg_06, bg_07, bg_08, bg_09]

def test_get_by_name_is_bg_00_baked_goods_dataset():
    assert baked_goods_dataset().get_by_name("Chocolate Croissant") == bg_00

def test_get_by_name_is_bg_09_baked_goods_dataset():
    assert baked_goods_dataset().get_by_name("Coconut Macaron") == bg_09

def test_get_by_name_is_none_baked_goods_dataset():
    assert baked_goods_dataset().get_by_name("Mooncake") is None