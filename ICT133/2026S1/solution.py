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
