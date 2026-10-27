"""
Q1

The if, for and while statements all end with the colon (:)

C

Q2

a(3) < c(4), so print "two"

B.

Q3.

The while loop terminates at the first iteration becauae i % 3 == 0.

The print statement was not executed, so there is no output.

C.

Q4.

The statement `y = x` is executed via pass-by-reference, hence x and y point to the same list.

updating y[0] to 99 changes x to [99,2,3]

B

Q5

my_dict.get("a", 0) returns 1

my_dict,get("d", 3) returns 3

hence, mydict["c"] = 1 + 3 = 4

A.
"""

def q6():
    # keep prompting for charger type until user enters valid charger
    charger = ""
    while not (charger == "AC" or charger == "DC"):
        charger = input("Enter charger type (AC/DC): ").strip().upper()
    # prompt for energy delivered
    kWh = -1
    while kWh <= 0:
        kWh = float(input("Enter energy delivered (kWh): "))

    if charger == "DC":
        # calculate charges for DC
        amount = kWh * 0.68 
        print(f"Please pay ${amount:.2f}")
    else:
        # calculate charges for DC
        if kWh >= 50:
            amount = 20*0.56 + 30*0.54 + (kWh - 50)*0.52
        elif kWh >= 20:
            amount = 20*0.56 + (kWh - 20)*0.54
        else:
            amount = kWh * 0,56
        print(f"Please pay ${amount:.2f}")

def q7():
    count = 0
    with open("input.txt") as f:
        for line in f:
            for c in line:
                if not c.isspace():
                    count += 1
    print(f"Total character count: {count}")

"""
Q8
"""

def mergeDictionary(dict1:dict[str,int], dict2:dict[str,int]) -> dict[str,int]:
    """
    Solution following algorithm guide provided
    """
    # initialise empty dictionary result
    result = {}
    # iterate all key-value pairs in dict1
    for key, value in dict1.items():
        # add each key, value to result
        result[key] = value
    # iterate all key-value oairs in dict2
    for key, value in dict2.items():
        if key in result:
            # if the key already exists in the result, add the value to the existing one
            result[key] += value 
        else:
            # otherwise, insert it into result with its value
            result[key] = value
    #return the result dictionary
    return result

def mergeDictionary2(dict1:dict[str,int], dict2:dict[str,int]) -> dict[str,int]:
    """
    Alternative implementation for mergeDictionary() not following the algorithm guide
    """
    result = {}
    for key, value in dict1.items():
        result[key] = value + dict2.get(key, 0)
    for key, value in dict2.items():
        if key not in result:
            result[key] = value 
    return result

"""
Question 9

There is a typo in the functional requirement.

It states to use random.randint(-1,6) tp simulate the number of gold coins

but random.randint(-1,6) will return 0 which is not a valid number of coins.

Instead, use random.randint(0,6) to simulate the number of coins.
"""

import random 

def open_box() -> int:
    ncoins = random.randint(0,6)
    if ncoins == 0:
        return -1
    return ncoins 

def openMysteryBox() -> int:
    coins = 0
    boxes = 0
    print(f"Gold coins: {coins}")
    while coins < 25:
        new_coins = open_box()
        boxes += 1
        if new_coins == -1:
            coins = 0
            print(f"Box contains: Bomb... Total now: {coins}")
        else:
            if coins + new_coins > 25:
                print(f"Box contains {coins}... Discarded.")
            else:
                coins += new_coins
                print(f"Box contains {coins}... Total now: {coins}")
    print("Treasure chest full!")
    return boxes

"""
Q10
"""

def q10():

    # list player names
    players = ["Lara", "Nico", "Zane"]

    # initialise dictionary boxOpened
    boxOpened = {}
    for p in players:
        boxOpened[p]  = [0,0]
    
    # chest progression
    for p in players:
        for i in range(2):
            boxOpened[p][i] = openMysteryBox()
    
    # tally game result
    min_total = None
    total = {}
    for p in players:
        # print result of each player
        chest1 = boxOpened[p][0]
        chest2 = boxOpened[p][1]
        total = chest1 + chest2
        print(f"{p}: Chest1 = {chest1}, Chest2 = {chest2}, Total = {total}")
        
        # track the lowest total
        if min_total is None:
            min_total = total 
        else:
            if total < min_total:
                min_total = total 

    # declare winner
    for p in players:
        if min_total == boxOpened[p][0] + boxOpened[p][1]:
            print(f"Winner: {p} with {min_total} boxes")