#This is the list that you will be using for all the sections of this part
myList = [1, 5, 2, 5, 4, 3, 7, 9, 4, 8, 0]

#Part 1
"""Find the sum of all elements in the list without using sum()"""
count = 0
for i in myList:
    count += i

#Part 2
"""Find the product of all elements in the list"""
count = 1
for i in myList:
    count *= i

#Part 3
"""Find the average of all elements in the list without using sum()"""
count = 0
for i in myList:
    count += i
avg = count / len(myList)

#Part 4
"""myUnique should only contain all the unique values from myList"""
"""Filter the values of myList and append only the unique values to myUnique"""
myUnique = []
for i in myList:
    if i not in myUnique:
        myUnique.append(i)


#Part 5
"""Find how many times the number 5 appears in myList without using count()"""
count = 0
for i in myList:
    if i == 5:
        count += 1


#Part 6
"""Find the max of myList without using max() you can assume that all values in the list are positive"""
current = myList[0]
for i in myList:
    if i > current:
        current = i

#I would do it this way instead since you can't always assume the list wont be empty
current = None
if len(myList) > 0:
    current = myList[0]
    for i in myList:
        if i > current:
            current = i


#This is the string that you will be using for this part
myString = "The Honda s2000 is my favorite car made by Honda. It made 240 hp out of a 2L from 1999-2003 "

#Part 7
"""Index a range from myString to get 's2000'"""
print(myString[10:15])

#Part 8
"""Make a list that contains every word from myString using a method that we discussed"""
new = myString.split(" ")

#Part 9
"""Format myString in 3 different ways using the variables below"""
brand = "Honda"
car = "s2000"
hp = 240


#way 1
print(f"The {brand} {car} is my favorite car made by {brand}. it made {hp} hp out of a 2L from 1999-2003")

#way 2
print("The {} {} is my favorite car made by {}. it made {} hp out of a 2L from 1999-2003".format(brand, car, brand, hp))

#way 3
print("The " + brand + " " + car + " is my favorite car made by " + brand + ". it made " + str(hp) + " hp out of a 2L from 1999-2003")

#Part 10
"""Which way of formatting the string was the easiest"""
"F string was the easiest"

#Part 11
"""Use a method that we discussed to replace 'Honda' and 's2000' in myString with your own favorite brand and car"""
myString = myString.replace("Honda", "BMW")
myString = myString.replace("s2000", "M3")
print(myString)