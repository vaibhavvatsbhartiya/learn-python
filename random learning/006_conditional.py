v2 = int(input("please enter your age: "))

if(v2 >= 18 and v2 < 150):
    print("you can vote")
elif(v2 > 150):
    print("wow you exceeds the limit")
else:
    print("you can't vote")