import pytest
# os is Python's built-in module for talking to the operating system for example environment variables, files and folders, paths.
import os 
import logging # debugging 

# 1. Assertions: Check whether all given condition is true. If true pass, else fail 
def test_input_and_expected_output():
    assert 29 + 3 == 32
    assert 34 < 39
    assert True == True 
    assert "cricket" in {"football", "cricket", "hiking", "music"}
    assert 89 > 34
    assert 0 != 1
    assert all([1, 1, 1, 1])
    assert any([0, 0, 0, 1])

# 2. Raising exceptions
def divide(a, b):
    if a >= float('inf') or a <= float('-inf'):
        raise ValueError("a value can not be more than max inf or less than -inf") 
    if b >= float('inf') or b <= float('-inf'):
        raise ValueError("b value can not be more than max inf or less than -inf") 
    if b == 0:
        raise ZeroDivisionError("can not be divided by zero") 
    try:
        return a / b
    except Exception as e:
        print(e)
        
def test_divide():
    assert divide(5, 2) == 2.5

def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError) as err_info:
        divide(10, 0)
    print(err_info.value)

def test_divide_by_too_large_number():
    with pytest.raises(ValueError):
        divide(float('inf'), 22222222222222222222222222222223)
        divide(float('-inf'), 22222222222222222222222222222223)
        divide(4444444433333332, float('inf'))
        divide(4444444433333332, float('-inf'))

"""
3. Fixtures
A fixture is a function decorated with @pytest.fixture that prepares data or
resources a test needs. A test requests a fixture by naming it as a parameter,
and pytest runs the fixture first and passes its return value in.
Code after yield runs once the test finishes, which handles cleanup.
"""
class User:
    def __init__(self, name:str, age:int):
        self.name = name 
        self.age = age 

@pytest.fixture
def create_sample_user():
    user = User("Mike", 44)
    return {"name": user.name, "age": user.age}

def test_user_details(create_sample_user):
    assert create_sample_user["name"] == "Mike"
    assert create_sample_user["age"] == 44

@pytest.fixture 
def open_text_file(tmp_path):
    file_path = tmp_path / "cat.txt"
    file_handle = open(file_path, "w")
    # yield gives the open file to the test, pauses the fixture while the test runs, 
    # and then carries on to file_handle.close() when the test finishes.
    yield file_handle
    file_handle.close()

def test_write_to_file(open_text_file):
    print(open_text_file.name)
    open_text_file.write("Meow\n")
    open_text_file.write("Mika")
    assert not open_text_file.closed 

"""
4. Builtin fixtures
Fixtures provided by pytest that need no definition.
- tmp_path: temporary folder created for each test
- capsys: captures print output
- monkeypatch: temporarily changes environment variables, attributes or functions
- caplog: captures logging output
- request: information about the running test, including fixture params
"""
# tmp_path: temporary folder created for each test
# capsys: captures print output
# monkeypatch: temporarily changes environment variables, attributes or functions
# caplog: captures logging output
# request: request: gives a fixture access to request.param, the current value from @pytest.fixture(params=[...]), so the fixture runs once per value




# 5. Parametrize
# 6. Markers
# 7. Test strategy
# 8. Configuration files
# 9. Coverage

"""
# 10. tox and CI
# - tox runs your test suite in several isolated environments, for example Python 3.10, 3.11 and 3.12
# - CI (Continuous Integration) runs tests automatically on a server, such as GitHub Actions, on every push or open a pull request.
"""

"""
11. Testing scripts
Testing a standalone .py file that is not part of an installed package.
- Import the script into tests using pythonpath in pytest.ini or pyproject.toml
- Keep logic in main() behind if __name__ == "__main__" so importing does not run it
- Run the script with subprocess and check its output
- Capture printed output with capsys
"""
# 12. Advanced parametrize
