# Write a program that:
# Ask user for a sentence

# Clean the sentence:
# remove extra spaces
# convert to lowercase
# Ask user for a word.
# Print:
# Total words in sentence
# First word
# Last word
# Whether search word exists
# Position of first occurrence
# Number of occurrences
# Replace the search word with: ***



# row_word = input("Enter sentense here: ").lower()
# row_word_search = input("Enter word and search: ").lower()
# clean_sen = " ".join(row_word.split())
# clean_sen1 = " ".join(row_word_search.split())

# remove_space = clean_sen.replace(" ","")
# remove_space = clean_sen1.replace(" ","")


# if clean_sen1 in clean_sen:
#     print("Word Found")
#     word_replace = clean_sen.replace(clean_sen1,"***")
#     print("After remove:",word_replace)
#     postion = clean_sen.find(clean_sen1)
#     print("position: ", postion)
#     print("Occurance: " ,clean_sen.count(clean_sen1))
#     words = clean_sen.split()
#     word_count = len(words)
#     print("Total char: ", word_count)
# else:
#     print("word not found")    


# ------------------------------------------------------------------------------------------------------------------------------------------------------



# colors = ("Red", "Blue", "Green", "Black", "White")

# first_color = colors[0]
# last_color = colors[-1]

# char = len(colors)

# print("Total colors: ", char)
# print("FIrst color: ", first_color)
# print("Last color: ", last_color)

# -------------------------------------------------------------------------------------------------------------------------------------------------


# numbers = (10,20,30,40,50,60,70,80)

# # First 3 numbers
# # Last 3 numbers
# # Reverse tuple using slicing


# first_3_numbers = numbers[0:3]
# last_3_number = numbers[-3:]
# reverse_no = numbers[::-1]


# print("First 3 number: " ,first_3_numbers)
# print("Last 3 number: " ,last_3_number)
# print("reverse No :", reverse_no)





# ---------------------------------------------------------------------------------------------------------------------------------------------------



# marks = (45, 78, 90, 45, 67, 45)


# Print:

# How many times 45 appears
# Index position of first 90
# Check if 100 exists in tuple

# duplicate = marks.count(45)
# postion = marks.index(90)

# print("45 appears:", duplicate, "times")
# print("90 found at index:", postion)

# if 100 in marks:
#      print("Found")
# else:
#      print("not found")     



# ---------------------------------------------------------------------------------------------------------------------------------------------------



# employee = ("Datta", 25, "QA")

# name , age , department = employee

# print("Emp Name: ", name)
# print("Emp age: ", age)
# print("Emp Department: ", department)

# -----------------------------------------------------------------------------------------------------------------------------------------------------

students = (
    ("Datta", 85),
    ("Rahul", 90),
    ("Amit", 78)
)

# Print:

# All student names and marks using a loop.
# Find the student with marks greater than 80.
# Print total number of students.



for name, marks in students:
    print(f"name: {name}, marks: {marks}")

for name , marks in students:
    if(marks > 80):
        print(f"names: {name} has score: {marks}")    

total_students = len(students)
print(f"Total no of students: {total_students}")










