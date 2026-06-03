# Primitive Data Types + type())


# name = "Datta"
# age = 25
# salary = 40000.00
# is_employee = True


# print("Name data type: ", type(name))
# print("age data type: ", type(age))
# print("salary data type: ", type(salary))
# print("is_employee data type: ", type(is_employee))


# -------------------------------------------------------------------------------------------------------------------------------------------


# (Input + Type Casting)

# Write a program that:

# ask user to enter:
# name
# age
# salary
# convert:
# age → integer
# salary → float
# print:
# values
# datatype of each variable


# emp_name = input("Enter ur Name here: ")
# emp_age = input("Enter ur age here: ")
# emp_salary = input("Enter ur salary here: ")

# new_emp_age = int(emp_age)
# new_emp_salary = float(emp_salary)


# print("Emp Name: ", emp_name)
# print("Emp age: ", emp_age)
# print("Emp salary: ", emp_salary)

# print("Emp Name data type: ", type(emp_name))
# print("Emp age data type: ", type(new_emp_age))
# print("Emp salary data type: ", type(new_emp_salary))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Arithmetic + Comparison Operators

# Write a program that:

# ask user to enter 2 numbers
# print:
# addition
# subtraction
# multiplication
# division
# conditions:
# check if first number is greater than second number


# first_no = int(input("Enter first no here: "))
# secound_no = int(input("Enter secound no here: "))

# print("Addition: ", first_no+secound_no)
# print("Subtraction: ", first_no - secound_no)
# print("Multiplication: ", first_no * secound_no)
# print("Division: ", first_no / secound_no)

# if first_no > secound_no:
#     print("First no is greter")
    

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# ask user to enter:
# username
# password
# conditions:
# username must be:
# admin and password 1234

# usr_name = input("Enter ur user name: ").lower()
# password = int(input("Enter ur password here: "))

# if usr_name == "admin" and password == 1234:
#     print("Login Successful")
# else:
#     print("invalid Credentials")    


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# age = int(input("Enter age: ")) ------------------ value_error


# --------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# ask user to enter:
# first number
# second number
# swap numbers using:

# first_no = int(input("Enter 1st no here: "))
# secound_no = int(input("Enter 2nd no here: "))

# print("Before swapping: ", first_no , '', secound_no)

# temp = first_no
# first_no = secound_no
# secound_no = temp

# print("After swapping: ", first_no ,' ', secound_no)



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Logical + Comparison Operators

# Write a program that:

# ask user to enter:
# age
# salary
# conditions:
# age must be greater than or equal to: 20 and salary 20000

# usr_age = int(input("Enter ur age: "))
# usr_sal = int(input("Enter ur salary: "))

# if usr_age >= 18 and usr_sal > 20000:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")   


# -------------------------------------------------------------------------------------------------------------------------------------------------


# User enters messy employee details.

# Program will:

# clean data
# validate data
# format output properly


# 1. Employee Name

# Ask user to enter employee full name.

# Program should:

# remove extra spaces
# convert to title case

# Validation:
# name should contain only alphabets


# 2. Employee Email

# Ask user to enter email.

# Program should:

# remove spaces
# convert lowercase

# Validation:

# must contain: @ and ends with .com

# Department Name

# Ask user to enter department.

# Program should:

# convert uppercase

# 4. Skills Input

# Ask user to enter skills like:
# convert skills into LIST using:

# Filename Validation

# Ask user to enter report filename.

# Validation:

# must start with: report and ends with .txt



# while True:
#     emp_name = " ".join(input(...).split()).title()
#     check_alph = emp_name.isalpha()

#     if emp_name.replace(" ", "").isalpha():
#         print("valid word")
#         break
#     else:
#         print("Not valid word. Name should contain only alphabets.")


# while True:
#     emp_email = input("Enter ur email: ").lower()

#     if "@" in emp_email and emp_email.endswith(".com"):
#         print("Email is valid")
#         break
#     else:
#         print("Not valid Email. email should contain @ and endswith .com")    


# emp_dept = input("Enter ur dept name: ").upper()
# print("Emp Department: ", emp_dept)

# skills = []
# for i in range(3):
#     emp_skills = input(f"Enter ur skills here {i+1} : ")
#     skills.append(emp_skills)
# print("Emp skills: ", skills, "\n")    
    

# while True:
#     emp_file = input("Enter a file name: ").lower()

#     if emp_file.startswith("report") and emp_file.endswith(".txt"):
#         print("Valid file")
#         break
#     else:
#         print("Invalid file !Must start with 'report' and end with '.txt")    

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# ask user to enter:5 username

# store usernames in list
# conditions for each username:
# must not contain spaces
# must not start with digit
# username length should be: 5 to 12

# if valid then store to the valid list or if not then store to invalid list



# valid_username = []
# invalid_username = []


# for i in range(5):
#     usr_name = input(f"Enter ur user name here {i+1}: ")
#     has_space = " " in usr_name
#     start_with_digit = usr_name[0].isdigit() if len(usr_name) > 0 else False
#     correct_length = 5<=len(usr_name) <=12

#     if not has_space and not start_with_digit and correct_length:
#         valid_username.append(usr_name)
#         print("Valid usrname")
#     else:
#         invalid_username.append(usr_name)
#         print("invalid user name")

# print("Valid User Name: ", valid_username)    
# print("InValid User Name: ", invalid_username)    


# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# ask user to enter:5 passwords
# conditions for valid password:
# minimum length 8 
# must contain:
# at least 1 uppercase letter
# at least 1 lowercase letter
# at least 1 digit
# store:
# valid passwords → valid_pass list
# invalid passwords → invalid_pass list
# print both lists


valid_pass = []
invalid_pass = []

for i in range(5):
    passw = input(f"Enter ur password here {i+1}: ")

    upper_pass = any(c.isupper()  for c in passw)
    lower_pass = any(c.islower()  for c in passw)
    digit_pass = any(c.isdigit()  for c in passw)
    correct_length = 8>=len(passw)

    if upper_pass and lower_pass and digit_pass and correct_length:
        valid_pass.append(passw)
        print("Valid password")
    else:
        invalid_pass.append(passw)
        print("Invalid password")




print("Valid pass: ", valid_pass)   
print("Invalid pass: ", invalid_pass)













