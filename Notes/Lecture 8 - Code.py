"Today we will be discussing classes"

#What are classes
"""
Essentially classes are objects that we create ourselves and can behave just like any other object that we have seen
or worked with so far.

We want to use classes when we are dealing with something that is more specific and can be categorized as its own object.
"""

#Example of classes that we have seen
"""
From what we have seen before, in the standard library there exists objects such as lists, dictionaries, etc. and with 
all of these objects they have a unique way of initializing/creating them, have unique methods that allow us to work with 
them

For example, Lists are initialized by [] and we can choose to enter in parameters/objects that we want to fill the list with
dictionaries are initialized by {} and just like lists we can choose to enter in parameters/objects as our key value pairs.

myList = []  Initialized to be empty
myDict = {}  Initialized to be empty
set = set()

We cannot use special characters such as {} or [] to initialize our own classes as they are reserved for the built in functions.

Like we have seen before, these objects have methods or functions that are specific to them and called on the
object's SELF instance.

myList.append() and myNewList.append() are using the same .append() method but they are being called on the SELF instance of
different objects.rent objects.
"""

#Our own classes
"""
For our own classes they will behave just like any other object that we have seen so far. 
Our objects will need to be initialized in some way and will need methods that we can use to work with our objects
"""


#This is the class declarations
class Student:

    #constructor
    def __init__(self, id, hw):
        self.id = id
        self.hw = hw

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getHW(self):
        return self.hw

    def getGrade(self):
        grade = sum(self.getHW())
        grade = sum(self.hw) #This is ok too and its not that bad since im still in the class

        total = len(self.getHW())
        total = len(self.hw)

        return grade/total

class UCIstudent(Student):

    def __init__(self, id, hw, favBoba):
        Student.__init__(self, id, hw)
        self.favBoba = favBoba

    def getBoba(self):
        return self.favBoba
        

Trung = Student(1234, [0.9, 0.8, 0.7])
#You dont want to do this
Trung.id = 345
#You want to do this instead
Trung.setId(345)
#You dont want to do this
print(Trung.id)
#You want to do this instead
print(Trung.getId())


print(Trung.getGrade())





















