"""
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

# question 1a i.
def q1a_i(n: int):
    if n % 10 in (2, 5, 7):
        print("Group A")

# question 1a ii.
def q1a_ii(s: str):
    if len(s) == 7 and s[0] in ("A", "B", "C"):
        print("Valid")
    else:
        print("Invalid")

# question 1a iii
def q1a_iii(s: str):
    isGroupA = s[-3:].lower().count("a") > 0
    isGroupB = s[-3:].lower().count("b") > 0
    if isGroupA:
        print("Group A")
    # cannot use elif as isGroupA and isGroupB are not mutually exclusive
    if isGroupB:
        print("Group B")
    if not (isGroupB or isGroupA):
        print("Group C")

# question 1b i
def q1b_i(s: str):
    oddDigits: list[str] = []
    for d in s:
        digit = int(d)
        if digit % 2 == 1:
            oddDigits.append(d)
    print(" ".join(oddDigits))

# question 1b ii
# error in exam question. the correct sample output is "3 5 4", not "3 5"
def q1b_ii(s: str):
    if len(s) >= 3:
        for i in range(len(s)-3,-1,-1):
            if s[i+1] < s[i] and s[i+1] < s[i+2]:
                print(s[i+1], end=" ")
        print()

q1b_ii("21547")

# question 2
# A dictionary will be used to contain the student id, name and score. 
# The dictionary key will be the student ID while the dictionary value will be a Tuple (StudentID, Name, Score)

# index numbers to access the Tuple representing a student score.
ID, NAME, SCORE = 0, 1, 2 

def task1(ict133: dict[str, tuple[str, str, int]], ict162: dict[str, tuple[str, str, int]]) -> int:
    return len(ict162) - len(ict133)

def task2(ict133: dict[str, tuple[str, str, int]], ict162: dict[str, tuple[str, str, int]]) -> int:
    failboth: list[str] = []
    for id in ict133:
        if id in ict162:
            failboth.append(id)
    return len(failboth)

def task3(ict133: dict[str, tuple[str, str, int]], ict162: dict[str, tuple[str, str, int]]) -> tuple[float, float]:
    ict133total = 0
    for student in ict133.values():
        ict133total += student[SCORE]
    ict133avg = ict133total / len(ict133)

    ict162total = 0
    for student in ict162.values():
        ict162total += student[SCORE]
    ict162avg = ict162total / len(ict162)

    return ict133avg, ict162avg


# question 3

def allSameValuesInSequence(seq: list[int]) -> bool:
    for i in range(1, len(seq)):
        if seq[i-1] != seq[i]:
            return False
    return True 

def allDifferentValuesInSequence(seq: list[int]) -> bool:
    detectedFirst: dict[int, bool] = {}
    for item in seq:
        if item not in detectedFirst:
            detectedFirst[item] = True
        else:
            return False
    return True

def readNumbers() -> list[int]:
    numList: list[int] = []
    while True:
        num = input("Enter a number: ").strip()
        if len(num) == 0:
            if len(numList) >= 2:
                break
            else:
                print("Please enter at least 2 numbers")
        else:
            # assumes valid input
            numList.append(int(num))
    return numList

def main():
    numList = []
    while True:
        print("Menu")
        print("1. Read another number sequence")
        print("2, Determine all numbers same")
        print("3. Determine all numbers different")
        print("0, Exit")
        choice = int(input("Enter a choice: ").strip())
        if choice in (0, 1, 2, 3):
            if choice == 0:
                print("Program ends")
                break
            elif choice == 1:
                numList = readNumbers()
            elif choice == 2:
                if len(numList) == 0:
                    print("You have not entered a number sequence")
                else:
                    if allSameValuesInSequence(numList):
                        print("All numbers are the same in", numList)
                    else:
                        print("Not all numbers are the same in", numList)
            else:
                # choice == 3
                if len(numList) == 0:
                    print("You have not entered a number sequence")
                else:
                    if allDifferentValuesInSequence(numList):
                        print("All numbers are different in", numList)
                    else:
                        print("Not all numbers are different in", numList)
        else:
            print("invalid choice")

# question 4a

def readFile(fname: str) -> dict[str, int]:
    data = {}
    with open(fname) as f:
        for line in f:
            item, qty = line.split()
            data[item] = int(qty)
    return data

def writeFile(fname: str, data: dict[str, int]):
    with open(fname, "w") as f:
        for item, qty in data.items():
            print(item, qty, file=f)

def q4a():
    # read data
    sales = readFile("sales.txt")
    salesToDate = readFile("salesToDate.txt")
    # update data
    for item, qty in sales.items():
        if item in salesToDate:
            salesToDate[item] += qty
        else:
            salesToDate[item] = qty
    # write data
    writeFile("salesToDate.txt", salesToDate) 

# question 4b
prices = {'pencil': 1.85, 'pen': 1.90, 'notebook': 0.90, 'lead': 2.50}

# question 4b i
def getOneSale(prices: dict[str, float]) -> dict[str, int]:
    sale: dict[str, int] = {}
    for item in prices:
        included = random.choice([True, False])
        if included:
            qty = random.randint(1,15)
            sale[item] = qty
    return sale

# question 4b ii:
def displayReceipt(sale: dict[str, int], prices: dict[int, float]):
    iwidth = max([len(item) for item in sale])
    qwidth = max([len(str(qty) for qty in sale.values())])
    total = 0
    for item, qty in sale.items():
        subtotal = qty * prices[item]
        total += subtotal
        print(str(qty).ljust(qwidth), "X", item.ljust(iwidth), "=", f"${subtotal:.2f}")
    print("Total".ljust(iwidth + 1 + 1 + qwidth + 1 + 1), f"${total:.2f}")
    