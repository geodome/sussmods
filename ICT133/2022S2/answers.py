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

from typing import List, Tuple, Dict
import random

def q1a_i(n1: int, n2: int) -> bool:
    fair = 0.45 < n1/(n1 + n2) < 0.55
    return fair

def compare(s:str, i:int=-1, count_i:int=-1, j:int=-1, count_j:int=0) -> bool:
    #use recursion since looping is not allowed
    if i == -1:
        i, count_i = 0, 0
        j, count_j = len(s)-1, 0
    if i >= j:
        if count_i > count_j:
            print("MORE")
        elif count_i == count_j:
            print("SAME")
        else:
            print("LESS")
    elif i < j:
        if s[i] == "a":
            count_i += 1
        if s[j] == "a":
            count_j += 1
        compare(s, i+1, count_i, j-1, count_j)
        
def q1a_ii(s: str):
    compare(s)

# alternative solution for q1a_ii

def q1a_ii_alternative(s: str):
    midpoint = len(s) // 2
    h1 = s[:midpoint]
    if len(s) % 2 == 1:
        h2 = s[midpoint+1:]
    else:
        h2 = s[midpoint:]
    n1 = h1.count("a")
    n2 = h2.count("a")    
    if n1 > n2:
        print("MORE")
    elif n1 < n2:
        print("LESS")
    else:
        print("SAME")

def q1b_i(s1: str) -> str:
    s2 = ""
    prev = ""
    for i in s1:
        if i != prev:
            s2 += i # s2 = s2 + i
        prev = i
    return s2

# question 1c
# an expression is a statement that yields a value which may be passed to 
# another statement for further processing.
# 
# E.g. q1a i) fair = 0.45 < n1/(n1+n2) < 0.55
# 0.45 < n1/(n1+n2) < 0.55 is an expression that yields a boolean value that 
# is passed to the variable fair

def q1b_ii(w1, w2: str):
    if len(w2) > len(w1):
        # by pigeon-hole principle
        print("impossible")
    else:
        # count freq of each character in w1
        d1 = {}
        for c in w1:
            d1[c] = d1.get(c,0) + 1
        # count freq of each character in w2
        d2 = {}
        for c in w2:
            d2[c] = d2.get(c,0) + 1
        # to check if w2 can be made from w1
        possible = True
        for c in d2:
            if d2[c] > d1.get(c,0):
                # u cannot construct a word with 3a from a word with 2a.
                # d1.get(c,0) returns 0 if d1 doesn't contain character c
                print("impossible")
                possible = False
                break
        if possible:
            print("Possible")
         
def q2a(staffSalaryList: List[List[str, int]]):
    NO, SALARY = 0, 1
    # i
    staffSalaryList[0][SALARY] = 2500
    # ii
    updated = False
    for i in range(len(staffSalaryList)):
        if staffSalaryList[i][NO] == "p123":
            staffSalaryList[i][SALARY] = 3600
            print("updated")
            updated = True
            break
    if not updated:
        print("Unable to locate")
    # iii
    N = len(staffSalaryList)
    total = 0
    for staff in staffSalaryList:
        total += staff[SALARY]
    average = total/N
    for staff in staffSalaryList:
        if staff[SALARY] > average:
            print(staff[NO])
    # iv 
    # Print the staff number in descending order of salary and in ascending order of staff number
    # first sort staff by descending salary order
    staffSalaryList2 = sorted(staffSalaryList, key=lambda staff: staff[SALARY], reverse=True)
    # group staff with same salary in the same ground
    salaryGroups: List[List[str, int]] = []
    prevSalary = -1
    for staff in staffSalaryList2:
        if staff[SALARY] != prevSalary:
            salaryGroups.append([])
            prevSalary = staff[SALARY]
        salaryGroups[-1].append(staff)
    for group in salaryGroups:
        # sort each salary group in ascending order of staff number
        for staff in sorted(group, key=lambda staff: staff[NO]):
            print(staff[NO])

# question 2c
# a dictionary is better suited for looking up data identifiable by a key while a list is better
# suited for sorting.

# question 3a
# I would use a dictionary to store that data as a dictionary would allow me to look up the cost of
# alphabet by using the alphabet as a dictionary key. In this way, I don't have to iterate through
# every data entry to find which one matches the alphabet I am looking for.

def q2b_ii(staffSalaryList: List[Tuple[str, int]]):
    NO, SALARY = 0, 1
    # i
    staffSalaryDict = {}
    for no, salary in staffSalaryList:
        staffSalaryDict[no] = salary
    # ii
    print(len(staffSalaryDict))
    # iii
    if "p123" in staffSalaryDict:
        staffSalaryDict["p123"] = 3600
        print("Updated!")
    else:
        print("Unable to be located")
    # iv
    # ascending  order  of  salary  and  in ascending order of staff number if the salaries tie.
    staffSalaryList2: List[List[int, str]] = sorted(staffSalaryDict, key=lambda key: staffSalaryDict[key])
    # group staff with same salary in the same ground
    salaryGroups: List[Tuple[str, int]] = []
    prevSalary = -1
    for staff in staffSalaryList2:
        if staff[SALARY] != prevSalary:
            salaryGroups.append([])
            prevSalary = staff[SALARY]
        salaryGroups[-1].append(staff)
    for group in salaryGroups:
        # sort each salary group in ascending order of staff number
        for staff in sorted(group, key=lambda staff: staff[NO]):
            print(staff[NO])


def q3b(lines: str, costDict: Dict[str, int]) -> float:
    total = 0
    for line in lines.split("\n"):
        for c in line:
            if c in costDict:
                total += costDict[c]
    # Cents not making up to 5 cents should be removed. 
    discount = total % 5  
    return (total - discount) / 100
    # alternative formulation for discounted cost is
    # total = 5*(total//5) where // is integer division


# question 3c
def justifyLines(lines: str):
    # find  max width
    lineSplit = lines.split("\n")
    maxWidth = 0
    for line in lineSplit:
        if len(line) > maxWidth:
            maxWidth = len(line)
    # step 2
    centered = []
    for line in lineSplit:
        centered.append(line.center(maxWidth))
    return "\n".join(centered)

# question 4a
def checkSequence(line: str) -> bool:
    seq = line.split(",")
    detectedFirstInteger = False
    indexFirstInteger = -1
    firstInteger = -1
    for i in range(len(seq)):
        if detectedFirstInteger:
            if seq[i] != "-":
                if firstInteger + (i - indexFirstInteger) != int(seq[i]):
                    return False
        else:
            if seq[i] != "-":
                detectedFirstInteger = True
                indexFirstInteger = i
                firstInteger = int(seq[i])
    return True

# question 4b
def q4b():
    with open("output.txt", "w") as output:
        with open("input.txt") as input:
            for line in input:
                outcome = checkSequence(line.strip())
                print(outcome, file=output)

# question 4c
def generateSequence(length: int) -> str:
    if length < 1:
        return ""
    current = random.randint(1,20)
    seq = [str(current)]
    prevDash = False
    for _ in range(1, length):
        isDash = random.randint(1,100) > 50
        if isDash:
            current += 1
            seq.append("-")
            prevDash = True
        else:
            if prevDash:
                current += random.randint(0,1)
                prevDash = False
            current += 1
            seq.append(str(current))
    return ",".join(seq)


# question 4d
def main():
    while True:
        length = int(input("Enter length of sequence to generate and 0 to end: "))
        if length == 0:
            break
        elif length < 0:
            print("Length of sequence must be a positive number")
        else:
            seq = generateSequence(length)
            print(seq, ":", checkSequence(seq))