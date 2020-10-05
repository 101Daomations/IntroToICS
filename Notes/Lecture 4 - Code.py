from collections import namedtuple
"KPOP is a NAMED TUPLE blue print that contains 2 variables, album and top3songs."
"album is a STRING of the group's album and top3songs is a LIST of the top 3 songs from that album"

KPOP = namedtuple("KPOP", "album top3Songs")
redVelvet = KPOP(album = "The ReVe Festival", top3Songs = ["Psycho", "In & Out", "Remember Forever"])
twice = KPOP(album="FANCY YOU", top3Songs=["FANCY", "HOT", "TURN IT UP"])
blackPink = KPOP(album="SQUARE TWO", top3Songs=["PLAYING WITH FIRE", "STAY", "WHISTLE"])
itzy = KPOP (album="IT'z ICY", top3Songs=["ICY", "CHERRY", "IT'z SUMMER"])
soloQueens = KPOP(album=None, top3Songs=["eight", "Stay Tonight", "Star"])


"kpop is a DICTIONARY where the key is the group's name and the value is a PARENT LIST where the first index is a LIST "
"of TUPLES of all the members where the first index is the member and the second index is their position as an INTEGER,"
"The second index of the PARENT LIST the group's respective NAMED TUPLE"

kpop = {"Red Velvet" : [[("Irene", 1), ("Wendy", 2), ("Joy", 3), ("Seulgi", 4), ("Yeri",5)], redVelvet],
        "Twice" : [[("Tzuyu", 1), ("Mina", 2), ("Dahyun", 3), ("Sana", 4), ("Nayeon", 5),
                    ("Jeongyeon", 6), ("MOMO", 7), ("Jihyo", 8), ("Chaeyoung", 9)], twice],
        "Black Pink" : [[("Jennie", 1), ("Lisa", 2), ("Jisoo", 3), ("Rose", 4)], blackPink],
        "ITZY" : [[("Ryujin", 1), ("Lia", 2), ("Yuna", 3), ("Yeji", 4), ("Chaeryeong", 5)], itzy],
        "Solo Queens" : [[("IU", 1), ("Chung Ha", 2), ("Heize", 3)], soloQueens]}


#What would this print?
print(kpop["Red Velvet"]) #[[("Irene", 1), ("Wendy", 2), ("Joy", 3), ("Seulgi", 4), ("Yeri",5)], redVelvet]

print(kpop["Red Velvet"][0]) #[("Irene", 1), ("Wendy", 2), ("Joy", 3), ("Seulgi", 4), ("Yeri",5)]

print(kpop["Red Velvet"][0][1]) #("Wendy", 2)

print(kpop["Red Velvet"][0][1][0]) #"Wendy"

print(kpop["Red Velvet"][0][1][1]) #2

print(kpop['Red Velvet'][1]) #KPOP(album = "The ReVe Festival", top3Songs = ["Psycho", "In & Out", "Remember Forever"])

print(kpop["Red Velvet"][1].album) #"The ReVe Festival"

print(kpop["Red Velvet"][1].top3Songs) #["Psycho", "In & Out", "Remember Forever"]

print(kpop["Red Velvet"][1].top3Songs[1]) #"In & Out"


"""I want to print every album within the kpop dictionary"""
for group in kpop.keys():
    print(kpop[group][1].album)

for group in kpop.values():
    print(group[1].album)

"""I want to make a combined list of all the members"""
mem = []
for group in kpop.keys():
    for member in kpop[group][0]:
        mem.append(member[0])

"""I want to print the group that have more than 5 members"""
for group in kpop.keys():
    if len(kpop[group][0]) > 5:
        print(group)

"""I want to find the average of all the ints in the dictionary"""
total = 0
mems = 0

for group in kpop.keys():
    for member in kpop[group][0]:
        mems += 1
        total += member[1]

avg = total / mems