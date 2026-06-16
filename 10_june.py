# Ask the user to enter 5 words.

# Store them in a list.

# After all inputs, print:

# Words having more than 4 characters
# Count of such words
# Convert those words to UPPERCASE before printing


# word_storage = []
# long_words = []


# for i in range(5):
#     single_words = input(f"Enter words here {i+1}: ")

#     word_storage.append(single_words)

# for word in word_storage:
#     if len(word) > 4:
#         long_words.append(word.upper())   


# print("Words having more than 4 characters:", long_words)
# print("Count of such words:", len(long_words))        


# -------------------------------------------------------------------------------------------------------------------------------------------------------

# no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# even_no = []
# odd_no = []

    
# for i in no:
#     if i % 2 == 0:
#         even_no.append(i)
#     else:
#         odd_no.append(i)    

# print("Even no: ", even_no)

# print("Odd no: ", odd_no)


# -------------------------------------------------------------------------------------------------------------------------------------------------



# calculate avg height from a list of heights

# height_list = input("Enter a no using space: ")

# heights = height_list.split()
# count = 0

# for height_list in heights:
#     count = count + 1
# print(count)    


# for i in range(count):
#     heights[i] = int(heights[i])

# total = 0

# for person in heights:
#     total += person

# avg = total / count

# print("Avg : ", round(avg))


# ------------------------------------------------------------------------------------------------------------------------------------------------

# no = 2

# for i in range(1,11):
#     print(no * i)




# ----------------------------------------------------------------------------------------------------------------------------------------------------



# wap to find a maximum from list of no


numbers = input("enter lits of numbers: ")

number_list = numbers.split()

count = 0
for number in number_list:
    count += 1

for i in range(count):
    number_list[1] = int(number_list[i])

max_number = number_list[0]

for number in number_list:
    if number > max_number:
        max_number = number

print("Max Number: ", max_number)        












