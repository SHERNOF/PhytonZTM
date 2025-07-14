# Under the hood of generators
def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      next(iterator)
    except StopIteration:
      break
  
special_for([1,2,3])


# class MyGen:
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#     MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration

# gen = MyGen(1,100)
# for i in gen:
#     print(i)


# Generator

# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, *kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper
# @performance
# def long_time():
#     print('1')
#     for i in range(100000000): #it finishes after.
#         i*5

# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000000)): #it took longer.
#         i*5

# long_time()
# long_time2()


# def gen_function(num):
#     for i in range(num):
#         yield i * 2
        
# g = gen_function(100)
# next(g)
# next(g)
# print(next(g))


# for item in gen_function(100):
#     print(item)



























# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i)
        
#     return result

# my_list = make_list(100)
# print(my_list)
    

    


# Error Handling 3
# while True: #this allows the code to continue to run
#     try:
#         age = int(input('what is your age?'))
#         10/age
#         raise ValueError('Hey cut it our')
#     except ZeroDivisionError:
#         print('enter a number > 0')
#         break
#     else:
#         print('thank yoi')
#     finally:
#         print('ok, finally done')




# Error ahndling 2
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError): # way of writing multiple exceprions
#         print('oopps')
        
# print(sum('1',2))


# Error Handling
# while True: #this allows the code to continue to run
#     try:
#         age = int(input('what is your age?'))
#         10/age
#     except ZeroDivisionError:
#         print('enter a number > 0')
#     else:
#         print('thank yoi')
#         break #this makes the code to stop





# lambda exercide

# #square
# my_list = [5,4,3]
# print(list(map(lambda item: item ** 2, my_list)))

# #list sorint
# a = [(0,2), (10, -1), (3,2)]
# a.sort(key=lambda x: x[1])
# print(a)





# map, filter, zip and reduce
# map()
# from functools import reduce
# my_list = [1,2,3]
# your_list = [10,20,30]

# # def multiply_by_2(item):   
# #     return item*2

# # print(list(map(lambda item: item * 2, my_list ))) #use lambda instead of the multiply_by_2()
# # print(my_list)

# # def only_odd(item):
# #     return item % 2 != 0

# print(list(filter(lambda item: item % 2 != 0, my_list ))) #use lambda instead of the only_odd(item)
# print(my_list)

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item
    
# print(reduce(accumulator, my_list, 0))
# print(my_list)


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





    

    