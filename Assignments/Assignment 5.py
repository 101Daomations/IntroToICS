from collections import namedtuple
#The template for the named tuple contains 2 variables:
#line_up which is a string and cars_from_line_up which is a list of strings
CARS = namedtuple("CARS", "line_up cars_from_line_up")

#These are the brands made using the cars template
BMW = CARS(line_up= "M line", cars_from_line_up = ["M2","M3","M8"])
BENZ = CARS(line_up = "AMG", cars_from_line_up = ["c43", "c63", "AMG GT"])
PORSCHE= CARS(line_up = "911", cars_from_line_up = ["Carrera", "Targa", "Convertible", "Turbo", "GT3RS"])
HONDA = CARS(line_up = "TYPE R", cars_from_line_up = ["Civic", "Integra", "NSX"])
FORD = CARS(line_up = "MUSTANG", cars_from_line_up = ["ECO BOOST", "GT", "SHELBY GT350"])
DODGE = CARS(line_up = "CHALLENGER", cars_from_line_up = ["V6", "Scat pack", "Hellcat", "DEMON"])

dict_cars = {"German": [BMW, BENZ, PORSCHE], "Japan": [HONDA], "American": [FORD, DODGE]}

#Part 1
"""Count the number of cars in porsche's 911 line up"""
#Do your code here


#Part 2
"""Add another M car to BMW's M line up"""
#Do your code here


#Part 3
"""Find which line up has the most cars in their line up and print the total"""
#Do your code here


#Part 4
"""Remove 'ECO BOOST' from ford's mustang line up"""
#Do your code here


#Part 5
"""Create a list of all the cars in the data structure"""
#Do your code here


#Part 6
"""Find the country that has the most cars"""
#Do your code here


#Part 7
"""Find the country that has the least cars"""
#Do your code here


#Part 8
"""Find which line ups have less than or equal to 3 cars"""