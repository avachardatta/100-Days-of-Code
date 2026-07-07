# employees = ["Datta", "Rahul", "Sneha"]

# employees.append("Amit")

# # print(employees)


# employees = ["Datta", "Rahul"]
# new_employees = ["Sneha", "Amit"]

# employees.extend(new_employees)

# # print(employees)


# employees = ["Datta", "Rahul", "Sneha"]

# employees.insert(1,"Amit")

# # print(employees)


# employees = ["Datta", "Rahul", "Sneha", "Amit"]

# employees.remove("Rahul")

# # print(employees)


# employees = ["Datta", "Rahul", "Sneha", "Amit"]

# # print("Removed: ", employees.pop())

# # print(employees)


# employees = ["Datta", "Rahul", "Sneha", "Amit"]

# # print(employees.index("Sneha"))


# cities = ["Mumbai", "Pune", "Mumbai", "Delhi", "Mumbai", "Pune"]

# # print("No of customer in mumbai : " , cities.count("Mumbai"))

# sales = [4500, 1200, 9800, 3500, 7000]

# sales.sort()
# # print(sales)


# sales = [1200, 3500, 4500, 7000, 9800]

# sales.reverse()
# # print(sales)


# employees = ["Datta", "Rahul", "Sneha", "Amit", "Rohan"]

# lenth = len(employees)
# # print("Total Employees: ", lenth)



# employees = ["Datta", "Rahul", "Sneha", "Amit", "Rohan", "Kiran"]


# print(employees[0:3])



# Create a new list that contains:

# No duplicate names
# Properly formatted names (e.g., Datta)
# Keep the order of the first occurrence


customers = [
    " datta ",
    "Rahul",
    "DATTA",
    " sneha ",
    "rahul",
    "Amit"
]

seen = set()

clean_data = []

for name in customers:
    formated_name = name.strip().capitalize()

    if formated_name not in seen:
        clean_data.append(formated_name)
        seen.add(formated_name)

# print(clean_data)        


# Rules:

# Remove extra spaces.
# Format names professionally.
# Remove duplicate names.
# Preserve the order of first appearance.


customers = [
    "Datta|Mumbai",
    " Rahul |Pune",
    "Sneha| Mumbai ",
    "datta|Mumbai",
    "AMIT|Delhi"
]

seen = set()
clean_data = []

for data in customers:
    parts = data.split("|")

    name = parts[0].strip().title()
    city = parts[1].strip().title()

    unique_key = f"{name}--{city}"

    if unique_key not in seen:
        clean_data.append(name)
        seen.add(unique_key)

print(clean_data)        