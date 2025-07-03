# map, filter, zip and reduce
# map()
my_list = [1,2,3]
def multiply_by_2(item):   
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,my_list)))
print(my_list)


# Functional Programming
# new_list = []
# def multiply_by_2(li):
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by_2([1,2,3]))




# class PlayerCharacter(): #class
#     def __init__(self, name, age): #expected attributes or argument when the class is instantiated; 
#                               #self is to define the Class. In this sample it s the PlayerCharacter
#         self.name = name #attributes or arguments later in the instatntiation
#         self.age = age
        
#     def run(self):
#         print('run')
#         return 'done'
        
# player1 = PlayerCharacter('Jedi', 4)
# print(player1.name)
# print(player1.age)
# print(player1.run())





# class FirstClass(): #class
#     pass

# first_class1=FirstClass() #instantiate the FirstClass class
# print(type(first_class1))

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))







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
# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet(self):
#         super().greet()  # 👈 call Parent method
#         print("Hello from Child")

# c = Child()
# c.greet()
# ➤ Hello from Parent
# ➤ Hello from Child


# end of Inheritance





    

    