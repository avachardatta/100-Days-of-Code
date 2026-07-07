cities = ["Mumbai", "Pune"]


# cities.append('Delhi')
# print(cities)


courses = ["Python", "SQL"]
new_courses = ["Excel", "Power BI"]


# courses.extend(new_courses)

# print(courses)



months = ["January", "March", "April"]

# months.insert(1,"February")

# print(months)


products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# products.remove("Mouse")

# print(products)


tasks = ["Collect Data", "Clean Data", "Analyze Data", "Create Dashboard"]

# removed = tasks.pop()
# print(removed)

# print(tasks)


courses = ["Python", "SQL", "Excel", "Power BI"]


# position = courses.index("Excel")

# print(position)


courses = ["Python", "SQL", "Python", "Excel", "Python", "Power BI"]

# print(courses.count("Python"))


marks = [78, 92, 65, 88, 95]

marks.sort()
print(marks)



cities = ["Mumbai", "Pune", "Delhi", "Chennai"]

cities.reverse()

print(cities)


orders = [
    "ORD001",
    "ORD002",
    "ORD003",
    "ORD004",
    "ORD005"
]

# print(len(orders))


temp_data = [
    "Record 1",
    "Record 2",
    "Record 3"
]

# temp_data.clear()

# print(temp_data)


sales = [1200, 2500, 3400, 4100, 5500, 6200]

# print(sales[1:4])



courses = ["Python", "SQL", "Excel", "Power BI"]

if "Tableau" in courses:
    print("Course Available")
else:
      print("Course not Available")  