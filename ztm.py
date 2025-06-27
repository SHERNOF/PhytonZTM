# class Car:
#     has_gasoline = True # Class object attribute
#     def __init__(self, brand='Tesla', speed=1):
#         if brand == 'Kawasaki':
#             self.brand = brand #attributes
#             self.speed = speed
    
#     def accelerate(self):
#         # if Car.has_gasoline:
#         self.speed += 10
#         print(f'{self.brand} is now going {self.speed} km/h')

# my_car2 = Car('Kawasaki', 5)
# my_car = Car('Tesla', 20)

# my_car2.accelerate()
# my_car.accelerate()

# Encapsulation
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner         # public
#         self.__balance = balance   # private (name mangled)

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance
# # Usage
# acct = BankAccount("Alice", 1000)
# acct.deposit(200)
# acct.withdraw(500)
# print(acct.get_balance())        # ✅ 700
# print(acct.owner)                # ✅ accessible
# print(acct.__balance)            # ❌ AttributeError

# Encapsulation

# Abstraction
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
# dog = Dog()
# print(dog.make_sound())  # ➤ "Bark"

# animal = Animal()       # ❌ Error: can't instantiate abstract class

# The Animal class defines an interface (contract).

# The Dog and Cat classes implement the interface.

# You can’t create an object of an abstract class directly.

# iNHERITANCE
# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):  # 👈 Child inherits from Parent
#     def greet_child(self):
#         print("Hello from Child")

# # Inheritance Usage
# c = Child()
# c.greet()         # ➤ "Hello from Parent"  (inherited)
# c.greet_child()   # ➤ "Hello from Child"

# Overriding Parent CLass
# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet(self):  # 👈 overrides Parent's method
#         print("Hello from Child")


# c = Child()
# c.greet()   # ➤ "Hello from Child"



# 🧪 Using super() to Call Parent’s Method
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # 👈 call Parent method
        print("Hello from Child")

c = Child()
c.greet()
# ➤ Hello from Parent
# ➤ Hello from Child


# end of Inheritance





    

    