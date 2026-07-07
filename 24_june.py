# employee = {
#     "name": "Datta",
#     "salary": 85000,
#     "city": "Mumbai"
# }

# print(employee["salary"])


# ------------------------------------------------------------------------------------------------------------------------------------------------------


# employee = {
#     "name": "Datta",
#     "salary": 85000
# }


# employee["city"] = "Mumbai"

# print(employee)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# employee = {
#     "name": "Datta",
#     "salary": 85000,
#     "city": "Mumbai"
# }


# employee["salary"] = 90000

# print(employee)

# -----------------------------------------------------------------------------------------------------------------------------------------------


# employee = {
#     "name": "Datta",
#     "salary": 85000,
#     "city": "Mumbai"
# }


# for key , value in employee.items():
#     print(f"{key} - {value}")



# ------------------------------------------------------------------------------------------------------------------------------------------------------



# employees = {
#     "Datta": 85000,
#     "Rahul": 65000,
#     "Sneha": 92000,
#     "Amit": 55000
# }


# for key , value in employees.items():
#     if value > 70000:
#         print(f"{key} - {value}")



# --------------------------------------------------------------------------------------------------------------------------------------------------------


# sales = {
#     "Jan": 12000,
#     "Feb": 18000,
#     "Mar": 15000,
#     "Apr": 22000
# }

# highest_salary = 0
# month = ""

# for key , value in sales.items():
#     if value > highest_salary:
#         month = key
#         highest_salary = value

# print(f"{month}- {highest_salary}")        


# --------------------------------------------------------------------------------------------------------------------------------------

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# word_counts = {}

# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
# print(word_counts)            

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# sales = {
#     "Laptop": 50000,
#     "Mouse": 1000,
#     "Keyboard": 2000,
#     "Monitor": 15000
# }


# # for key , value in sales.items():
# #     if value > 5000:
# #         print(f"{key} - {value}")




# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a set that contains only the unique customer names.
# Remove extra spaces using a string method.
# Convert names to Title Case.
# Store only unique names in a set.
# Print the final set.

# customers = [
#     " datta ",
#     " rahul ",
#     " datta ",
#     " sneha ",
#     " amit ",
#     " rahul "
# ]

# unique_customers = set()

# for name in customers:
#     clean_name = name.strip().title()
#     unique_customers.add(clean_name)

# print("Unique customers:", unique_customers )





# -------------------------------------------------------------------------------------------------------------------------------------------------------

# counts how many times each product appears

sales = [
    ["Laptop", 50000],
    ["Mouse", 1000],
    ["Laptop", 50000],
    ["Keyboard", 2000],
    ["Mouse", 1000]
]

# word_count = {}

# for item in sales:
#     product = item[0]

#     if product in word_count:
#         word_count[product] += 1
#     else:
#         word_count[product] = 1    

# print(word_count)        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clean each name using string methods.
# Print only names whose length is greater than


customers = [
    " datta ",
    " rahul ",
    " sneha ",
    " datta ",
    " amit "
]

# for name in customers:
#     clean_name = name.strip().title()
#     if len(clean_name) > 4:
#         print(clean_name)



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Find all sales greater than 1000.
# Store them in a new list.
# Print the new list.
# Print how many sales are in the new list.


sales = [1200, 500, 3000, 800, 2500]

# new_sales = []


# for i in sales:
#     if i > 1000:
#         new_sales.append(i)
# print(new_sales)        
# print("Count of new list",len(new_sales))   



# -------------------------------------------------------------------------------------------------------------------------------------------------------


# Find all unique cities and store them in a set.

# cities = (
#     "Mumbai",
#     "Pune",
#     "Mumbai",
#     "Delhi",
#     "Pune"
# )

# unique_city = set()

# for city in cities:
#     unique_city.add(city)
# print(unique_city)    

# my_set = set(cities)

# print(my_set)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Task
# Clean the employee name.
# Print only employees with salary greater than 70000.
# Display the name in Title Case.

# employees = [
#     [" datta ", 85000],
#     [" rahul ", 65000],
#     [" sneha ", 92000],
#     [" amit ", 55000]
# ]


# for key , value in employees:
#     if value > 70000:
#         clean_name = key.strip().title()
#         print(f"{clean_name} - {value}")



# --------------------------------------------------------------------------------------------------------------------------------------------------

# Create a dictionary that stores how many times each product appears.

products = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse"]

# product_count = {}

# for i in products:
#     if i in product_count:
#         product_count[i] += 1
#     else:
#         product_count[i] = 1    

# print(product_count)        


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Create two lists:

# even_numbers
# odd_numbers

numbers = [10, 25, 40, 55, 70, 85]


# even_no = []
# odd_no = []

# for i in numbers:
#     if i % 2 == 0:
#         even_no.append(i)
#     else:
#         odd_no.append(i)

# print("Even No: ", even_no)        

# print("Odd No: ", odd_no)        


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Task
# Clean every feedback using string methods.
# Convert them to Title Case.
# Store only unique feedbacks in a set.
# Print the final set.


feedback = [
    "Excellent Service",
    "good support",
    "EXCELLENT SERVICE",
    "Good Support",
    "Quick Response"
]

# clean_set = set()

# for i in feedback:
#     clean_feedback = i.strip().title()
#     clean_set.add(clean_feedback)
# print(clean_set)    



# ---------------------------------------------------------------------------------------------------------------------------------------------


# Create a new dictionary where:

# Key = Product Name
# Value = Price



# orders = [
#     ["Laptop", 50000],
#     ["Mouse", 1000],
#     ["Keyboard", 2000],
#     ["Monitor", 15000]
# ]

# my_dict = dict(orders)

# print(my_dict)

# my_dict = {}

# for product, price in orders:
#     my_dict[product] = price

# print(my_dict)


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Create a list that contains only employee names whose salary is greater than 70000.

employees = {
    "Datta": 85000,
    "Rahul": 65000,
    "Sneha": 92000,
    "Amit": 55000
}

# all_names = list(employees.keys())
# high_earners = []

# for name in all_names:
#     if employees[name] > 70000:
#         high_earners.append(name)
# print("High Earners:", high_earners)



# --------------------------------------------------------------------------------------------------------------------------------------------------

# Requirements:

# Clean customer names using strip() and title()
# Store unique customer names in a set
# Return the set
# Print the returned value


# customers = [
#     [" datta ", "Mumbai"],
#     [" rahul ", "Pune"],
#     [" datta ", "Mumbai"],
#     [" sneha ", "Delhi"],
#     [" rahul ", "Pune"]
# ]


# def find_unique_customers(customers):
    
#     clean_names_set  = set()

#     for name , city in customers:
#         clean_name = name.strip().title()
#         clean_names_set.add(clean_name)
#     return clean_names_set
    
# result = find_unique_customers(customers)
# print(result)



# -----------------------------------------------------------------------------------------------------------------------------------------------
# Requirements:

# Clean employee names.
# Consider only salaries greater than 70000.
# Create a dictionary where:
# Key = Employee Name
# Value = Salary
# Return the dictionary.
# Print the returned dictionary.



employees = [
    [" datta ", 85000],
    [" rahul ", 65000],
    [" sneha ", 92000],
    [" amit ", 55000],
    [" datta ", 85000]
]

# def count_high_earners(employees):
#     high_earners_dict = {}

#     for emp_name , salary in employees:
#         clean_name = emp_name.strip().title()
#         if salary > 70000:
#             high_earners_dict[clean_name] = salary
#     return high_earners_dict

# result = count_high_earners(employees)   
# print(result)



