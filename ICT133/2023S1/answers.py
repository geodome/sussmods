"""
Author: Donaldson Tan
If you need tuition, feel free to contact me at 
maths_and_programming@outlook.sg.  

If you don't understand the solutions provided, you may 
consult me at @geodome via Telegram.  

I provide tuition for the following SUSS undergraduate modules:  

* BUS105  Statistics
* ENG301  Microprocessor Programming  
* EAS439  Numerical Analysis
* ICT133  Structured Programming  
* ICT162  Object Oriented Programming    
* ICT235  Data Structures and Algorithms
* ICT325  Algorithm Design and Analysis
* ICT330  Database Management Systems
* MTD215  Application of C++ in Multimedia
* MTD315  Computer Interactive Graphics
* MTH105  Fundamentals of Mathematics  
* MTH109  Calculus  
* MTH207  Linear Algebra  
* MTH210  Fundamentals of Probability
* MTH212  Statistical Analysis
* MTH240  Engineering Mathematics I
* MTH316  Multivariable Calculus  
* MTH321  Engineering Mathematics II
* MTH355  Basic Mathematical Optimisation
* MTH357  Applied Regression Analysis I

"""   

#   q1

from math import sqrt

def q1a():
    c = float(input("Enter the longest side: "))
    b = float(input("Enter one shorter side: "))
    a = sqrt(c**2 - b**2)
    print("In order to form a right-angled triangle, the other shorter side should be {a:.2f}")

def q1b():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    right_angled = False
    longest = max(a, b, c)
    if a == longest:
        right_angled = a**2 == b**2 + c**2
    elif b == longest:
        right_angled = b**2 == a**2 + c**2
    else:
        right_angled = c**2 == a**2 + b**2
    if right_angled:
        print(f"The 3 sides [{a:.2f}, {b:.2f}, {c:.2f}] can form a right-angled triangle")
    else:
        print(f"The 3 sides [{a:.2f}, {b:.2f}, {c:.2f}] cannot form a right-angled triangle")

#   q2. Don't use list, set or dictionary

def cafeMenu() -> None:
    print("<< Cafe Menu >>")
    print("A. Soup of the Day")
    print("B. Garden Salad")
    print("C. BLT Sandwich")
    print("X. Exit")

def takeOrder() -> tuple[int,int,int]:
    A, B, C = 0, 0, 0
    while True:
        choice = input("Enter your order: ").strip().upper()
        if choice == "A":
            A += 1
        elif choice == "B":
            B += 1
        elif choice == "C":
            C += 1
        elif choice == "X":
            break
        else:
            print("Invalid choice")
    return A, B, C

def q2a():
    cafeMenu()
    A, B, C = takeOrder()
    total = A*3.5 + B*4.5 + C*5.5

    print(f"Thank you. Please pay ${total:.2f}")

def q2c():
    cafeMenu()
    A, B, C = takeOrder()
    total = A*3.5 + B*4.5 + C*5.5
    if total > 20:
        member = input("Are you a member? (Y/N) ").strip().upper()
        if member == "Y":
            total = 0.9*total
    print(f"Thank you. Please pay ${total:.2f}")

#   q3a

import random

def getDiceValues(number: int):
    """
    No need to sort the dice values. Just generate the frequency for each dice value instead.
    """
    counts = [0 for _ in range(6)]
    for _ in range(number):
        d = random.randint(0,5)
        counts[d] += 1
    dice = 6
    dice_values = []
    for count in counts:
        for _ in range(count):
            dice_values.append(dice)
        dice -= 1
    return dice_values

#   q3b

def playGame():
    NAME, DICE, SCORE, LASTWIN, N = 0, 1, 2, 3, 10
    player1 = [input("Enter player 1 name: "), getDiceValues(N), 0, -2]
    player2 = [input("Enter player 2 name: "), getDiceValues(N), 0, -2]
    for i in range(N):
        dice1, dice2 = player1[DICE][i], player2[DICE][i]
        if dice1 > dice2:
            player1[SCORE] += 1
            if player1[LASTWIN] + 1 == i:
                print(f"{player1[NAME]} is the winner")
                break
            else:
                player1[LASTWIN] = i
        elif dice1 < dice2:
            player2[SCORE] += 1
            if player2[LASTWIN] + 1 == i:
                print(f"{player2[NAME]} is the winner")
                break
            else:
                player2[LASTWIN] = i
    else:
        # when using for-else construct, the else-block only executes if there was no break during the for-loop
        print("Draw. There is no winner.")

    
#   q4a

def countRepeatingChar(word:str) -> int:
    freqTable = {}
    for c in word:
        if c in freqTable:
            freqTable[c] += 1
        else:
            freqTable[c] = 1
    return max(freqTable.values())

#   q4b

def initializeDictionary(filename:str) -> dict[int,list[str]]:
    stats = {}
    with open(filename) as f:
        for line in f:
            word = line.strip()
            count = countRepeatingChar(word)
            if count in stats:
                stats[count].append(word)
            else:
                stats[count] = [word]
    return stats

#   q4c

def main():
    inputfile = "input.txt"
    outputfile = "output.txt"
    stats = initializeDictionary(inputfile)
    freqs = sorted(stats.keys())
    with open(outputfile, "w") as f:
        for freq in freqs:
            if freq > 1:
                words = " ".join(stats[freq])
                print(f"{freq}: {words}", file=f)


