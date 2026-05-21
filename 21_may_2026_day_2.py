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



numbers = [50, 10, 90, 30, 70]

numbers.sort()

print("Sorted No: ", numbers)

numbers.reverse()

print("Reverse sort: ", numbers)
