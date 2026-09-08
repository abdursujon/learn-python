from city_functions import formatted_city_and_country_name

def test_city_country_return_correct_string():
    formatted_name = formatted_city_and_country_name("sanTiago", "chile")
    assert formatted_name == "Santiago Chile"
