
# def greet_user():
#     print("Hello! Welcome back.")


# greet_user()


# -------------------------------------------------------------------------------------------------------------------------------------------------

# def greet(name):
#     print("Hello",name)


# greet("Rahul")
# greet("Datta")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# sales = [1000, 2000, 3000, 4000]

# def calculate_total(sales):
#     total_sales = 0

#     for i in sales:
#         total_sales += i

#     print("Total_sales: ", total_sales)

# calculate_total(sales)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

# marks = [85, 92, 78, 95]

# def calculate_average(marks):
#     total_len = len(marks)

#     avg = sum(marks) / total_len
#     return avg

# my_avg = calculate_average(marks)

# print(my_avg)



# -------------------------------------------------------------------------------------------------------------------------------------------------------

# numbers = [10, 45, 23, 89, 67]

# def find_highest(numbers):
#     max_number = numbers[0]

#     for i in numbers:
#         if i > max_number:
#             max_number = i
#     return i

# highest_no = find_highest(numbers)

# print(highest_no)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

salaries = [45000, 85000, 60000, 95000, 70000]
# Count how many employees have a salary greater than 70000.
# Return the count.

# def count_high_salary(salaries):
#     high_salary = []

#     for i in salaries:
#         if i > 70000:
#             print(f" Salary: {i}")
#             high_salary.append(i)
#     return high_salary

# high_salary_count = count_high_salary(salaries)

# count_of_person = len(high_salary_count)
# print("No of high salary: ", count_of_person)

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Find the highest salary.
# Return the highest salary

employees = [
    ["Datta", 85000],
    ["Rahul", 65000],
    ["Sneha", 92000],
    ["Amit", 55000],
    ["Priya", 92000]
]



# def find_top_salary(employees):
#     top_emp_name = employees[0][0]
#     top_high_salary = employees[0][1]

#     for emp , salary in employees:
#         if salary > top_high_salary:
#             top_high_salary = salary
#             top_emp_name = emp
#     return top_high_salary

# highest_salary = find_top_salary(employees)

# print("Returned Highest Salary:", highest_salary)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Clean customer names using:
# strip()
# title()
# Find duplicate customer names.
# Return the duplicates as a set.


customers = [
    [" Datta ", "Mumbai"],
    [" Rahul ", "Pune"],
    [" Datta ", "Mumbai"],
    [" Sneha ", "Mumbai"],
    [" Rahul ", "Pune"],
    [" Amit ", "Delhi"]
]

# def find_duplicates(customers):
#     seen = set()
#     duplicates = set()

#     for item in customers:
#         cleaned_name = item[0].strip().title()
#         if cleaned_name in seen:
#             duplicates.add(cleaned_name)
#         else:
#             seen.add(cleaned_name)
#     return duplicates

# duplicate_set = find_duplicates(customers)        

# print("Duplicate Customers:", duplicate_set)

# -----------------------------------------------------------------------------------------------------------------------------------------------------


# Print only the sales values greater than 10000.



sales = (12000, 8000, 15000, 7000, 18000, 9000)

# count = 0

# for i in sales:
#     if i > 10000:
#         print(f"sales: -{i}")
#         count = count + 1
# print("Months: ", count)



# --------------------------------------------------------------------------------------------------------------------------------------------------

# Print only the numbers that are divisible by 10.

numbers = {10, 15, 20, 25, 30, 35, 40}

count = 0
for i in numbers:
    if i % 10 == 0:
        print(f"Divisible by 10: {i}")
        count = count + 1

print("No: ", count)


