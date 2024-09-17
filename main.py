#Let's practice learning Python

# print("Ice cream is the best!")

# #String 
# first_name = "Sarah"
# food="mac and cheese"
# email = "Sarah@fake.com"

# print(first_name)
# print(f"Do you like {food}?")
# print(f"Your email is {email}.")

# # Integers (whole numbers - would be a float if not)
# age = 34
# quantity = 3
# num_of_students = 8

# print(f"You are {age} years old.")
# print(f"You are buying {quantity} cupcakes.")
# print(f"My old class had {num_of_students} students.")

# # Float
# price = 10.99
# gpa = 3.9
# distance = 5.5

# print(f"The price is ${price}.")
# print(f"Your GPA is: {gpa}")
# print(f"You ran {distance}km.")

# #boolean (true or false)
# is_student = True
# for_sale = False
# is_online = True

# print(f"Are you a student?: {is_student} ")

# if is_student:
#     print("You are a student.")
    
# else:
#     print("You are NOT a student.")

# if for_sale:
#     print("That item is for sale.")
# else:
#     print("That item is NOT available.")

# if is_online:
#     print("You are online")
# else:
#     print("You are offline")

# Typecasting = the process of converting a variable from one data type to another
                # str(), int(), float(), bool()

# name = "Sarah Lakey"
# age = 34
# gpa = 3.9
# is_student = True

# # age = str(age)
# # print(age)
# # print(type(age))

# print(age+1)

# input() = a function that prompts user to enter data 
#           returns data as a string

name = input("What is your name? ")
age = int(input("How old are you? "))

age = age + 1

print(f"Hello, {name}!")
print("Happy birthday!")
print(f"You are {age} years old.")