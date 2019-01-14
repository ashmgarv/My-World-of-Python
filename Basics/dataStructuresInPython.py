#Lists
myList = [56,7,8,90,43,5,71]
print(myList)

#Append at the end of the list
myList.append(23)
print(myList)

#Delete from a specific index
myList.pop(3)
print(myList)

#Delete a range of items
del myList[1:3]
print(myList)

#Remove a specific item whose index is not known ;  only the first occurence is removed
myList.remove(43)

#use -1 to print last value in the list
print(myList[-1])

#insert at a specific index
myList.insert(1,7)
print(myList)


#Count works with lists as well as strings
x = "fgtutpkjnjndjndjijdjnd kjn"
print(x.count('n'))

#Stacks

#LIFO
#Use append to add items at the top of the stack
#Use pop to pop the last item

#Queues
#FIFO

#Tehcnically, queues can be implemented using lists but as we need to shift all the items once we remove a single item at the begining, the
#performance is affected if the number of items is huge ; so we use the dequeue wrapper

from collections import  deque
#dequeue is a class
queue = deque([])
queue.append(1)
queue.append(3)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

#Tuples
#A tuple is a read-only list
#This is a tuple with a single value
#If we remove the trailing ',', python will treat this as an integer
point1 = 1,

point = 1,2
print(type(point))

#Swapping variables
x = 3
y = 4

#Explanation
#Unpacking a tuple is what is helps swapping with just a single line of code
x , y = y , x

print(x,y)


#Arrays
#Arrays perform faster with a large sequence of numbers
#Makes sense to use this only if we have a performance problem
from array import array
#first argument is a typecode, which should a shorthand for one of the types' in Python
numbers = array("i",[1,2,3])
#Has same methods to insert and remove as Lists
#Unlike lists, arrays do not accept different value types


#Sets
numbers = [1,1,2,3,4,5,7,7]
#Use the below command to get the unique elemenst out of a list
unique = set(numbers)
print(unique)
second = {2,3,4,5,9}

#To add an element
second.add(7)

#To remove a particular element
second.remove(5)
print(second)

union = unique | second
print(union)

#Cross data structure operations are prermitted
intersection = unique & second
print(intersection)

print(unique - second)

#Use ^ to print the semantic difference i.e the set of items that are in either unique or second but not in both
print(unique ^ second)

#Items in a set are unordered, that is they do not have a sequence
#Which means that the items cannot be accessed using indeces
#we cannot have duplicates in a set

#Dictionaries
#Approach 1 for definition / declaration

dict1 = {"1":"a","2":"b"}

print(dict1)

dict2 = dict(w="a",y="b")
print(dict2)


#values()
#keys()
#items() - can be packed and unpacked
for i, k in dict2.items():
    print(i , k)


dict3 = {y:y%2 for y in range(2,40,2)}
print(dict3)


#Generator objects can be used to achieve memory efficient operations
#as they take as less as 120 bytes to store any size of data
#Unlike lists they do not store all the values in the memory, instead they spit out new values in every iteration
from sys import getsizeof
xsd = 4000000
print(getsizeof(xsd))

values = (i for i in range(10))
#values is a generator object

print(getsizeof(values))

#We cant get the total number of items we are working with at a point of time as the number of items is not known to the interpreter / compiler

# '*' is the unpacking operator, this can be used to unpack lists
listA = [2,4,6,1,23]
print(listA)

#This prints in the manner: [2,4,6,1,23]

#Now to print in the manner: 2 4 6 1 23,  we can use the unpacking operator * as shown below

print(*listA)

#We can unpack dictionaries using the ** operator
