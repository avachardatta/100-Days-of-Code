# Create a program that:
# Ask user for:
# Name
# Age
# City
# Print the information using an f-string.




# name = input("Enter ur name here: ") 
# age = int(input("Enter ur age here: "))
# city = input("Enter ur city here: ")

# print(f"Hello {name}! \n You are {age} years old , and live in {city}")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that asks the user for:

# Product Name
# Product Price
# Quantity
# total bill




# product_name = input("Enter product name here: ") 
# product_qty = int(input("Enter qty here: "))
# product_price = int(input("Enter product price here: "))

# total_bill = product_price * product_qty

# print(f"Product {product_name} \n product price {product_price} \n Quantity {product_qty} \n, Total Bill {total_bill}")


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that asks the user for:

# Employee Name
# Monthly Salary
# calculate annual_salary = monthly_salary * 12

# emp_name = input("Enter emp name here: ") 
# monthly_salary = float(input("Enter monthly salary here: "))

# annual_salary = monthly_salary * 12

# print(f"Employee: {emp_name} \n Monthly Salary: {monthly_salary} \n Annual Salary: {annual_salary} ")




# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create a program that asks the user for age Age >= 18  → Adult
# Age < 18   → Minor


# age = int(input("Enter ur age here: "))

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")    


# -----------------------------------------------------------------------------------------------------------------------------------------
# Create a program that asks the user for:
# marks
# Marks >= 40  → Pass
# Marks < 40   → Fail



# marks = float(input("Enter ur marks here: "))

# if marks >= 40: 
#     print("Pass")
# else:
#     print("fail")  



# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that asks the user for
# Salary >= 50000  → High Salary
# Salary < 50000   → Regular Salary



# salary = float(input("Enter ur salary here: "))

# if salary >= 50000: 
#     print("High Salary")
# else:
#     print("regular salary")  


# -------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that:
# Ask the user: n 
# usr enter 5 
# and print 
# 1
# 2
# 3
# 4
# 5


# n_value = int(input("Enter ur any number here: "))

# for i in range(n_value):
#     print(i+1)
    

# -------------------------------------------------------------------------------------------------------------------------------------------------


# Create a program that:
# Ask user for a number n.
# Print:

# 1
# 4
# 9
# 16
# 25

# n_value = int(input("Enter ur any number here: "))

# for i in range(n_value):
#     current_no = i + 1
#     print(current_no **2)




# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that:

# Ask the user for a number n.

# Print the total sum from 1 to n.

# 1 + 2 + 3 + 4 + 5 = 15

# n_value = int(input("Enter ur any number here: "))

# total = 0

# for num in range(n_value + 1):
#   total += num
  
# print(total)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# Create a program that:
# Ask the user to enter 5 numbers
# Store them in a list
# Print:
# Original List
# First Number
# Last Number
# Total Numbers Entered


# no = []

# for i in range(5):
#     num = int(input(f"enter a no here {i+1}: "))
#     no.append(num)

# print("Original list: ", no)

# first_no = no[0]
# last_no = no[-1]
# length = len(no)

# print("first No: ", first_no)
# print("last No: ", last_no)
# print("Total no: ", length)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create a program that:

# Create an empty list
# Ask user to enter 5 names
# Store them in the list
# Print only the names that start with "S"

# names = []

# for i in range(5):
#     name_list = input(f"enter name here {i+1}: ")
#     names.append(name_list)

# for single_name in names:
#     if single_name.lower().startswith("s"):
#         print("name start with s: ", single_name)
        

# -----------------------------------------------------------------------------------------------------------------------------------------

# Create a program that:

# Ask the user to enter 5 numbers
# Store them in a list
# Create a new list
# Store only numbers divisible by 3

nos = []
divisible_by_3 = []

for i in range(5):
    no_list = int(input(f"enter no here {i+1}: "))
    nos.append(no_list)
    
for i in nos:    
    if i % 3 == 0:
        divisible_by_3.append(i)

print("Numbers divisible by 3:", divisible_by_3)







