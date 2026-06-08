

# Print:

# Total number of sales entries
# How many sales are greater than 1500
# Highest sale (without using max())

# sales = (1200, 1500, 900, 2000, 1750)


# length = len(sales)
# count_greter_than_1500 = 0
# print("Total Entries: ", length)

# for i in sales:
#     if i > 1500:
#         count_greter_than_1500 += 1
        
# print("sales > 1500:" , count_greter_than_1500)
# highest_sales = max(sales)

# print("Highest sales: ", highest_sales)

# sales = (1200, 1500, 900, 2000, 1750)


# high_sales = sales[0]

# for sale in sales:
#     if sale > high_sales:
#         high_sales = sale


# print("High sales: ", high_sales)        

# ---------------------------------------------------------------------------------------------------------------------------------------


# Print:

# How many times "Pune" appears
# Index of first "Delhi"
# Ask user for a city name


cities = ("Mumbai", "Pune", "Delhi", "Bangalore", "Pune")


count_of_pune = cities.count("Pune")

print("No of occurance: ", count_of_pune)

idx = cities.index("Delhi")

find_city = input("Enter city name here: ").title()


if find_city in cities:
    print("City found")
else:
    print("Not found")

print("index of delhi: ", idx)    

