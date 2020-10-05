from collections import namedtuple
#The template for the named tuple contains 2 variables:
#line_up which is a string and cars_from_line_up which is a list of strings
CARS = namedtuple("CARS", "line_up cars_from_line_up")

#These are the brands made using the cars template
BMW = CARS(line_up= "M line", cars_from_line_up = ["M2","M3","M8"])
BENZ = CARS(line_up = "AMG", cars_from_line_up = ["c43", "c63", "AMG GT"])
PORSCHE = CARS(line_up = "911", cars_from_line_up = ["Carrera", "Targa", "Convertible", "Turbo", "GT3RS"])
HONDA = CARS(line_up = "TYPE R", cars_from_line_up = ["Civic", "Integra", "NSX"])
FORD = CARS(line_up = "MUSTANG", cars_from_line_up = ["ECO BOOST", "GT", "SHELBY GT350"])
DODGE = CARS(line_up = "CHALLENGER", cars_from_line_up = ["V6", "Scat pack", "Hellcat", "DEMON"])

dict_cars = {"German": [BMW, BENZ, PORSCHE], "Japan": [HONDA], "American": [FORD, DODGE]}

#Part 1
"""Count the number of cars in porsche's 911 line up"""
#Do your code here
def p1():
    count = 0
    for i in dict_cars["German"][2].cars_from_line_up:
        count += 1
    print(count)

    print(len(dict_cars["German"][2].cars_from_line_up))


#Part 2
"""Add another M car to BMW's M line up"""
#Do your code here
def p2():
    dict_cars["German"][0].cars_from_line_up.append("M4")


#Part 3
"""Find which line up has the most cars in their line up and print the total"""
#Do your code here
def p3():
    count = 0
    for country in dict_cars.values():
        for brand in country:
            if len(brand.cars_from_line_up) > count:
                count = len(brand.cars_from_line_up)
    print(count)


#Part 4
"""Remove 'ECO BOOST' from ford's mustang line up"""
#Do your code here
def p4():

    dict_cars["American"][0].cars_from_line_up.remove("ECO BOOST")


#Part 5
"""Create a list of all the cars in the data structure"""
#Do your code here
def p5():
    total = []
    for country in dict_cars.values():
        for brand in country:
            for car in brand.cars_from_line_up:
                total.append(car)
    print(total)


#Part 6
"""Find the country that has the most cars"""
#Do your code here
def p6():
    highest = 0
    place = None
    for country, brands in dict_cars.items():
        count = 0
        for brand in brands:
            count += len(brand.cars_from_line_up)
        if count > highest:
            highest = count
            place = country
    print(place)


#Part 7
"""Find the country that has the least cars"""
#Do your code here
def p7():
    lowest = 0
    place = None
    for country in dict_cars.keys():
        count = 0
        for brand in dict_cars[country]:
            count += len(brand.cars_from_line_up)
    for country, brands in dict_cars.items():
        count = 0
        for brand in brands:
            count += len(brand.cars_from_line_up)
        if lowest == 0:
            lowest = count
            place = country
        elif count < lowest:
            lowest = count
            place = country
    print(place)


#Part 8
"""Find which line ups have less than or equal to 3 cars"""
def p8():
    final = []
    for country in dict_cars.values():
        for brand in country:
            if len(brand.cars_from_line_up) <= 3:
                final.append(brand.line_up)
    print(final)


