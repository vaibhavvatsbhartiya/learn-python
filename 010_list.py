# created by placing elements inside square brackets []

V2 = ["Devsa", "Samrat", 21]
# it can have different type of data types

v = [ 1, 3, 5, 7, 9]
v[1]= 21 # see how 3 replace and 21 placed. This lists are mutable
print(v)

# delete 
del v[-1]
print(v)

# del v 
print(v) # delete entire list named v

# List Comprehension: it's a elegant and concise way to create the new list from existing list available

# syntax: new_list = [`expression` `for item in list` `if condition`]

VV = [Vv for Vv in range(100) if Vv%2 == 0]
print(VV)


# different methods which i can used on list 

# append(): use to add new item at the end of list.
# insert(): use to add data at particular position. {[1,2,3] after using insert(1,21) i get [1,21,2,3]}
# sort(): use to sort list which has same type of data in it. eg: numeric values or aplhabetic order
# pop(): use to delete the particular value
# clear(): use to clear the entire value from list, but still list exist which is now empty.
# reverse(): use to reverse the value
# index(): use to find the index/position of particular data
# count(): use to count the number of entries present in the list{ let us suppose number 2 i pass, now count the 2 in entire list.}

# syntax
# list_name.method()


# functions in list
# len(list): use to check the lenght of list. 
# max(list): use to find the max element in list.
# min(list): use to find the minimum element in list.
# sum(list): use to typecast the sequence.
# list(seq): use to get the total sum of all number available in list. 

# my bad, actually there is an error while my server is live on render. I'll solve this soon and notify here. Sorry for the inconvenience.