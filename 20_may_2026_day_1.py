# String / string methods

# Write a program that:

# asks user to enter a word
# conditions:
# if word contains only alphabets
# → print "Valid word"
# otherwise
# → print "Invalid word"


# word = input("Enter word here: ")

# check_alph = word.isalpha()

# if check_alph:
#     print("valid word")
# else:
#     print("Not valid word")    

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# asks user to enter a number as string
# conditions:
# if input contains only digits
# → print "Valid Number"
# otherwise
# → print "Invalid Number"


# no = input("Enter no here: ")

# check = no.isdigit()

# if check:
#     print("Valid Number")
# else:
#     print("Invalid Number")


# ------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:

# asks user to enter a sentence
# print:
# sentence in uppercase
# sentence in lowercase
# conditions:
# if sentence is fully uppercase
# → print "Already uppercase"



# sentense = input("Enter sentese here (uppercase , lowercase , ): ")

# sen_upper = sentense.isupper()

# if sen_upper:
#     print("Sentense is already upper")
# else:
#     print("Upper Case: " , sentense.upper())
#     print("Lower Case: " , sentense.lower())


# --------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:

# asks user to enter a filename
# conditions:
# file must start with report and end with .txt

# file_det = input("Enter file name: ")

# start = file_det.startswith("report")
# end = file_det.endswith(".txt")

# if start and end:
#     print("Valid file")
# else:
#     print("Invalid file")    


# --------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:

# asks user to enter a sentence
# replace: pyhon to sql
# print updated sentence
# conditions:
# if "sql" exists in updated sentence
# → print "Replacement successful"



# sentese = input("Enter sentese here: ").lower()

# after_repl = sentese.replace("python","SQL")

# print("Ur sentese : ", after_repl)

# if "SQL" in after_repl:
#     print("Replacement successful")
# else:
#     print("Nt Replacement successful")    


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that:

# asks user to enter an email
# program should:
# remove extra spaces
# convert to lowercase
# conditions:
# email must contain "@"
# email must end with ".com"


# while True:
#     email_checker = input("Enter ur email here: ").lower().strip()


#     if "@" in email_checker and email_checker.endswith(".com"):
#         print("Valid Email")
#         break
#     else:
#         print("Enter ur email again")    

# print(f"Ur Email: {email_checker}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# Write a program that:

# asks user to enter a sentence
# program should:
# remove extra spaces
# convert to title case
# print:
# total words
# first word
# last word


# sentence = input("Enter sentese here: ").title()

# cleaned = " ".join(sentence.split()).title()

# text = cleaned.split()

# first_word = text[0]
# last_word = text[-1]
# total_len = len(text)

# print("Uncleaned sentese: ", cleaned)
# print("Total Words: ", total_len)
# print("First word: ", first_word)
# print("Last word: ", last_word)


# ----------------------------------------------------------------------------------------------------------------------------------------------------














