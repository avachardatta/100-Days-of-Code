# Create a program:

# Ask user to enter 5 words.
# Store them in a list.
# After all inputs:
# Print:
# Longest word
# Shortest word
# Total number of words that start with "a" (case-insensitive)



# words = ["apple", "banana", "cat", "elephant", "dog"]
# words = []

# longest_word = words[0]
# shortest_word = words[0]
# count_starts_with_a = 0

# for i in range(5):
#     row_data = input(f"write a some words here {i+1}: ")
#     words.append(row_data)

# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

#     if len(word) < len(shortest_word):
#         shortest_word = word

#     if word.lower().startswith("a"):
#         count_starts_with_a += 1    



# print("Longest words: ", longest_word)
# print("Shortest words: ", shortest_word)
# print("Start with a: ", count_starts_with_a) 



# -----------------------------------------------------------------------------------------------------------------------------------------------------


# Create a program:

# Ask user to enter 5 numbers.

# Store them in a list.

# After input, print:

# Count of even numbers
# Count of odd numbers
# Sum of even numbers only
# Sum of odd numbers only


# no = []
# even_no = 0
# odd_no = 0
# even_sum = 0
# odd_sum = 0

# for i in range(5):
#     row_data = int(input(f"write a some words here {i+1}: "))
#     no.append(row_data)

# for nos in no:
#     if nos % 2 == 0:
#         even_no += 1
#         even_sum  += nos
#     else:
#         odd_no += 1
#         odd_sum += nos


# print("Even no: ", even_no)
# print("Odd no : ", odd_no)
# print("total of even no: ", even_sum)
# print("total of odd no: ", odd_sum)



# -------------------------------------------------------------------------------------------------------------------------------------------------


# Ask the user to enter 5 names.

# Store them in a list.

# After all inputs, print:

# Names with more than 5 characters
# Total count of such names



# data = []
# word_gr_than_5 = 0

# for i in range(5):
#     row_data = input(f"write a some words here {i+1}: ")
#     data.append(row_data)

# for word in data:
#     if len(word) > 5:
#         word_gr_than_5 += 1
#         print(word)

# print("Count of greter than 5 words: ", data)