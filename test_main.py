from main import get_report, get_all_values_by_field, get_complete_devices_list

test_report_dict = {
    "apple": [4.8, 4.5, 4.6, 4.3, 4.7, 4.9, 4.4, 4.6, 4.7, 4.5],
    "samsung": [4.6, 4.4, 4.7, 4.5, 4.3, 4.8, 4.4, 4.6, 4.5, 4.7],
    "xiaomi": [4.3, 4.4, 4.2, 4.5, 4.3, 4.6, 4.2, 4.4, 4.3, 4.5],
    "huawei": [4.5, 4.6, 4.4, 4.7, 4.3, 4.5, 4.6, 4.4, 4.5, 4.6],
    "google": [4.7, 4.8, 4.6, 4.9, 4.5, 4.7, 4.8, 4.6, 4.7, 4.8],
    "oneplus": [4.4, 4.5, 4.3, 4.6, 4.4, 4.7, 4.3, 4.5, 4.4, 4.6],
}

test_devices_list = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "iphone 14", "brand": "apple", "price": "899", "rating": "4.7"},
    {"name": "galaxy z flip", "brand": "samsung", "price": "999", "rating": "4.5"},
    {"name": "poco x5", "brand": "xiaomi", "price": "299", "rating": "4.4"},
    {"name": "mate 50", "brand": "huawei", "price": "799", "rating": "4.6"},
    {"name": "pixel 8", "brand": "google", "price": "699", "rating": "4.8"},
]


def test_get_report():
    assert get_report("average", test_report_dict) == [
        ("google", 4.71),
        ("apple", 4.6),
        ("samsung", 4.55),
        ("huawei", 4.51),
        ("oneplus", 4.47),
        ("xiaomi", 4.37),
    ]


def test_get_all_values_by_field_rating():
    result = get_all_values_by_field("rating", test_devices_list)
    expected = {
        "apple": [4.9, 4.7],
        "samsung": [4.8, 4.5],
        "xiaomi": [4.6, 4.4],
        "huawei": [4.6],
        "google": [4.8],
    }
    assert result == expected


def test_get_all_values_by_field_price():
    result = get_all_values_by_field("price", test_devices_list)
    expected = {
        "apple": [999.0, 899.0],
        "samsung": [1199.0, 999.0],
        "xiaomi": [199.0, 299.0],
        "huawei": [799.0],
        "google": [699.0],
    }
    assert result == expected
