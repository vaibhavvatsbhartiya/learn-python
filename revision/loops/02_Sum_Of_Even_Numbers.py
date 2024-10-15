# print table and skip 5th iteration

num = 21

for i in range (1,11):
    
    if i == 5:
        continue
    j = i*num
    print(num, " x ",i ,"=", j )