#Syntax
#[expression for item in items]
#These can be used in place of map and filter functions as the code looks cleaner and more performant

items = [
    ("Product1",23),
    ("Product2",7),
    ("Product3",9)
]


#Filtering, same as the filter() in the lambdaUsage file
products = [item for item in items if item[1] >= 9]
print(products)

#Mapping
prices = [item[1] for item in items]
print(prices)
