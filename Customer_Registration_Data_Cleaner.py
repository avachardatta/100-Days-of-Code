# Customers enter:

# name
# email
# city
# feedback message

# But users type messy data:

# extra spaces
# uppercase/lowercase mix
# invalid emails
# bad words
# empty text

# Your program should:

# clean data
# validate data
# format properly
# show final cleaned customer record

# This is EXACTLY the type of preprocessing done before:

# storing into database
# sending to CRM
# using Pandas
# analytics systems

while True:
    
    name = input("Enter ur name here: ")

    name_cleaned = " ".join(name.split()).title()

    
    if name_cleaned.replace(" ", "").isalpha() and name_cleaned!= "":
        break
    else:
        print("Enter ur name again use char")     




while True:
    email = input("Enter ur email here: ").strip().lower()


    if "@" in email and email.endswith(".com"):
        print("Valid Email")
        break
    else:
        print("Enter ur email again")    


while True:
    city = input("Enter ur city name: ")

    city_cleaned = " ".join(city.split()).title()

    if city_cleaned.replace(" ", "").isalpha() and city_cleaned!= "":
        break
    else:
        print("Enter ur email again ")  
    

while True:

    Feedback = input("Enter feedback here: ")

    if Feedback == "":
        print("Feedback can not be empty")
        continue

    banned_words = ["badword1", "stupid", "useless"]
    feedback_cleaned = Feedback

    for word in banned_words:
        feedback_cleaned = feedback_cleaned.replace(word, "***")

    break

print("\n" + "="*40)
print("       PROCESSED CUSTOMER RECORD        ")
print("="*40)
print(f"Customer Name: {name_cleaned}")
print(f"Email Address: {email}")
print(f"Target City:   {city_cleaned}")
print(f"Cleaned Feed:  {feedback_cleaned}")
print("="*40)



