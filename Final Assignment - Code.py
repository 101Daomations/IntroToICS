from collections import namedtuple
meetDate = namedtuple("Meet Date", "month day year location")
clubs = {"imports@UCI" : [meetDate(month=3, day=12, year=2020, location="UTC In & Out")],
         "drive@UCR" : [meetDate(month=5, day=12, year=2020, location="Tiger Sugar")]}

#Takes in a month as an int and returns True if the month is valid, False otherwise
def isValidMonth(month: int) -> bool:
    pass

#Takes in a month and day as an int and returns True if the date is valid, False otherwise
#You can assume that leap years don't exist
def isValid(month: int, day: int) -> bool:
    pass


#Adds a Meet
def addMeet(month: int, day: int, year: int, location: str, club: str) -> None:
    pass


#Deletes a Meet
def delMeet(meet: meetDate, club: str) -> None:
    pass


#Returns a list of grpi[s who have meets in a given month, year
def getMeetsByDate(month: int, year: int) -> [str]:
    pass


#Returns a list of meet locations given a club
def getMeetsByClub(club: str) -> [str]:
    pass



