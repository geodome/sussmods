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

# question 1a

def q1a(s: str):
    if len(s) == 8 and s[:3].isupper() and s[4:8].isdigit() and s[7] in ("S", "X" "Z"):
        print("valid")
    else:
        print("invalid")

q1a("ABC4567S")
q1a("ABC45678")

# question 1b

def q1b(n: int):
    width = len(str(n*n))
    for i in range(1, n+1):
        for j in range(i, n*i+1, i):
            print(str(j).rjust(width), end=" ")
        print()

q1b(8)

# question 2a
def getDuration(duration: str) -> int:
    h, m = duration.split(":")
    h, m = int(h), int(m)
    return h*60 + m

print(getDuration("1:20"))

# question 2b
def computeCharge(minutes: int) -> float:
    if minutes <= 10:
        return 0.0
    if 10 < minutes <= 60:
        return 1.50
    return min(5, 1.5 + (minutes - 60) * 0.02)

print(computeCharge(15))
print(computeCharge(35))
print(computeCharge(70))
print(computeCharge(360))

#question 2c
def q2c():
    while True:
        duration = input("Enter duration: ").strip()
        if len(duration) == 0:
            break
        minutes = getDuration(duration)
        print(str(minutes), "parking.", end= " ")
        charge = computeCharge(minutes)
        if charge == 0.0:
            print("No charge")
        else:
            print("Please pay", str(charge))

# question 3a
def q3a():
    qtyPrice = [2, 1.5, 4, 0.5, 1, 2.5 , 3, 2.0]
    items = len(qtyPrice)//2
    total = 0
    for i in range(0,len(qtyPrice),2):
        qty = qtyPrice[i]
        price = qtyPrice[i+1]
        subtotal = qty * price
        print(str(qty).rjust(2, "0"), "x", str(price).rjust(3), "= $", str(subtotal).rjust(3))
        total += qty * price
    print(str(items).rjust(2,"0"), "items")
    print(f"Total price ${total:.2f}")

q3a()

# question for 3b
def q3b():
    numlist = []
    while len(numlist) < 5:
        numstr = input("Enter num: ").strip()
        if len(numstr) == 0:
            break
        num = int(numstr)
        if len(numlist) == 0:
            numlist.append(num)
        else:
            if num <= numlist[0]:
                numlist.insert(0, num)
            elif num >= numlist[-1]:
                numlist.append(num)
            else:
                for i in range(len(numlist)-1):
                    if numlist[i] <= num <= numlist[i+1]:
                        numlist.insert(i+1, num)
                        break
        print(numlist)

# q3b()

# question 4a
def readFile() -> dict[str, list[str]]:
    seatingPlan: dict[str, list[str]]= {}
    with open("seating.txt") as f:
        for line in f:
            cols = line.split(",")
            seatingPlan[cols[0]] = cols[1:]
    return seatingPlan 

# question 4b
def displaySeatingPlan(seatingPlan: dict[str, list[str]]):
    # assume each row is labelled A-Z, max 9 seats per row
    rows = sorted(seatingPlan.keys())
    # assume every row has the same number of seats
    ncols = len(seatingPlan[rows[0]])
    for row in rows:
        cols = seatingPlan[row]
        print(row, " ".join(cols))
    print(" ", " ".join([str(i+1) for i in range(ncols)]))
    
seatingPlan = {'A':['O','X','O','X'], 'B':['O','O','O','X'], 'C':['O','X','O','O'] }
displaySeatingPlan(seatingPlan)

# question 4c
def bookingmenu(seatingPlan: dict[str, list[str]]):
    while True:
        seatno = input("Emter seat no: ")
        row, col = seatno[0], int(seatno[1:]) - 1
        num = int(input("Enter number of seats to book: "))
        # first check seat availability
        available = True
        for n in range(num):
            if seatingPlan[row][col + n] == "X":
                available = False
                break
        if not available:
            print("Not available")
        else:
            # proceed to book
            for n in range(num):
                seatingPlan[row][col + n] = "X"
            print("Seats successfully allocated")

