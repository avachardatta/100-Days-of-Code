# List and list methods


# Write a program that:

# create empty list
# ask user to enter 5 favorite movies
# store movies using:

# movies = []

# print("Enter ur favourite movie name")

# for i in range(5):
#     movie = input(f"Enter ur favourite movies {i+1}: ")
#     movies.append(movie)

# print("Your favourite movies", movies)

# --------------------------------------------------------------------------------------------------------------------------------------------------------



# Write a program that:

# Create this list
# numbers = [10,20,30,40,50]

# Expected output
# [10,30,40,50,60]


# no = []
# for i in range(5):
#     numbers = int(input(f"Enter no here(10,20,30,40,50) {i+1}: "))
#     no.append(numbers)

# no.append(60)

# print("Original List: ", no)

# removed_item = no.pop(1)


# print(f"Removed item was: {removed_item}")
# print("After remove : ", no)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------



# Write a program that:
# create list:
# print:
# how many times 45 appears
# index position of first 90


# marks = [45, 78, 90, 45, 67, 45]

# print("No 45 appers: ", marks.count(45))

# search_no = 90

# if search_no in marks:
#     print(f"found at index: {marks.index(search_no)}")
# else:
#     print(f"sorry {search_no} is not found")    


# -------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# create list
# using list methods:
# sort list in ascending order
# reverse the list
# print final output



# numbers = [50, 10, 90, 30, 70]

# numbers.sort()

# print("Sorted No: ", numbers)

# numbers.reverse()

# print("Reverse sort: ", numbers)




# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# create empty list
# ask user to enter 5 numbers using loop
# store numbers in list
# print:
# largest number
# smallest number
# total sum


# numbers = []

# for i in range(5):
#     no = int(input(f"Enter no here {i+1}: "))
#     numbers.append(no)

# total = sum(list)

# print("Largest No: ", max(numbers))
# print("Smallest No: ", min(numbers))
# print("Total : ", total)


# --------------------------------------------------------------------------------------------------------------------------------------------------------




# Write a program that:

# create list:

# ask user to enter fruit name
# conditions:
# if fruit exists in list
# → print "Fruit Available"
# otherwise
# → print "Fruit Not Available



# fruits = ["apple", "banana", "mango"]

# for i in range(5):
#     fruit = input(f"Enter frutis and check availibilty {i+1}: ").lower().strip()
#     if fruit in fruits:
#         print("Fruit Available")
#     else:
#         print("Fruit Not Available")    

# --------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:

# create empty list
# ask user to enter 5 numbers
# store numbers in list
# print:
# only even numbers from list


# even_numbers = []
# odd_numbers = []

# for i in range(5):
#     no = int(input(f"Enter no here {i+1}: "))
    
#     if no % 2 == 0:
#        even_numbers.append(no)
#     else:
#         odd_numbers.append(no)

# print("Even No: ", even_numbers)
# print("Odd No: ", odd_numbers)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# create list

# using loop:
# convert every name to title case
# store updated names in NEW list


# names = ["datta", "rahul", "amit"]

# title_case_names = []


# for name in names:
#     cleaned_name = name.title()
#     title_case_names.append(cleaned_name)

# print("Original names:", names)
# print("Updated names: ", title_case_names)

# --------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:
# create list
# using loop:
# create NEW list containing only numbers greater than 40
# print final filtered list

# numbers = [10, 25, 30, 45, 60, 75]

# new_list = []

# for i in numbers:
#     if(i > 40):
#         new_list.append(i)
      


# print("new updated list: ", new_list)


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:
# create list:
# ask user to enter new item
# insert new item at:


# items = ["laptop", "mouse", "keyboard"]

# new_item = input("Ener a word here: ")
# items.insert(1,new_item)


# print("Update list: ", items)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:
# create two lists:
# combine both lists into ONE list
# print final list

# no1 = [10,20,30]
# no2 = [40,50,60]


# no1.extend(no2)

# print("Combine list: ", no1)



# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Task
# Create empty list called fruits
# add 3 fruits using:change second fruit to:



# fruits = []

# for i in range(3):
#     favourite_fruits = input(f"Enter ur favourite fruits {i+1} :")
#     fruits.append(favourite_fruits)
    
# fruits[1] = "Orange"

# print("U enter this fruits list: ", fruits)    




# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Create list:
# print only the middle 4 numbers using slicing
# print reversed list using slicing
# print only the middle 4 numbers using slicing
# print reversed list using slicing



# numbers = [10,20,30,40,50,60,70,80,90,100]

# # 0     1    2    3    4   5     6   7  8    9
# # 10 , 20 , 30 , 40 , 50 , 60 , 70, 80 , 90 ,100


# print(numbers[3:7])
# print(numbers[::-1])



# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# Ask user to enter a sentence.
# Then:
# convert sentence into list of words using:
# print:
# word list
# total number of words


# row_sen = input("Enter sentense here: ").split()

# total_words = len(row_sen)

# # sentese.sp

# print(row_sen)

# print("No of words: ", total_words)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Create list:
# combine list into single sentence using:

# words = ["Python", "is", "fun"]

# new_sentense = " ".join(words)

# print("new sentense: ", new_sentense)


# ------------------------------------------------------------------------------------------------------------------------------------------------------


# Create list:
# print only EVEN numbers
# print square of each even number

# numbers = [10,15,22,31,40,55]

# even_number = []
# odd_number = []

# for i in numbers:
#    if i % 2 == 0:
#     print("Even No: ", i , "|", "Square: ", i**2)
#     even_number.append(i)
#    else:
#         print("Odd No:  ", i, "|", "Square: ", i**2)
#         odd_number.append(i)

# -------------------------------------------------------------------------------------------------------------------------------------------------------




# colors = []

# for i in range(3):
#    colurs = input(f"Enter a color here {i+1}: ")
#    colors.append(colurs)

# colors.insert(1,"Yellow")

# print("Colors: ", colors)





# -----------------------------------------------------------------------------------------------------------------------------------------------------


# list1 = [10,20,30]
# list2 = [40,50]

# list1.extend(list2)


# removed_item = list1.pop(-1)

# print("Removed Item:", removed_item)
# print("Update list: ", list1)


# --------------------------------------------------------------------------------------------------------------------------------------------------

# sentense = input("Enter sentense here: ").split()


# extra_space = " ".join(sentense)

# print("new sentense: ", extra_space)

# ------------------------------------------------------------------------------------------------------------------------------------------------------










