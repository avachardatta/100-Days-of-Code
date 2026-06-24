# Count how many times the letter "a" appears.


# feedback = "Data Analytics is Amazing"


# count = 0

# for char in feedback:
#     if char.lower() == 'a':
#         count = count + 1 
# print("Total a's: ", count)




# --------------------------------------------------------------------------------------------------------------------------------------------------

# Print all sales values greater than 1000.

sales = [500, 1200, 800, 1500, 300, 2000]


# count = 0

# for i in sales:
#     if i > 1000:
#         print(i)
#         count = count + 1

# print("Count ", count)        




# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Print only the quarters that made a profit.

profits = (25000, -5000, 18000, -2000, 32000)


# total_sales = 0

# count = 0

# for i in profits:
#     if i > 0:
#         print(i)
#         count += 1
#         total_sales = total_sales + i
# print("Profits: ", count)        
# print("Total sales: ", total_sales)


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Find all employees whose salary is equal to the highest salary.


# employees = [
#     [" datta ", 85000],
#     [" rahul ", 65000],
#     [" sneha ", 92000],
#     [" amit ", 55000],
#     [" priya ", 92000]
# ]


# highest_salary = employees[0][1]

# for emp, salary in employees:
#     if salary > highest_salary:
#         highest_salary = salary


# for emp, salary in employees:
#     if salary == highest_salary:
#         clean_name = emp.strip().title()
#         print(f"Emp Name: {clean_name} | Salary: {salary}")



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Print the duplicate customer names and how many times they appear.

customers = [
    [" Datta ", "Mumbai"],
    [" Rahul ", "Pune"],
    [" Datta ", "Mumbai"],
    [" Sneha ", "Mumbai"],
    [" Rahul ", "Pune"],
    [" Amit ", "Delhi"],
    [" Sneha ", "Mumbai"]
]

# def find_duplicates(customers):
#     name_counts = {}

#     for item in customers:
#         cleaned_name = item[0].strip().title()
#         name_counts[cleaned_name] = name_counts.get(cleaned_name, 0) + 1
            
#     duplicates_with_counts = {}
#     for name, count in name_counts.items():
#         if count > 1:
#             duplicates_with_counts[name] = count

#     return duplicates_with_counts

# duplicate_data = find_duplicates(customers)        

# for name, count in duplicate_data.items():
#     print(f"{name}:  {count} times")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Using a while loop only:

# Print all numbers greater than 30.

# numbers = [10, 25, 40, 55, 70]

# index = 0

# while index < len(numbers):
#     current_no = numbers[index]

#     if current_no > 30:
#         print(current_no) 

#     index += 1

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate the total sales.
# Print the final total

# sales = [1000, 2500, 800, 3000, 1500]

# total_sales = 0

# while sales:
#     single_sale = sales.pop()
#     total_sales = total_sales + single_sale

# print(total_sales)


# --------------------------------------------------------------------------------------------------------------------------------------------------



# A company wants to count how many sales values are greater than 1000.

# def count_high_sales(*args):
#     count = 0
    
#     for i in args:
#         if i > 1000:
#             count += 1
#             print(f"Highest sale: {i}")

#     return count
# total_high_sales = count_high_sales(500, 1200, 800, 1500, 3000)

# print("Number of sales greater than 1000:", total_high_sales)



# ----------------------------------------------------------------------------------------------------------------------------------------------

# find the highest value

# def find_highest(*args):
#     highest_value = 0
#     for i in args:
#         if i > highest_value:
#            highest_value = i
#     return highest_value       
    
# highest = find_highest(45, 12, 89, 23, 67)
# print(highest)



# -------------------------------------------------------------------------------------------------------------------------------------------------

# Print only employees whose salary is greater than 70000.

# def check_salary(**kwargs):

#     high_earners = {}

#     for key , value in kwargs.items():
#         if value > 70000:
#             high_earners[key] = value
#     return high_earners

# results = check_salary(
#     Datta=85000,
#     Rahul=65000,
#     Sneha=92000,
#     Amit=55000
# )    

# for name , salary in results.items():
#     print(f"Name: {name}| salary: {salary}")



# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Requirements
# Clean names using:
# strip()
# title()
# Find duplicate names.
# Return the duplicates as a set.


# def find_duplicate_names(customers):

#     seen = set()
#     duplicate = set()
#     for name , city in customers:
#         cleaned_name = name.strip().title()
#         if cleaned_name in seen:
#             duplicate.add(cleaned_name)
#         else:
#             seen.add(cleaned_name)
#     return duplicate        



# customers = [
#     [" datta ", "Mumbai"],
#     [" rahul ", "Pune"],
#     [" datta ", "Mumbai"],
#     [" sneha ", "Mumbai"],
#     [" rahul ", "Pune"],
#     [" amit ", "Delhi"]
# ]


# print(find_duplicate_names(customers))


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# find the conunt of products

# def count_products(sales):
#     product_count = {}
#     for product , price in sales:
#         if product in product_count:
#             product_count[product] += 1
#         else:
#             product_count[product] = 1                   
#     return product_count

# sales = [
#     ["Laptop", 50000],
#     ["Mouse", 1000],
#     ["Laptop", 50000],
#     ["Keyboard", 2000],
#     ["Mouse", 1000],
#     ["Laptop", 50000]
# ]
# final_counts = count_products(sales)
# print("Product Counts:", final_counts)


# text = "Data Analyst"
# position = text.find("Analyst")

# print(position)



# ----------------------------------------------------------------------------------------------------------------------------------------------------


# employees = ["Datta", "Rahul", "Sneha"]

# employees.append("Priya")

# print(employees)

# employees = ["Datta", "Rahul", "Sneha", "Priya"]

# employees.remove("Rahul")

# print(employees)



# employees = ["Datta", "Rahul", "Sneha", "Priya"]

# employees.pop()

# print(employees)


# numbers = [10, 20, 30, 40, 50]


# print(numbers[1:4])

# sales = [1200, 500, 3000, 800, 2500]

# count = 0
# for i in sales:
#     if i > 1000:
#         print(i)
#         count += 1

# print("Count: ", count)



# numbers = [10, 20, 30, 40, 50]

# reversed_list = []

# for i in range(len(numbers) - 1, -1, -1):
#     reversed_list.append(numbers[i])

# print(reversed_list)




# months = ("Jan", "Feb", "Mar", "Apr", "May")

# for i in months:
#     print(i)



# sales = (1200, 500, 3000, 800, 2500, 400)

# count = 0

# for i in sales:
#     if i > 1000:
#         print(i)
#         count += 1

# print("Count : ", count)        



# months = ("Jan", "Feb", "Mar", "Apr", "May")

# print(months[1:4])



employees = (
    ("Datta", 85000),
    ("Rahul", 65000),
    ("Sneha", 92000),
    ("Amit", 55000)
)


highest_salary = employees[0][1]
top_employee = employees[0][0]


for i , j in employees:
    if j > highest_salary:
        top_employee = i
        highest_salary = j 

print(top_employee)
print(highest_salary)        