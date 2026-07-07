# Task:
# Remove extra spaces from the beginning and end.
# Convert the name to title case.
# Print the final result.

# customer_name = "   datta avachar   "



# clean_sen = ' '.join(customer_name.split())

# title_case = clean_sen.title()

# print(title_case)

# # 2nd way 

# customer_name = customer_name.strip()
# customer_name = customer_name.title()

# print(customer_name)


# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Print only the sales values greater than 1000.

# sales = [1200, 500, 2500, 800, 3200, 900]


# for i in sales:
#     if i > 1000:
#         print(i)


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Task
# Add "Priya" to the list.
# Remove "Rahul" from the list.
# Print the final list.

# customers = ["Datta", "Rahul", "Sneha"]

# customers.append("Priya")
# customers.remove("Rahul")


# print(customers)

# --------------------------------------------------------------------------------------------------------------------------------------------------


# Print each month on a new line using a for loop.
# months = ("Jan", "Feb", "Mar", "Apr")

# for i in months:
#     print(i)



# ----------------------------------------------------------------------------------------------------------------------------------------------



# students = [
#     ["Datta", 85],
#     ["Rahul", 92],
#     ["Sneha", 78]
# ]


# for student , marks in students:
#     print(f"{student} scored {marks}")



# -------------------------------------------------------------------------------------------------------------------------------------------
# Find and print the student with the highest marks.

# students = [
#     ["Datta", 85],
#     ["Rahul", 92],
#     ["Sneha", 78],
#     ["Priya", 95],
#     ["Amit", 88]
# ]

# topper_name = students[0][0]
# max_number = students[0][1]

# for student , marks in students:
#     if marks > max_number:
#         max_number = marks
#         topper_name =  student

# print(f"Topper {topper_name} \nscored: {max_number}")


# ---------------------------------------------------------------------------------------------------------------------------------------------------


# sales = [
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Pen Drive", 700]
# ]



# count = 0

# for product , price in sales:
#     if price > 1000:
#         print(f" {product} - {price}")
#         count+=1

# print("Total exp products: ",count)



# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Print only the duplicate customer IDs.

# customer_ids = [101, 102, 103, 101, 104, 102, 105]

# seen = set()
# duplicates = set()

# for item in customer_ids:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)

# print(duplicates)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Calculate the total sales amount.

# sales = [
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Pen Drive", 700]
# ]


# total_sales = 0
# count = 0

# for products , price in sales:
#     total_sales += price
#     count = count + 1

# avg = total_sales / count


# print("Total sales: ", total_sales)
# print("Average : ", avg)

