# basically these are list and tuple which we called as Sequential Data type.

# SETS
Set Data type

# Set is also a collection data type in Python. However, it is not an ordered collection of objects, like a list or tuple. Hence, indexing and slicing operations cannot be done on a set object. A set also doesn’t allow duplicate objects to be stored, whereas, in list and tuple, the same object can appear more than once. Even if an object is put more than once in a set, only one copy is held. Set is a Python implementation of a set as defined in Mathematics. The set object has suitable methods to perform mathematical set operations like union, intersection, difference, etc. A set object contains one or more items, not necessarily of the same type which are separated by a comma and enclosed in curly brackets {}.

S1={1, "Ravi", 75.50}
print(S1)
{1, 75.5, 'Ravi'}
type(S1)
# Output: <class 'set'>
S2={10,23,40,23,50,10}
print(S2)
# Output: {40, 10, 50, 23}

set() function

# Python has an in-built function set() using which set object can be constructed out of any sequence like string, list or tuple object.

S1=set("Internshala")
print(S1)
# Output: {'t', 'n', 's', 'h', 'e', 'a', 'l', 'I', 'r'}
S2=set([45,67,87,36,55])
print(S2)
# Output: {55, 67, 36, 45, 87}
S3=set((10,25,15))
print(S3)
# Output: {25, 10, 15}


# The order of elements in the set is not necessarily the same that is given at the time of assignment. Python optimizes the structure for performing operations over the set as defined in mathematics. Only immutable (and hashable) objects can be a part of a set object. Numbers (integer, float as well as complex), strings, and tuple objects are accepted but list and dictionary objects are not.
S1={(10,10), 10,20}
print(S1)
# Output: {10, 20, (10, 10)}
S2={[10,10], 10,20}

# Output: 
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     S2={[10,10], 10,20}
# TypeError: unhashable type: 'list'

# note:-
# n the first case, (10,10) is a tuple, hence it becomes part of a set. In the second example though, since [10,10] is a list, an error message is displayed saying the list is unhashable. (Hashing is a mechanism in computer science that enables quicker searching of objects in the computer’s memory. https://en.wikipedia.org/wiki/Hash_function) Even though mutable objects are not stored in a set, set itself is a mutable object. A set object can be modified by add(), update(), remove() and discard() methods.



# 1. add(): adds a new element in set object
S1=set({"Python", "Java", "C++"})
print(S1)
# Output: {'Python', 'C++', 'Java'}
S1.add("Perl")
print(S1)
# Output: {'Perl', 'Python', 'C++', 'Java'}


# 2. update():adds multiple items from a list or tuple
S1={"Python", "Java", "C++"}
S1.update(["C++", "Basic"])
S1
# output: {'C++', 'Java', 'Python', 'Basic'}
S1.update(["Ruby", "PHP"])
S1
# output: {'Ruby', 'PHP', 'Java', 'C++', 'Python', 'Basic'}


# 3. clear(): Removes contents of set object results in an empty set
S1.clear()
print(S1)
# output: set()

# 4. copy(): Creates a copy of set object
S1={"Python", "Java", "C++"}
S2=S1.copy()
print(S2)
# output: {'C++', 'Java', 'Python'}

# 5. discard(): Returns set after removing an item from it. No changes are done if the item is not present
S1={"Python", "Java", "C++"}
S1.discard("Java")
print(S1)
# Output: {'C++', 'Python'}
S1.discard("SQL")
print(S1)
# Output: {'C++', 'Python'}

# 6. Returns set after removing an item from it. Results in error if the item is not present
S1={"Python", "Java", "C++"}
S1.remove("C++")
print(S1)
# Output: {'Java', 'Python'}
S1.remove("SQL")
# Output:-
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     S1.remove("SQL")
# KeyError: 'SQL'

# want to read about set operations refer SetOperations folder