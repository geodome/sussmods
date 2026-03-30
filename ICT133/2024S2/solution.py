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

"""
q1(a)

The hint to answering this question lies in the input prompt for each 
variable in the main() function. It tells us the test(x,y,z) function emulates
Python's range(start,stop,step) but a closer inspection of the code at line 2 [x <= y] says
it is inclusive of the stop value, unlike Python's range().

The output are 2,4,6,8. Hence x = 2, y = 8 and z = 2.

q1(b)

testSelection(1) passes the if-criteria at line 8.
testSelection(4) passes the if-criteria at line 12.
testSelection(5) passes the if-criteria at line 6.
testSelection(8) passes the if-criteria at line 10.
testSelection(0) passes the if-criteria at line 3.

The output is:
Scenario 2
Scenario 4
Scenario 1
Scenario 3
Scenario 0

q1(c)

True
False
False
True 

"""

# q2a

def addTwoLists(L1:list[int], L2:list[int]) -> list[int]:
    if len(L1) != len(L2):
        return [] 
    L = []
    for i in range(len(L1)):
        L.append(L1[i] + L2[i])
    return L

# q2b
# to execute the program, run checkExpression(numList)

def checkExpression(expList):
    n_correct = 0
    for exp in expList:
        num1 = exp[0]
        num2 = exp[1]
        result = exp[2]
        if result == num1 + num2:
            print(f"{num1} + {num2} = {result} correct")
            n_correct += 1
        else:
            print(f"{num1} + {num2} = {result} incorrect")
    print(f"{n_correct} correct out of {len(expList)}")

# q3a
def setupMorseMapping(filename:str) -> dict[str,str]:
    map = {}
    with open(filename) as f:
        for line in f:
            letter, code = line.split(" ")
            map[code] = letter 
    return map 

# q3b
def decode(morseMapping:dict, morseCodes:str) -> str:
    codes = morseCodes.split(" ")
    decoded = []
    for code in codes:
        if code not in morseMapping:
            return None
        letter = morseMapping[code]
        decoded.append(letter)
    return " ".join(decoded)

# q4a
import random

def getTreasureList() -> list[int]:
    L = [1,1,1,1,1,0,0,0,0,0]
    random.shuffle(L)
    return L 

def countTreasures(treasureList:list[int], indices:list[int]) -> int:
    count = 0
    for i in indices:
        if treasureList[i] == 1:
            count += 1
    return count 

# q4b

def main():
    treasureList = getTreasureList()
    won = False
    for round in range(1,6):
        picks = input(f"Round {round}: Enter your 5 picks: ")
        indices = [int(i) for i in picks.split(",")]
        count = countTreasures(treasureList, indices)
        print(f"You got {count} hits!!")
        if count == 5:
            won = True 
            break
    if won:
        print("You are the winner!!")
    else:
        print("You lost!!")