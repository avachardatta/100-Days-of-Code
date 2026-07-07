text = "   Data Analyst   "

# clean_data = text.strip()
# print(clean_data)


email = "DATTA@GMAIL.COM"

# lower_email = email.lower()
# print(lower_email)


designation = "data analyst"

# upper_email = email.upper()
# print(upper_email)


customer_name = "datta avachar"

# tital_name = customer_name.title()
# print(tital_name)

message = "python is easy"

# tital_name = message.capitalize()
# print(tital_name)



text = "Data Analyst"

# new_word = text.replace('Analyst','Engineer')

# print(new_word)

sentence = "Python is easy to learn"

# find_word = sentence.find('easy')
# print(find_word)


feedback = "Amazing Amazing Service"
# print(feedback.count('Amazing'))

text = "Python Python"

# print(text.count("python"))





text = "Python python PYTHON PyThOn"

# count = 0
# word = text.split()
# for i in word:
#     if i.lower() == 'python':
#         count = count + 1 

# print(count)


record = "EMP001,Datta,Mumbai"

# data = record.split(",")

# print(f"Employee ID: {data[0]} \nName: {data[1]} \nCity: {data[2]}")

# ans Python | SQL | Power BI | Excel

skills = ["Python", "SQL", "Power BI", "Excel"]

# new_list =  " | ".join(skills)

# print(new_list)



invoice = "INV2026001"


# start_with = invoice.startswith('INV')

# if invoice.startswith("INV"):
#     print("Valid Invoice")
# else:
#     print("Invalid Invoice")    


# filename = "sales_report.csv"

# if filename.endswith(".csv"):
#     print("File Accepted")
# else:
#     print("File Not Accepted")



employees = [

" datta avachar ",

" RAHUL SHARMA ",

" sneha patil "

]

clean_name = [name.strip().title() for name in employees]
print(clean_name)


email = "datta@gmail.com"

if email.endswith("@gmail.com"):
    print("Valid email")
else:
    print("Invalid email")

resume = "Python, SQL, Power BI, Excel"

if resume.find("SQL"):
    print("Skill Found")
else:
    print("Skill Missing")    

if "SQL" in resume:
    print("Skill Found")
else:
    print("Skill Missing")



invoice = "INV2026|Laptop|50000"

data = invoice.split("|")


print(f"Invoice: {data[0]}")
print(f"Product: {data[1]}")
print(f"Price: {data[2]}")