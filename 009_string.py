v2 = "Devsa Samrat 21"

for v in v2:
    print(v)


# string slicing
print(v2[0::1]) # syntax: string[start: sotp: step] 


# different type of functions i python

print(v2.isalpha()) # check string has only alphabets or not

# isdigit() : check numeric value
# islower() : check lowercase 
# isupper : check uppercase
# lower() : conersion to lowercase
# upper() : conersion to uppercase
# lstrip() : use to remover space from left side
# rstrip() : use to remover space from right side


# strings are immutable(values can't be changed)
# and if i want to change the value of string save it in different one

V = v2.upper()
print(V)