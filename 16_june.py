# name = "Data Analyst"

# print(name[0]) ------ D
# print(name[-1]) ---------t
# print(name[0:4]) ------------Data


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


employees = [
    ["Datta", 85],
    ["Rahul", 92],
    ["Sneha", 78],
    ["Priya", 95],
    ["Amit", 88]
]

# Task
# Calculate the average score.
# Print only employees whose score is above average.


# scores = [item[1] for item in employees]

# avg = sum(scores) / len(scores)

# print("Average Score: ", avg)

# for student , marks in employees:
#     if marks > avg:
#         print(f"{student} - {marks}")        



# --------------------------------------------------------------------------------------------------------------------------------------------------


# transactions = [
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Laptop", 50000],
#     ["Keyboard", 1500],
#     ["Mouse", 800],
#     ["Monitor", 12000]
# ]

# seen = set()
# duplicates = set()

# for item , price in transactions:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)

# print(duplicates)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Find the most expensive product and print: without using max

# sales = [
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Pen Drive", 700]
# ]

# max_product = sales[0][0]
# max_price = sales[0][1]

# for item , price in sales:
#     if price > max_price:
#         max_price = price
#         max_product = item

# print(f"Most Expensive Product: {max_product} - {max_price}")


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Count how many times each word appears.
# Do not use collections.Counter

# words = ["python", "sql", "python", "powerbi", "sql", "excel"]

# word_counts = {}

# for word in words:
#     if word in word_counts:
#         word_counts[word] +=1
#     else:
#         word_counts[word] = 1

# for word, count in word_counts.items():
#     print(f"{word}: {count}")



# --------------------------------------------------------------------------------------------------------------------------------------------------



# Print only employees whose salary is greater than 70000.


# employees = [
#     (" DATTA ", 85000),
#     (" rahul ", 65000),
#     (" SNEHA ", 92000),
#     (" amit ", 55000)
# ]

# for emp , salary in employees:
#     if salary > 70000:
#         print(f"Emp Name: {emp.strip().title()} | Salary: {salary}")


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Print only the duplicate customer IDs.

# customer_ids = [
#     "C101",
#     "C102",
#     "C103",
#     "C101",
#     "C104",
#     "C102",
#     "C105"
# ]

# seen = set()
# duplicates = set()

# for i in customer_ids:
#     if i in seen:
#         duplicates.add(i)
#     else:
#         seen.add(i)    

# print(duplicates)        



# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Print only products whose price is greater than 1000.   
# Remove extra spaces.
# Convert product names to uppercase


# orders = [
#     [" laptop ", 50000],
#     ["mouse", 800],
#     [" KEYBOARD ", 1500],
#     ["monitor", 12000],
#     ["pen drive", 700]
# ]


# for product , price in orders:
#     if price > 1000:
#        print(f"Product Name: {product.strip().upper()} | price: {price}")


# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Calculate the total sales.
# Calculate the average sales.
# Print only the months where sales are above average.


# sales = [
#     ("Jan", 12000),
#     ("Feb", 15000),
#     ("Mar", 9000),
#     ("Apr", 18000),
#     ("May", 7000)
# ]


# total_sales = 0


# for month , sale in sales:
#     total_sales += sale
    
# print("Total sales: " , total_sales)   
# average_sales = total_sales / len(sales)
# print("Avg sales: " , average_sales)

# for month, sale in sales:
#     if sale > average_sales:
#         print(f"{month} - {sale}")







# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# Print only the duplicate customer names.
# Remove extra spaces.
# Convert names to title case.



customers = [
    [" Datta ", "Mumbai"],
    [" Rahul ", "Pune"],
    [" Datta ", "Mumbai"],
    [" Sneha ", "Mumbai"],
    [" Rahul ", "Pune"],
    [" Amit ", "Delhi"]
]


# seen = set()
# duplicates = set()

# for name , place in customers:
#     if name in seen:
#         duplicates.add(name)
#         print(f"Duplicate Name: {name.strip().title()}")
#     else:
#         seen.add(name)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# reverse the list without using reverse() / [::-1]

# numbers = [10, 20, 30, 40, 50]


# for i in reversed(numbers):
#     print(i)

# --------------------------------------------------------------------------------------------------------------------------------------------


# text = "Data Analyst"

# count = 0
# vowels = ['a','e','i','o','u']
# found_vowels = []

# for char in text.lower():
#     if char in vowels:
#         count += 1
#         found_vowels.append(char) 

# print("Total Vowels Count: ", count)    
# print("Vowels found in the text: ", found_vowels)



# -------------------------------------------------------------------------------------------------------------------------------------------------


# months = ("Jan", "Feb", "Mar", "Apr", "May")


# output :
# Month 1: Jan
# Month 2: Feb
# Month 3: Mar
# Month 4: Apr
# Month 5: May

# for i in range(5):
#     print(f"Month {i+1}: {months[i]}")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# print Total Unique Numbers and expected output


# numbers = [10, 20, 10, 30, 20, 40, 50, 40]

# unique_list = []

# for num in numbers:
#     if num not in unique_list:
#         unique_list.append(num)

# seen = set()
# duplicate = set()

# for i in numbers:
#     if i in seen:
#         duplicate.add(i)
#     else:
#         seen.add(i)    


# duplicate_count = len(duplicate) 
# print("Unique list: ", unique_list)
# print("Duplicate count: ", duplicate_count)


# --------------------------------------------------------------------------------------------------------------------------------------------------------


# Find all employees who have the highest salary.

employees = [
    ("Datta", 85000),
    ("Rahul", 65000),
    ("Sneha", 92000),
    ("Amit", 55000),
    ("Priya", 92000)
]

highest_salary = employees[0][1]
for emp, salary in employees:
    if salary > highest_salary:
        highest_salary = salary

print(f"Highest Salary Found: {highest_salary}")

for emp, salary in employees:
    if salary == highest_salary:
        print(f"Emp name: {emp} | Salary: {salary}")