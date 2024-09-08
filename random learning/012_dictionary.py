# Python dictionary is unordered collection of items.
# while other compound data type have only one value as element, dictionary has a 'key : value' pair.


# note:- let us suppose a 
set = {1,3,5,7,9}
# if i try to access a value from set by indexing like: print(set[2])
# I'll get an error because set contains data but randomly for can't access the values by in indexing.
# so how i get value 
# use for loop
for elem in set:
    print(elem)


# Dictionary
my_dict = {1:'Vaibhav', 2:'Vats', 3:'V2', 4:'Devsa', 5:'Samrat', 6:'21'}

# print entire dictionary
print(my_dict)

# also use keys and get the value. similar to indexing but here i've to pass the key
print(my_dict[4])

# loop
for i in my_dict:
    print(my_dict[i]) # i is representing keys here

# add a new value
my_dict['title'] = 'GodLike Great Emperor'
print(my_dict)

# update the value just use keys
my_dict[4] = 'DevSa'
print(my_dict)
