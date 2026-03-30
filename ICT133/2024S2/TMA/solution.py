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
from typing import List, Tuple 

# question 1(a)

def q1a():
    AP = 0
    year = int(input("Enter Year of Birth: "))
    age = 2025 - year
    if age < 21:
        print("You are not eligible for AP Cash")
    else:
        yes_no = input("Do you own more than 1 property? (Y/N)").upper()
        if yes_no == "Y":
            AP = 200
        else:
            income = float(input("Assessable Income: "))
            if income <= 34000:
                AP = 600
            elif income <= 100000:
                AP = 350
            else:
                AP = 200
        print(f"You will receive ${AP} AP Cash.")

def q1b():
    AP = 0
    senior = 0
    year = int(input("Enter Year of Birth: "))
    age = 2025 - year
    if age < 21:
        print("You are not eligible for AP Cash")
    else:
        yes_no = input("Do you own more than 1 property? (Y/N)").upper()
        if yes_no == "Y":
            AP = 200
        else:
            income = float(input("Assessable Income: "))
            if income <= 34000:
                AP = 600
            elif income <= 100000:
                AP = 350
            else:
                AP = 200
            av = float(input("Annual value of home: "))
            if av <= 21000:
                if 55 <= age <= 64:
                    senior = 250
                if age > 64:
                    senior = 300
            else:
                if age >= 55:
                    senior = 200
        if senior > 0:
            print(f"You will receive ${AP} AP Cash and ${senior} AP Senior's Bonus")
        else:
            print(f"You will receive ${AP} AP Cash.")

# Question 2
# This question covers materials up to seminar 3. Demonstrate your understanding of functions, 
# selection,  and  repetition  structures.  You  may  explore  the  use  of  list  or  tuple,  but  no 
# dictionary or set is allowed for this question. 

# 2(a)

def isAnagram(word1:str, word2:str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())

# 2(b)

def countVowels(word:str) -> int:
    count = 0
    for c in word:
        if c in ("a", "e", "i", "o", "u"):
            count += 1
    return count

# 2(c)

def countRepeatingCharacters(word:str) -> int:
    counts = [0]*26
    for c in word.lower():
        counts[ord(c) - ord('a')] += 1
    repeating = 0
    for count in counts:
        if count > 1:
            repeating += count
    return repeating 

# 2(d)

def main():
    while True:
        word1 = input("Enter 1st word: ")
        if word1.lower() == "x":
            print("bye")
            break
        word2 = input("Enter 2nd word: ")
        if isAnagram(word1, word2):
            if countRepeatingCharacters(word1) == countVowels(word1):
                print(f"{word1} is a super anagram of {word2}")
            else:
                print(f"{word1} is an anagram of {word2}")
        else:
            print(f"{word1} is not an anagram of {word2}")
        print()

# 3(a)

def factorial1(n:int) -> int:
    """n must be an integer >= 0"""
    if n == 0:
        return 1
    else:
        return n*factorial1(n-1)

# 3(b)
def factorial2(n:int, lookupTable:List[int]):
    if n == 0:
        # n = 0 is not in the lookup table
        return 1
    # consider cases for invoking the lookup table
    if n <= len(lookupTable):
        # factorial n is already in the lookup table
        return lookupTable[n-1]
    else:
        # append factorial n to the table
        lookupTable.append(n*factorial2(n-1))
        return lookupTable[-1]

# question 4
import random

def getPlayers() -> List[str]:
    players = []
    lessThan2 = True
    while lessThan2:
        name = input(f"Enter Player {len(players)+1}'s name: ")
        if len(players) == 0:
            players.append(name)
        elif players[0].lower() == name.lower():
            print("duplicate name. Enter again.")
        else:
            players.append(name)
        lessThan2 = len(players) < 2
    return players

def getBoardSize() -> int:
    n = 0
    rightSize = False
    while not rightSize:
        n = int(input("Enter board size: "))
        rightSize = n >= 5 and n%2 == 1
    return n
        
def getNewBoard(n:int) -> List[List[List[List[str]]]]:
    board = [] 
    treasureMap = []
    toPlant = []
    treasures = (n**2 - 1)//2
    for i in range(n):
        board_row = [] 
        treasure_row = []
        for j in range(n): 
            board_row.append("?")
            treasure_row.append("-")
            toPlant.append((i,j))
        board.append(board_row)
        treasureMap.append(treasure_row)
    random.shuffle(toPlant)
    for i in range(treasures):
        row, col = toPlant[i]
        treasureMap[row][col] = "*"
    return [board, treasureMap]

def printBoard(board:List[List[List[str]]]):
    n = len(board[0])
    width = len(str(n))
    # print header
    print("".ljust(width), end=" ")
    print(" ".join([str(i).ljust(width) for i in range(n)]))
    # print subsequent rows
    for row in range(n):
        print(str(row).ljust(width), end=" ")
        print(" ".join([board[0][row][col].ljust(width) for col in range(n)]))



def validatePick(row: int, col:int, board:List[List[List[str]]]) -> bool:
    n = len(board[0])
    if -1 < row < n and -1 < col < n:
        if board[0][row][col] == "?":
            return True
        else:
            print("The position is already uncovered")
    else:
        print("invalid row or column numbers")
    return False 

def pickSquare(board:List[List[List[str]]], n: int, name:str) -> Tuple[int,int]:
    validated = False
    row, col = 0, 0
    while not validated:
        r, c = input(f"{name}, please pick a square: ").split(",")
        row = int(r)
        col = int(c)
        validated = validatePick(row, col, board)
    return row, col
        
def uncover(board:List[List[List[str]]], row:int, col:int) -> int:
    board[0][row][col] = board[1][row][col]
    if board[0][row][col] == "*":
        print("Is a hit!")
        return 1 
    print("No treasure there")
    return 0

def main():
    # prompt user to enter 2 player names
    players = getPlayers()
    # prompt user to enter board size
    n = getBoardSize()
    nTreasures = (n**2 - 1)//2
    threshold = nTreasures // 2

    nextGame = True
    while nextGame:
        # create new game session
        board = getNewBoard(n)
        scores = [0, 0]
        coveredSquares = n**2
        print("Generated new board and planted treasures")

        # pick first player
        current = random.randint(0,1)

        # start game
        nextRound = True
        while nextRound:
            # display board
            printBoard(board)
            print()
            # ask user to enter valid row, col
            row, col = pickSquare(board, n, players[current])
            # uncover the board
            increment = uncover(board, row, col)
            coveredSquares -= 1
            # update score
            scores[current] += increment 
            # evaluate whether to go to next round
            nextRound = coveredSquares > 0 and scores[current] <= threshold
            # print score tally
            if nextRound:
                print(f"Current score: {players[0]}({scores[0]}) {players[1]}({scores[1]})")
                print()
            # switch to next player
            current = 1 - current
        
        # determine winner
        if scores[0] > scores[1]:
            print(f"{players[0]} is the winner")
            nextGame = False 
        elif scores[1] > scores[0]:
            print(f"{players[1]} is the winner")
            nextGame = False
        else:
            print("It is a tie. Rematch!")
            nextGame = True 
        
        # display final board
        print()
        printBoard(board)
        print()

        # print final score tally
        print(f"Final score: {players[0]}({scores[0]}) {players[1]}({scores[1]})")
        print()
