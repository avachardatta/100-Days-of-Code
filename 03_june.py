# Ask user to enter a name.

# Print:

# Original name
# Uppercase
# Lowercase
# Title Case
# Length of name

# Example:

# row_data = input("Enter ur name here: ")

# print("Original: ", row_data)
# print("Upper: ", row_data.upper())
# print("lower: ", row_data.lower())
# print("TItle: ", row_data.title())
# print("Length: ", len(row_data))


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# sen = input("Enter a word here: ")
# print(sen.isalpha())

# if sen.isalpha():
#     print("Valid word")
# else:
#     print("Not a valid word")    



# ----------------------------------------------------------------------------------------------------------------------------------------------------------



# Ask user to enter a filename.

# Print:

# filename in lowercase
# startswith("report")
# endswith(".txt")



# file_name = input("Enter file name here: ").lower()

# if file_name.startswith("report") and file_name.endswith(".txt"):
#     print("Lowercase: ",file_name)
#     print("Starts With Report", "True")
#     print("Ends With .txt" , "True")
# else:
#     print("Enter valid file name")

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Create an empty list.
# Ask user to enter 5 numbers.
# Store them 
# Then print:
# Original list
# Largest number
# Smallest number
# Total sum


# no = []
# for i in range (5):
#     number = int(input(f"enter no here {i+1} :"))
#     no.append(number)

# largest_no = max(no)
# smallest_no = min(no)
# total = sum(no)

# print("Original list: ", no)
# print("Largest No: ", largest_no)
# print("Smallest No: ", smallest_no)
# print("Total sum: ", total)




# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Perform these operations:

# Add 60 at the end.
# Insert 15 at index 1.
# Remove 40.
# Print:
# Updated list
# Length of list

# numbers = [10, 20, 30, 40, 50]

# numbers.insert(1,15)
# numbers.append(60)
# numbers.remove(40)
# lenth = len(numbers)

# print("Updated list: ", numbers)
# print("Length: ", lenth)


# ------------------------------------------------------------------------------------------------------------------------------------------------------


# Print:

# How many times 45 appears
# Index position of first 90
# Check whether 100 exists in the list

# marks = [45, 78, 90, 45, 67, 45]

# print("Occurance: ", marks.count(45))
# print("Index position : " , marks.index(90))


# if 100 in marks:
#     print("100 found")
# else:
#     print("100 not found")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Using a loop:
# Create a new list containing only numbers greater than 40.



# numbers = [10, 25, 30, 45, 60, 75]
# filter_list = []

# for i in numbers:
#     if i > 40:
#         filter_list.append(i)
         
# print("Filtered list: ", filter_list)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Print:
# Slicing
# First 3 numbers
# Last 3 numbers
# Middle 4 numbers
# Reverse list using slicing

# numbers = [10,20,30,40,50,60,70,80,90,100]

# print("First 3:", numbers[:3])
# print("Last 3:", numbers[-3:])
# print("Middle 4: ", numbers[3:7])
# print("reverse: ", numbers[::-1])


# --------------------------------------------------------------------------------------------------------------------------------

# Ask user for a new item.
# If item is not already in the list:



# items = ["Laptop", "Mouse", "Keyboard"]

# new_item = input("Enter an item name here: ")

# if new_item in items:
#     print("Item already exists")
# else:
#     items.append(new_item)
#     print("Item added successfully")    
#     print("Updated List:", items)






# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Original sentence
# Sentence without leading/trailing spaces
# Total number of characters (excluding spaces)
# Whether the sentence contains the word "python" (case-insensitive)


row_sen  = input("Enter a sentese here: ").strip()


no_of_char = len(row_sen.replace(" ", ""))

if "python" in row_sen.lower():
    contains_python = True
else:
    contains_python = False


print("Original sentese: ", row_sen)
print("No of char excluding space: ", no_of_char)    
print("Contains 'python'?: ", contains_python)



