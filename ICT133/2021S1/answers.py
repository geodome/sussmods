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

import random

# q1

def q1a_i(n: int) -> None:
    tens = n // 10
    ones = n % 10
    if tens == 1 or ones == 1:
        print("valid")

def q1a_ii(s: str) -> None:
    if s[0] == s[1] and s[1] == s[2]:
        print("Group A")
    if s[0] == s[2] and s[0] != s[1]:
        print("Group B")
    if s[0] != s[2]:
        print("Group C")

def q1a_iii(nList: list[int]) -> None:
    total = sum(nList[::2])
    if total % 2 == 0:
        print("sum of digits in even position is even")
    else:
        print("sum of digits in even position is odd")

def q1b_i(s: str) -> None:
    for d1 in s[::-1]:
        d2 = int(d1) - 1
        print(d2)

def q1b_ii(s: str) -> None:
    # assumes len(s) > 1
    for i in range(len(s)-1):
        d1 = int(s[i])
        d2 = int(s[i+1])
        if d1 + d2 >= 12:
            print("False")
            break
    else:
        print("True")

# q2

def task1(X: list[str|float], Y: list[str,float]) -> None:
    # 2 control structures are used
    price_diff = 0
    for product, price in X.items():
        price_diff += price - Y[product]
    price_diff = price_diff / len(price_diff)
    if price_diff == 0:
        print("Both stores share the same average price")
    elif price_diff < 0:
        print("The average price of store X is cheaper.")
    else:
        print("The average price difference of store Y is cheaper.")

def task2(X: list[str|float], Y: list[str,float]) -> None:
    # 2 control structures are used
    for product, price in X.items():
        if price < Y[product]:
            print(product, price)
    
def task3(product: str, X: list[str, float], Y: list[str,float]) -> None:
    # no control structures are used
    print("X:", X[product], "Y:", Y[product])

# q3

def roll() -> int:
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def playGame(playerList: list[str], maxLimit: int) -> list[str]:
    rolls = []
    highest = -1
    for _ in playerList:
        n = roll()
        rolls.append(n)
        if n <= maxLimit and n > highest:
            highest = n
    winners = []
    for i in range(len(playerList)):
        if rolls[i] == highest:
            winners.append(playerList[i])
    return winners

def main() -> None:
    playerList = ["A", "B", "C", "D", "E"]
    maxLimit = 12
    SKIPPED = 0

    toExit = False
    while not toExit:
        print("Menu")
        print("1. Change max limit for sum of 3 rolls")
        print("2. Play Game")
        print("0. Exit")
        
        choice = int(input("Enter choice: "))
        if choice == SKIPPED:
            toExit = True
            print("Application ends")
        elif choice == 1:
            n = int(input("Enter a new max limit: "))
            if n < 10:
                print("Please enter a number that is at least 10.")
            else:
                maxLimit = n
                print(f"The new max limit is {maxLimit}.")
        elif choice == 2:
            winners = playGame(playerList, maxLimit)
            for winner in winners:
                print(winner)
        else:
            print("Invalid choice")

# q4a i and ii

def readFile(filename="products.txt") -> dict[str, list[float|str]]:
    data = {}
    with open(filename) as f:
        for line in f:
            items = line.split(",")
            product = items[0].strip()
            price = float(items[1])
            desc = items[2].strip()
            data[product] = [price, desc]
    return data

def writeFile(data: dict[str,list[float|str]], filename="products.txt") -> None:
    with open(filename, "w") as f:
        for product, info in data.items():
            price, desc = info
            print(f"{product}, {price:.2f}, {desc}", file=f)

# q4b i and ii

def display_registry() -> None:
    data = readFile("products.txt")
    for product, info in data.items():
        price, desc = info
        print(f"{product}, {price:.2f}, {desc}")

def update_registry() -> None:
    data = readFile("products.txt")
    toExit = False
    SKIPPED = ""
    while not toExit:
        code = input("Enter code of product: ").strip()
        if code == SKIPPED:
            toExit = True
        elif code in data:
            price = float(input("Enter price of product: "))
            data[code][0] = float(f"{price:.2f}")
            writeFile(data)
            print(f"Updating entry {code} with new price {price:.2f}")
        else:
            price = float(input("Enter price of product: "))
            desc = input("Enter name of product: ").strip()
            data[code] = [float(f"{price:.2f}"), desc]
            writeFile(data)
            print(f"adding entry {code}, {price:.2f}, {desc}")

