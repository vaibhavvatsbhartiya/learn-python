# Methods for String Processing

capitalize()
upper()
lower()
title()
find()
index()
count()
isalpha()
isdigit()
islower()
isupper()



# Formatting Strings Using the format() Method
# With Python 3.0, the format() method has been introduced for handling complex string formatting more efficiently. This method of the built-in string class provides functionality for complex variable substitutions and value formatting. This new formatting technique is regarded as more elegant.

# The general syntax of the format() method is: string.format(var1, var2,...)

# 1. The string itself contains placeholders {} in which values of variables are successively inserted.

name="Malhar"
age=23
percentage=55.5
print("my name is {} and my age is {} years".format(name, age))

# Output: 'my name is Malhar and my age is 23 years'

# 2. You can also specify formatting symbols. Only change is using colon (:) instead of %. For example, instead of %s use {:s} and instead of %d use (:d}

print("my name is {:s} and my age is {:d} years".format(name, age))
# Output: 'my name is Malhar and my age is 23 years'


# 3. Precision formatting of numbers can be accordingly done.

print("my name is {:s}, age {:d} and I have scored {:6.3f} percent marks".format(name, age, percentage))
# Output: 'my name is Malhar, age 23 and I have scored 55.500 percent marks'