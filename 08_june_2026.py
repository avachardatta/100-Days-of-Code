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

# nos = []
# divisible_by_3 = []

# for i in range(5):
#     no_list = int(input(f"enter no here {i+1}: "))
#     nos.append(no_list)
    
# for i in nos:    
#     if i % 3 == 0:
#         divisible_by_3.append(i)

# print("Numbers divisible by 3:", divisible_by_3)


# ------------------------------------------------------------------------------------------------------------------------------------------------------


# Print:

# Total number of elements
# How many times 20 appears
# Check whether 35 exists or not


# numbers = (15, 20, 35, 20, 50, 20)
# found = False
# apperance = numbers.count(20)

# print("Total Elements: ", len(numbers))
# print("20 appears: ", apperance)


# for no in numbers:
#     if no == 35:
#         print("35 Found")
#         found = True
#         break
# if found == False:
#     print("35 Not found")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# First color
# Last color
# First 3 colors using slicing
# Reverse tuple using slicing


# colors = ("Red", "Blue", "Green", "Yellow", "Black")

# print("First Color: ", colors[0])
# print("Last color: ", colors[-1])
# print("First 3 Colors: ", colors[0:3])
# print("Reverse: ", colors[::-1])

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# store values into variables and print
# Name: Ram
# Age: 25
# Department: Developer
# Salary: 40000



# employee = ("Datta", 25, "QA", 40000)

# name, age, Department, Salary = employee

# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Department: {Department}")
# print(f"Salary: {Salary}")


# -------------------------------------------------------------------------------------------------------------------------------------------

# Print:
# The set
# Total unique elements
# Check whether 30 exists


# numbers = {10, 20, 30, 20, 40, 10, 50}

# print("Unique Elements: ", numbers)
# print("Total unique elements: ", len(numbers))


# if 30 in numbers:
#     print("30 Found")
# else:
#     print("30 not found")


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Perform:

# Add "Power BI"
# Remove "Excel"
# Print final set
# Check if "SQL" exists


# skills = {"Python", "SQL", "Excel"}

# skills.add("Power BI")
# skills.remove("Excel")

# if 'SQL' in skills:
#     print("Sql found")
# else:
#     print("sql not found")


# ----------------------------------------------------------------------------------------------------------------------------------------------------



# set1 = {"Python", "SQL", "Excel"}
# set2 = {"SQL", "Power BI", "Python"}


# common_skills = set1.intersection(set2)

# common_count = len(common_skills)

# print("Common skills: ", common_skills)
# print("Total Common Skills: ",common_count)



# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Print only employees who belong to: qa 

# employees = [
#     ["Datta", "QA", 40000],
#     ["Rahul", "DEV", 55000],
#     ["Amit", "QA", 35000],
#     ["Priya", "HR", 45000]
# ]

# qa_list = []


# for name, dept, salary in employees:
#     if dept.lower() == 'qa':
#         qa_list.append(name)
#         qa_list.append(dept)
#         qa_list.append(salary)

# print("Employees in QA department:", qa_list)        
        # print(f"{name} - {dept} - {salary}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Students scoring 80 or more


# students = [
#     ["Datta", 85],
#     ["Rahul", 72],
#     ["Amit", 91],
#     ["Priya", 65]
# ]


# for name , marks in students:
#     if marks >=80:
#         print(f"{name} - {marks}")


# ------------------------------------------------------------------------------------ ------------------------------------------------------------


# Find the student with the highest marks.

students = [
    ["Datta", 85],
    ["Rahul", 72],
    ["Amit", 91],
    ["Priya", 65]
]


highest_name = students[0][0]
highest_marks = students[0][1]                                                                                                                  

for student in students:
    current_name = student[0]
    current_score = student[1]

    if current_score > highest_marks:
        highest_marks = current_score
        highest_name = current_name

print(f"Topper {highest_name} \n Marks {highest_marks}")    
