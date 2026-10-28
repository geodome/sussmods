# Questiun 1

def q1():
    charger = input("Enter charger type (AC/DC): ").strip().upper()
    if not(charger == "AC" or charger == "DC"):
        print("Wrong charger type. Please run the program again.")
    else:
        kwh = float(input("Energy delivered: "))
        if charger == "DC":
            amount = kwh * 0.68
        else:
            amount = 0
            if kwh < 20:
                amount += kwh * 0.56
            else:
                amount += 20 * 0.56
            if kwh < 50:
                amount += (kwh - 20) * 0.54
            else:
                amount += 30 * 0.54
            if kwh > 50:
                amount += (kwh - 50) * 0.52            

        print(f"Please pay {amount:.2f}")

# Question 2

def planA_with_deposit_cap() -> None:
    """
    Solution for 2a
    """
    deposit = int(input("Enter initia deposit amount: "))
    if not ( 0 < deposit <= 30000):
        print("Error! Amount  is up to 30k")
    else:
        age = int(input("Enter age of deposit: "))
        if not (1 <= age <= 100): 
            print("Error! Age must be between 1 and 100 inclusive")
        else:
            rate = float(input("Enter interest rate in %: "))
            balance = deposit
            interest = 0
            print( f"{'age':3}   {'balance':7}  {'interest':7}  {'End of Year':7}")
            while age <= 70:
                interest = rate/100 * balance
                print(f"{age:3}   {balance:7.0f}   {interest:7.0f}   {(balance + interest):7.0f}")
                balance += interest 
                age += 1

def calculate_interest(balance, rate):
    return min(balance, 30000)*rate/100 + min(max(balance - 30000, 0), 30000)*max(0, (rate - 1))/100  + max(balance-60000, 0)*max(0, (rate - 2))/100

def calculate_balance(age:int, payout_age:int, deposit:float, rate:float) -> float:
    """
    Solutin for 2a
    """
    balance = deposit
    interest = 0
    print( f"{'age':>3}  {'balance':>12}  {'interest':>12}  {'End of Year':>12}")
    while age < payout_age:
        interest = calculate_interest(balance, rate)
        print(f"{age:3}  {balance:12.0f}  {interest:12.0f}  {(balance + interest):12.0f}")
        balance += interest 
        age += 1
    return balance

def planA_without_deposit_cap() -> None:
    """
    Solution for 2b
    """
    deposit = int(input("Enter initial deposit amount: "))
    if deposit < 0:
        print("Error! Amount  must be positive.")
    else:
        age = int(input("Enter age of deposit: "))
        if not (1 <= age <= 100): 
            print("Error! Age must be between 1 and 100 inclusive")
        else:
            rate = float(input("Enter interest rate in %: "))
            balance = calculate_balance(age, 71, deposit, rate)

def payout(payout_age: int, balance: float, rate: float, withdrawal: float) -> int:
    age = payout_age
    while balance > 0:

def planA_with_payout() -> None:
    payout_age = int(input("Enter payout age: "))
    if not 1 <= payout_age <= 100:
        print("Error. Invalid age")
    else:
        withdrawal = float(input("Enter yearly withdrawal: "))
        if withdrawal <= 0:
            print("Error. Invalid withdrawal amount")
        else:
            deposit = int(input("Enter initial deposit amount: "))
            if deposit < 0:
                print("Error! Amount  must be positive.")
            else:
                age = int(input("Enter age of deposit: "))
                if age >= payout_age:
                    print("Error. You cannot withdraw before depositing")
                elif not (1 <= age <= 100): 
                    print("Error! Age must be between 1 and 100 inclusive")
                else:
                    rate = float(input("Enter interest rate in %: "))
                    balance = calculate_balance(age, payout_age, deposit, rate)
                    end_of_plan = payout(payout_age, balance, rate, withdrawal)
                    print(f"Payout ends at age {end_of_plan}")

