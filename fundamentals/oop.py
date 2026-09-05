import random 



# ============================Sample Class and how to creat object ============================= #
# Example of how to create a class in python 
class Person: 
    # class attribute 
    hobbies = ["Reading", "Gaming", "Coding", "Cooking", "Swimming", "Drawing", "Photography", "Painting", "Singing", "Dancing", "Hiking", "Gardening", "Traveling", "Writing", "Cycling", "Meditation", "Yoga", "Movie Watching", "Music", "Knitting"]

    #constructor 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
    
    def person_details(self): 
        hobby = random.choice(self.hobbies)
        return f"Name: {self.name}\nAge: {self.age}\nHobby: {hobby}"
    
p = Person("Sujon", 43)
print(p.person_details())


''''
Let us assume that our favourite person in programming world is called PAIE. 
Yes, modern object oriented programming is built on the idea of PAIE.
P = Polymorphism 
A = Abstraction 
I = Inheritance 
E = Encapsulation
Below you can explore each of them in details. 
'''


# ============================Polymorphism============================= #

'''
P = Polymorphism: When you think of this concept, think of yourself. 
You are same person, but you have different behaviour as you grow as a personl.
This concept exactly the same. It means same method, different behavior. 
'''
class Dog: 
    def sound(self): 
        return "Woof Woof, I Like Eating Bone"

class Cat: 
    def sound(self):
        return "Meow Meow, I Like to Eat Fish"

# pass an animal object such as dog or cat in this case 
def make_sound(animal): 
    print(animal.sound())

make_sound(Dog())
make_sound(Cat())

# ============================Abstraction============================= #


''' 
A = Abstraction: Hide complexity, show only necessary details. Often we create interface
and define simple methods that other class implement and handle their own complexity. 
We can then use this interface to complete complex task without having to worry about too much 
details about how they were implemented. In python we need to import to create abstract classes. 
We need to import abc(abstract base class) to use abstractmethod. 
abstractmethod = Marks which methods MUST be implemented by child classes. 
ABC prevents instantiation
'''
# This is abstraction, where we define what method must exist without implementing them 
from abc import ABC, abstractmethod
class PaymentMethod(ABC): 
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass

# Concrete implementation of the PaymentMethod interface 
class CreditCard(PaymentMethod): 
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"Paid: {amount} via Credit Card number {self.card_number}"
    
    def refund(self, amount):
        return f"Refunded: ${amount} to the card number {self.card_number}"


class MasterCard(PaymentMethod): 
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"Paid: {amount} via Master Card number {self.card_number}"
    
    def refund(self, amount):
        return f"Refunded: {amount} to the card number {self.card_number}"


class Visa(PaymentMethod): 
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"Paid: {amount} via Visa Card number {self.card_number}"
    
    def refund(self, amount):
        return f"Refunded: {amount} to the card number {self.card_number}"

# Use case of abstraction: Now we can use any payment method without caring about details
def checkout(payment: PaymentMethod, amount: int): 
    print(payment.pay(amount))
    print(payment.refund(amount))

# Same code will now work for all type of payment
checkout(CreditCard("1234-5678-9012"), 100)
checkout(MasterCard("1234-5678-9012"), 399)
checkout(Visa("1234-5678-9012"), 566)

# ==========================Inheritance=========================== #

'''
I = Inheritance. Inherit behaviour from parent class. 
''' 
class Student(Person): 
    def __init__(self, name, age, student_id, grade): 
        super().__init__(name, age) # name and age inheritance from parent class
        self.student_id = student_id 
        self.grade = grade 

    # Override parent method 
    def person_details(self): 
        hobby = random.choice(self.hobbies)
        return f"Name: {self.name}\nAge: {self.age}\nHobby: {hobby}\nStudent Id: {self.student_id}\nGrade: {self.grade}"

def main(): 
    p = Person("Sujon", 33)
    print(p.person_details())
    s = Student("Alice", 20, "S123", "A")
    print(s.person_details())

main()    


# ==========================Encapsulation=========================== #

'''
E = Encapsulation: Hide internal details, control access what user can and can not see. 
'''

class BankAccount:
    def __init__(self, balance): 
        # private instance attribute, can not be access directly by calling it
        self.__balance = balance 
    
    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount
        else: 
            print("Invalid amount, try again")
    
    def get_balance(self): 
        return self.__balance

account = BankAccount(700)
# with encapsulation we ensure no one can set balance to anything 
# can not do account.balance = -700
print(b.get_balance())