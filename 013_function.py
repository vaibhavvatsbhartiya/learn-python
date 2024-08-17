# Function is a group of related statements that performs a specific task.

# Functions help break our program into smaller and modular chunks. As our program grows larger and larger functions make it well stractured and more organised.

# types of functions

# 1. Built in function: Built in function are those which are already pre-defined in pyton for our use. eg:- int(), input(), max(), min(), len(), range() etc

# 2. Modules: these are a file containing functions and variables defined in the seprated files. A module is a simply a file that contains python code. when i break a program into modules each module should contain function that performs related task. eg: math, random etc

import math # or write import math as m
# dir(math) in console and get all function which can be performaed
print(math.pi) # print(m.pi)

# also i can import a single function only if needed
from math import cos # or use * and it will import all the stuff
print(cos(10))


# 3. User defined: these are created by developer like us. 
# syntax:-
#  def function_name(parameters):
#     """docstring"""
#     statement(s)

def greet(name):
    print('Ram Ram Ji, Sarae nae by', name)


greet('Vaibhav Vats')

# now let us suppose in any case i forget to pass the role
def greets(name, role="Godlike Great Emperor"): # so in that case ik predefined role pass kr diya gya hai
    print('Ram Ram Ji, Sarae nae by', name)
    print("m hoo", role)


greets('Vaibhav Vats') # yaha role pass nhai kra but firr bhi output m aa rha hai 'Godlike Great Emperor'.

# returning from the function
# the return statement is used to exit the function and go back to the place where it is called.

def sum_of_list(a):
    print('calculating ...')
    return sum(a)
    # # or 
    # sum = sum(a)
    # return sum 

list = [1,2,4,3,5,6,7,8,9]
total_sum_of_list = sum_of_list(list)
print('total sum is: ',total_sum_of_list)