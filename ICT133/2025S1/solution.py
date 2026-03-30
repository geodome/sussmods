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

# Question 1
def q1():
    years = float(input("Enter years of experience: "))
    if years < 2:
        level = "Junior"
    elif years >= 2 and years < 5:
        level = "Mid-level"
    else:
        level = "Senior"
    print(f"Employee category is {level}.")

# Question 2
def q2(input_str:str):
    for i in range(len(input_str)):
        print(input_str[:i+1])

# Question 3a
def deductWords(word1:str, word2:str) -> list[str]:
    """
    Basic solution, sufficient for passing ICT133, with quadratic time complexity.
    """
    w1 = list(word1)
    for i in range(len(w1)-1,-1,-1):
        if w1[i] in word2:
            del w1[i]
    return w1

def deductWords2(word1:str, word2:str) -> list[str]:
    """
    Advanced solution for 3a, with log-linear time complexity. The bottleneck is sorting the words
    into alphabetical order, with log-linear time complexity; but the filtering process of removing
    letters of the 2nd word from the 1st word has linear time complexity.
    """
    # sort each word
    # Python uses Tim Sort with log linear time complexity
    w1 = sorted(word1)
    w2 = sorted(word2)
    # begin filtering
    filtered = []
    p1, p2 = 0, 0
    while p1 < len(w1) and p2 < len(w2):
        if w1[p1] < w2[p2]:
            while p1 < len(w1) and w1[p1] < w2[p2]:
                filtered.append(w1[p1])
                p1 += 1
        elif w1[p1] > w2[p2]:
            while p2 < len(w2) and w1[p1] > w2[p2]:
                p2 += 1
        else:
            d = w2[p2]
            while p1 < len(w1) and w1[p1] == d:
                p1 += 1
            while p2 < len(w2) and w2[p2] == d:
                p2 += 1            
    # append remaining unfiltered letters in w1
    if p1 < len(w1):
        for c in w1[p1:]:
            filtered.append(c)
    return filtered

# Question 3b
def q3b():
    while True:
        word1 = input("Enter 1st Word: ").strip().lower()
        if word1.upper() == "X":
            print("bye")
            break
        word2 = input("Enter 2nd word: ").strip().lower()
        result = deductWords(word1, word2)
        if len(result) == 0:
            print("Nothing left")
        else:
            resultStr = ", ".join(result)
            print(f"{len(result)} remaining characters: {resultStr}")

"""
Question 4

The guessWhat(numList1, numList2) essentially creates a new list with each element i 
is the multiplication result of element i in numlist1 and element i of numlist2
When there is no corresponding element i in numList2, then the result is 0.

The output are:
[3, 8]
[6, 12, 20]
[12, 12, 0]
[2, 6]
[0]
"""

"""
Question 5

The python code is counting the frequency of each letter as the first 
letter of each word. The caveat here is when printing the dictionary,
the key order is not deterministic.

The output is:
{"a": 1}
{"a": 1, "b": 1}
("a": 2, "b": 1)
{"a": 2, "b": 1, "g":1}
{"a": 2, "b": 1, "c":1, "g":1}
{"a": 3, "b": 1, "c":1, "g":1}
{"a": 3, "b": 2, "c":1, "g":1}
{"a": 3, "b": 3, "c":1, "g":1}

"""

# Question 6a

def readStudentData() -> dict[str,dict[str,list[float]]]:
    data: dict[str,dict[str,list[float]]] = dict()
    with open("student.txt") as f:
        for line in f:
            student_id = line.strip()
            data[student_id] = {"PCQ1": [], "PCQ2":[], "PCQ3":[]}
    return data

# Question 6b

def loadAssessmentData(data:dict[str,dict[str,list[float]]]):
    with open("assessment.txt") as f:
        for line in f:
            student_id, test, score = line.strip().split(",")
            if len(data[student_id][test]) < 3:
                data[student_id][test].append(float(score))

# Question 6c

def writeSummary(result:dict[str,dict[str,list[float]]]):
    with open("summary.txt", "w") as f:
        for student_id in result:
            for test in ["PCQ1", "PCQ2", "PCQ3"]:
                pcq = result[student_id][test]
                if len(pcq) == 0:
                    final = "No Attempt"
                else:
                    final = max(pcq)
                print(f"{student_id} {test} {final}", file=f)
            
