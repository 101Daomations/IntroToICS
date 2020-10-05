from collections import namedtuple
"""Problem 1"""
#Write a function that will return the highest value
#The function will take in 3 integers and return an integer
def maxofThree(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


"""Problem 2"""
#Write a function that will return the product of all values in a given list
#You can assume that the list will only contain integers or floats
def multiply(array):
    prod = 1
    for i in array:
        prod *= i
    return prod


"""Problem 3"""
#Write a function to check if a number is within a given range (inclusive)
#You can assume that values of start, end, and number are all valid
#Return True if number is in the range False otherwise
def checkRange(start, end, number):
    if number in range(start, end+1):
        return True
    return False


"""Problem 4"""
#Write a function that will take in a List and return a List of all even values from the original list
#Hint: a number is even if its remainder when divided by 2 is 0
def evenValues(array):
    new = []
    for i in array:
        if i % 2 == 0:
            new.append(i)
    return new




"""Problem 5"""
#Write a function that takes in a student named tuple and a major as a string
#and return the student with the updated major
student = namedtuple('student', 'GPA major')
def changeMajor(student, newMajor):
    return student._replace(major = newMajor)



#Ignore this part its just for testing
if __name__ == "__main__":
    print("Problem 1")
    if maxofThree(2,4,8) == 8:
        print("Problem 1 check 1/3 passed")
    if maxofThree(2,10,8) == 10:
        print("Problem 1 check 2/3 passed")
    if maxofThree(10,4,8) == 10:
        print("Problem 1 check 3/3 passed\n")
    print("Problem 2")
    if multiply([2,4,5]) == 40:
        print("Problem 2 check 1/1 passed\n")
    print("Problem 3")
    if checkRange(1,4,2) == True:
        print("Problem 3 check 1/3 passed")
    if checkRange(1, 4, 1) == True:
        print("Problem 3 check 2/3 passed")
    if checkRange(1, 4, 4) == True:
        print("Problem 3 check 3/3 passed\n")
    print("Problem 4")
    if evenValues([1,2,3,4]) == [2,4]:
        print("Problem 4 check 1/1 passed\n")
    print("Problem 5")
    trung = student(GPA="4", major="UU")
    if changeMajor(trung, "DS") == student(GPA="4", major="DS"):
        print("Problem 5 check 1/1 passed")


