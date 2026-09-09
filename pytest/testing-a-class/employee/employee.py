class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name 
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        if amount > self.annual_salary:
            return "Raise can't be more than annual_salary"
        else: 
            self.annual_salary = self.annual_salary + amount
        return self.annual_salary

e = Employee("Abdur", "Sujon", 30000)
print(e.give_raise())
print(e.give_raise(8000))