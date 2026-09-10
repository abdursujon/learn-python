from employee import Employee 
import pytest 

@pytest.fixture
def employee():
    employee = Employee("Abdur", "Sujon", 35000)
    return employee

def test_default_give_raise(employee):
    total_salary_after_raise = employee.give_raise()
    assert total_salary_after_raise == 40000

def test_invalid_raise(employee):
    total_salary_after_raise = employee.give_raise(50000)
    assert total_salary_after_raise == "Raise can't be more than annual_salary"

def test_valid_raise(employee):
    total_salary_after_raise = employee.give_raise(34999)
    assert total_salary_after_raise == 69999