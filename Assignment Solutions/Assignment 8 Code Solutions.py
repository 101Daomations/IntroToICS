"""
This assignment will be a little different. I have provided the code for you below and what I want you to do is to
follow along and track what is happening with the text file and the console output.
You will write what you observer as well as why it did on each and every line what it did on a google doc/pdf.
I want you to focus on the 'cursor' like what we discussed in lecture
"""

#Example
file = open("MyFavoriteCars.txt", "w")
file.write("This file contains my favorite cars")
file.close()

#You will write in your google doc something along the lines of
"""
line 8: created and opened the file MyFavoriteCars.txt to write
line 9: Wrote 'This file contains my favorite cars' on the first line of the txt file
line 10: Closed MyFavoriteCars.txt
"""

#UNCOMMENT EACH PART (delete the """ from the top and bottom of the code block)
#AS YOU GO SO YOU CAN TRACK WHAT IS HAPPENING AT EACH PART
#After you uncomment a code block you can leave it uncommented

#Part 1

file = open("MyFavoriteCars.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()


#Part 2

file = open("MyFavoriteCars.txt", "w")
#You can just say lines 37-41 do....
file.write("2008 BMW M3\n"
           "2004 Honda S2000\n"
           "2019 Porsche GT3 Touring\n"
           "2010 Lexus ISF\n"
           "2011 Audi R8")
file.close()




#Part 3

file = open("MyFavoriteCars.txt", "r")
car = file.read()
print(car)
print(file.readline())
file.close()


#Part 4

file = open("MyFavoriteCars.txt", "r")
print(file.readline())
car = file.read()
print(car)
file.close()

print("Part 5")

#Part 5

file = open("MyFavoriteCars.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline() )
file.close()


#Part 6

file = open("MyFavoriteCars.txt", "r")
print(file.readline(3))
print(file.read())
file.close()


print("Part 7")
#Part 7

file = open("MyFavoriteCars.txt", "r")
print(file.readline(12038921))
print(file.read(10))
file.close()


#Part 8

file = open("MyFavoriteCars.txt", "r")
print(file.readlines())
file.close()



#Now that you have a general idea of how files should work lets do some practice

#Part 9
#Open and loop through MyFavoriteCars.txt and print every car (line)
#Write your code here

file = open("MyFavoriteCars.txt", "r")
for i in file:
    print(i)
file.close()

#Part 10
#Do the same thing as part 9 but instead of printing keep a count of how many car (line)
#that has more than 5 characters
print("Part 10")
count = 0
file = open("MyFavoriteCars.txt", "r")
for i in file:
    j = i.split(" ")
    if len(j[1]) > 5:
        count += 1
print(f"{count} car(s) have more than 5 characters")
file.close()