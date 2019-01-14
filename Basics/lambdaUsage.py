items = [
    ("Product1",23),
    ("Product2",7),
    ("Product3",9)
]


#Filtered product list
filtered = list(filter(lambda item:item[1] >= 9, items))
print(filtered)

#get product list out of the tuple list
pricesSorted = sorted(list(map(lambda item:item[1], items)), reverse=True)
print(pricesSorted)






