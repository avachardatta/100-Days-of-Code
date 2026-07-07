# Write a program:

# Ask user for:

# employee name
# age
# salary
# department
# Conditions
# Level 1

# Employee must satisfy: age >= 21 and salary >= 30000
# Level 2 (Nested If)

# If eligible:

# Check department.

# If department is: ["QA", "DEV", "HR"]
# Eligible For Bonus or not 
# Extra

# Use membership operator: for department checking.

# emp_details = {}
# emp_name = input("Enter emp name: ")
# emp_age = int(input("Enter emp age: "))
# emp_salary = float(input("Enter emp salary: "))
# emp_department = input("Enter emp department: ")



# department = ['QA','Dev','HR']



# if emp_age >= 21 and emp_salary >= 30000:
#     if emp_department.lower() in department:
#         print("Eligible For Bonus")
#     else:
#         print("Department Not Eligible")
# else:
#     print("Ur not eligible")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# emp_details = {}
# emp_name = input("Enter name here: ")
# emp_age = int(input("Enter ur age: "))
# emp_salary = float(input("Enter salary: "))
# ext_loan_amt = float(input("Enter ur existing loan amt: "))


# bonus = 0

# if emp_salary > 50000:
#     bonus+=5000
# else:
#     bonus = 0

# total_salary = emp_salary + bonus

# if emp_age >= 21 and total_salary >= 55000:
#     if ext_loan_amt < 10000:
#         print("Loan Approved")
#     else:
#         print("Clear Existing Loan First")
# else:
#     print("Loan Rejected")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# skills = []
# name = input("Enter ur name here: ")
# age = int(input("Enter ur age here: "))
# department = input("Enter department here: ")
# for i in range(3)
#     candidate_skills = input(f"Enter ur skills {i+1}: ")
#     skills.append(candidate_skills)

# print("Name: ", name)
# print("Department: ", department)
# print("SKills: ", skills)
# print("Total Skills: ", len(skills))


# if age>= 21 and department in ["QA", "DEV", "HR"]:
#     if "Python" in skills:
#         print("Eligible For Interview")
#     else:
#         print("Learn Python First")    
# else:
#     print("Not Eligible")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------



available_items = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 10000
}

# orders = []
# total_bill = 0

# total_budget = float(input("Enter your total shopping budget: "))
# remaining_budget = total_budget


# for i in range(3):
#     print(f"\n-----Item{i+1}----")
#     customer_order = input("Choose item (Laptop, Mouse, Keyboard, Monitor): ").capitalize()

#     if customer_order in available_items:
#         item_price = available_items[customer_order]
        
#         if remaining_budget >= item_price:
#             orders.append(customer_order)
#             total_bill += item_price          
#             remaining_budget -= item_price    
#             print(f"Added {customer_order} to your orders. Cost: {item_price}")
#         else:
#             print(f"Insufficient funds! {customer_order} costs {item_price}, but you only have {remaining_budget} left.")
            
#     else:
#         print("Invalid item selected. This item will not be added.")

# print("\n" + "="*30)
# print("FINAL RECEIPT")
# print("="*30)
# print(f"Initial Budget: {total_budget}")
# print(f"Your final orders: {orders}")
# print(f"Total Bill: {total_bill}")
# print(f"Remaining Change: {remaining_budget}")







































