from name_function import get_formatted_name
from name_function import get_formatted_name_including_middle_name


def test_first_and_last_name():
    formatted_name = get_formatted_name("janis", "jasper")
    assert formatted_name == "Janis Jasper"


def test_formatted_name_including_middle_name_with_no_middle_name_provided_should_pass():
    formatted_name = get_formatted_name_including_middle_name("janis", "jasper")
    assert formatted_name == "Janis Jasper"


def test_formatted_name_including_middle_name_provided_should_pass():
    formatted_name = get_formatted_name_including_middle_name(
        "janis", "jasper", "Karai"
    )
    assert formatted_name == "Janis Karai Jasper"
