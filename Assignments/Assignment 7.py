"""The goal of this assignment is to come up with at least 5 test cases for each of these functions"""

#This function separates evens and odd values into different lists
def myFunction1(array):
    arr1 = []
    arr2 = []
    for i in array:
        if i % 2 != 0:
            arr1.append(i)
        else:
            arr2.append(i)
    return arr1, arr2


#This function removes the nth occurrence of an object in a list
def myFunction2(array, target, n):
    final = []
    count = 0

    for i in array:
        if i == target:
            count += 1
            if count != n:
                final.append(i)
        else:
            final.append(i)

    return final


#Write your own function, it can do what ever it wants but it has to have at least 7 lines
#It cant be something that we've already done, then come up with at least 5 test cases for it
