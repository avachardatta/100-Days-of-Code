# Write a program that:
# Ask user to enter 3 employee records.
# For each employee ask:
# Name
# Target Sales
# Actual Sales
# Store in nested list:
# Calculate : - Performance % Formula : - (actual_sales / target_sales) * 100

# If performance is > 100 then excellent
# >=80 good 
# else need imrpovement



# employees = [
#     ["Datta", 100000, 120000],
#     ["Rahul", 100000, 85000]
# ]


# matrix = []
# n = int(input("Hw many entries: "))

# for i in range(n):
#     emp_name = input("Enter emp_name: ")
#     emp_actual_sale = int(input("Enter emp_actual_sale: "))
#     emp_target_sale = int(input("Enter emp_target_sale: "))

#     performance = (emp_actual_sale / emp_target_sale) * 100

#     if performance > 100:
#         status = "Excellent"
#     elif performance >= 80:
#         status = "Good"
#     else:
#         status = "Need Improvement"


#     matrix.append([emp_name, emp_target_sale, emp_actual_sale, status])

# for emp in matrix:
#     print(f"Name: {emp[0]}")
#     print(f"Performance: {(emp[2]/emp[1])*100:.2f}%")
#     print(f"Status: {emp[3]}")
#     print("-" * 20)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:
# Ask user to enter full name.
# Program should:
# remove extra spaces
# convert to title case
# Print:
# cleaned name
# total characters (excluding spaces)
# Condition:
# If cleaned name contains only alphabets and spaces:


# usr_name = input("Enter ur name: ")

# words_list = usr_name.split()  
# clean_name = " ".join(words_list).title()

# if words_list and all(word.isalpha() for word in words_list):
#     print("Valid Name")
#     print("Cleaned Name: ", clean_name)
    
#     char_only_len = sum(len(word) for word in words_list)
#     print("Total char (excluding spaces): ", char_only_len)
# else:
#     print("Invalid name. Name must only contain alphabets and spaces.")

# -------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:

# Ask user to enter a product name.
# Program should:
# remove extra spaces
# convert to title case
# Conditions:

# Product name:

# must be at least 5 characters long (excluding spaces)
# must NOT contain digits
# Print:

# Also print:
# cleaned product name
# total characters (excluding spaces)

# prod_name = input("Enter ur product Name: ")

# prod_list = prod_name.split()

# clean_prod_name = " ".join(prod_list).title()

# remove_space = clean_prod_name.replace(" ","")

# has_digits = any(char.isdigit() for char in remove_space)

# if len(remove_space) >=5 and not has_digits:
#     print("Clean product name: ", clean_prod_name)
#     print("Len of char: ", len(remove_space))
#     print("Valid name")

# else:
#     print("Invalid name")



# -----------------------------------------------------------------------------------------------------------------------------------------------------




# Write a program that:

# Ask user to enter a filename.
# Program should:
# remove extra spaces
# convert to lowercase
# Conditions:

# File must:

# start with "report"
# end with ".txt"
# must NOT contain spaces
# Print: valid file 


# file_check = input("Enter file name here: ").strip().lower()

# start_with = file_check.startswith("report")
# ends_with = file_check.endswith(".txt")
# has_no_internal_spaces = " " not in file_check

# if start_with and ends_with and has_no_internal_spaces:
#     print("Valid file")
#     print("Cleaned File Name: ", file_check)
#     postion = file_check.find("report")
# else:
#     print("Invalid file")







# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# Ask user to enter a sentence.
# Clean it:
# remove extra spaces
# convert to lowercase
# Ask user for a word to search.
# Print:
# whether word exists
# position using find()
# total occurrences using count()



row_sen = input("Enter sentese here( find ur word): ").lower()
find_word = input("Enter word to find in ur enter sentese: ").lower()

clean_sen = " ".join(row_sen.split())
clean_word = " ".join(find_word.split())


if clean_word in clean_sen:
    print("Word Found")
    postion = clean_sen.find(clean_word)
    print("position: ", postion)
    print("Occurance: " ,clean_sen.count(clean_word))
else:
    print("not found")    

