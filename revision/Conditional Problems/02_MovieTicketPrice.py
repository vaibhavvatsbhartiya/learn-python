
age = int(input("Enter the age: "))

day = str(input("Enter the day: "))

price = 12 if age>=18 else 8

if day == "wednesday":
    price -= 2 

print(price)