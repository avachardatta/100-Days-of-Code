# customer_name = "   datta avachar   "

# clean_name = customer_name.strip().title()
# print(clean_name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# For each record:

# Split the string into its three parts.
# Remove extra spaces from each part.
# If the customer is Premium, print:



# customers = [
#     " Datta Avachar | Mumbai | Premium ",
#     " Rahul Sharma | Pune | Standard ",
#     " Sneha Patil | Delhi | Premium ",
#     " Amit Shah | Mumbai | Standard "
# ]





# for data in customers:
#     clean_name = data.split('|')
#     if clean_name[2].strip() == 'Premium':
#         parts = clean_name[0].strip().title()
#         clean_city = clean_name[1].strip().title()    
#         print(f"Customer: {parts} | City: {clean_city}")



# -----------------------------------------------------------------------------------------------------------------------------------------------------------


# customer = "     Datta Avachar     "

# clean_name = customer.strip()
# print(clean_name)



# products = [
#     " Laptop ",
#     " Mouse  ",
#     " Keyboard ",
#     " Monitor "
# ]


# for item in products:
#     clean_products = item.strip()
#     print(clean_products)


# ---------------------------------------------------------------------------------------------------------------------------------

# Remove extra spaces.
# Store the cleaned IDs in a new list.
# Print the new list

employee_ids = [
    " EMP001 ",
    " EMP002",
    "EMP003 ",
    " EMP004 "
]

# new_list = []

# for i in employee_ids:
#     cleaned_id = i.strip()
#     new_list.append(cleaned_id)

# print(new_list)


# ------------------------------------------------------------------------------------------------------------------------------------------------------


employees = [
    " datta avachar ",
    " rahul sharma ",
    " sneha patil "
]

# new_emp_list = []

# for names in employees:
#     clean_products = names.strip().title()
#     new_emp_list.append(clean_products)

# print(new_emp_list)


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# Print only the months where sales are greater than 10,000.

# monthly_sales = (12000, 15000, 9000, 18000, 11000, 7000)


# for i in monthly_sales:
#     if i > 10000:
#         print("sales :", i)



# -------------------------------------------------------------------------------------------------------------------------------------------------------
# "Did we have at least 3 months where sales were greater than 10,000?"

# monthly_sales = (12000, 15000, 9000, 18000, 11000, 7000)

# count = 0

# for i in monthly_sales:
#     if i > 10000:
#         count = count + 1

# if count >= 3:
#     print("Target achieved")
# else:
#     print("Target not achieved")         


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# An HR manager wants to know if every employee has completed mandatory training.


training_status = (
    "Completed",
    "Completed",
    "Pending",
    "Completed",
    "Completed"
)

# all_completed = True

# for i in training_status:
#     if i != 'Completed':
#         all_completed = False
#         break

# print(all_completed)


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# This looks simple, but I want you to think about business efficiency.

profits = (12000, 15000, -5000, 18000, 11000)

# has_loss = False

# for i in profits:
#     if i < 0:
#         has_loss = True
#         break
# if has_loss:
#     print("Warning: Loss Detected")         
# else:
#     print("No Loss This Year")


# ------------------------------------------------------------------------------------------------------------------------------------------------

"I only care about the first Premium order. Once you find it, stop searching."

# orders = [
#     ["ORD101", "Standard"],
#     ["ORD102", "Standard"],
#     ["ORD103", "Premium"],
#     ["ORD104", "Premium"],
#     ["ORD105", "Standard"]
# ]


# for key , value in orders:
#     if value == 'Premium':
#         print("First Premium Order:", key)
#         break


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Can you verify that every employee is Active?"

# If every employee is Active:

# Payroll Can Be Processed

# Otherwise:

# Payroll Blocked



employees = [
    ["EMP001", "Active"],
    ["EMP002", "Active"],
    ["EMP003", "Inactive"],
    ["EMP004", "Active"],
    ["EMP005", "Active"]
]

active = True

for key , value in employees:
    if value == 'Inactive':
        active = False
        break

if active:
    print("Payroll Can Be Processed")
else:
    print("Payroll Blocked")
