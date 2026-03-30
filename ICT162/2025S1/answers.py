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
Q1a(i)
The output is:
A running job 1
B running job 2

Q1a(ii)
The output is:
C running job 1
B running job 2

Q1a(iii)
This causes an error as A.job2() is an undefined abstract method.

Q2

p.cost = 3
p.method1() = f"{p.specialty()} ${p.cost}" = "Chendol $3"

c.cost = 6
c.method1() = f"{c.specialty()} ${c.cost}" = f"{"Durian " + super().speciality()} ${c.cost}" = "Durian Chendol $6"

gc.cost = 8
gc.method1() = f"Ice Cream {gc.specialty()} ${gc.cost}" = f"Ice Cream Durian Chendol $8"

ggc.cost = 10
ggc.method1() = f"Ice Cream {ggc.specialty()} ${ggc.cost}" = f"Ice Cream Durian Chendol $10"

The output of main() is:

Chendol $3
Durian Chendol $6
Ice Cream Durian Chendol $8
Ice Cream Chocolate Durian Chendol $10
"""

# Question 3a

class CapitaStar:

    def __init__(self, phone:int, name:str):
        self.__phone = phone 
        self.__name = name 
        self.__starDollars = 0
    
    @property
    def starDollars(self) -> int:
        return self.__starDollars
    
    @starDollars.setter
    def starDollars(self, newValue:int) -> None:
        self.__starDollars = newValue
    
    def addStarDollars(self, amountSpent:float):
        if amountSpent > 10:
            self.__starDollars += int(amountSpent)
    
    def redeemStarDollars(self, dollars:int) -> bool:
        if self.__starDollars >= dollars:
            self.__starDollars -= dollars 
            return True 
        return False
    
# Question 3b

class CapitaCard(CapitaStar):

    _FACTOR = 6
    _MONTHLY_CAP = 1200

    def __init__(self, phone:int, name:str, cardNumber:str) -> None:
        super().__init__(phone, name)
        self.__cardNumber = cardNumber
        self.__remainingCap = CapitaCard._MONTHLY_CAP
    
    def resetCap(self):
        self.__remainingCap = CapitaCard._MONTHLY_CAP
    
    def addStarDollars(self, amountSpent:float) -> None:
        if amountSpent > 10:
            capped = min(int(self.__remainingCap). int(amountSpent))
            uncapped = max(0, int(amountSpent - self.__remainingCap))
            self.__remainingCap = max(0, self.__remainingCap - amountSpent)
            self.__starDollars += CapitaCard._FACTOR*capped + uncapped 

"""
Question 3c

The addStarDollars(float) method was overrided by replacement. In this method, 
super().addStarDollars(float) was not invoked at all.

"""

# Question 4a

class ExpenseException(Exception):
    pass

# Question 4b

class Expense:

    def __init__(self, merchantName:str, amount:float, expenseType:str, isCapitaStar:bool) -> None:
        if expenseType not in BudgetPlan._TYPE_BUDGET:
            raise ExpenseException()
        self.__merchantName = merchantName
        self.__amount = amount 
        self.__expenseType = expenseType
        self.__isCapitaStar = isCapitaStar
    
    @property 
    def amount(self) -> float:
        return self.__amount
    
    @property
    def expenseType(self) -> str:
        return self.__expenseType
    
    @property 
    def isCapitaStar(self) -> bool:
        return self.__isCapitaStar
    
    def __str__(self) -> str:
        return f"Merchant: {self.__merchantName} \t Amount: ${self.__amount} \t Type: {self.__expenseType}"
 
# Question 5a

class BudgetPlan:
    _TYPE_BUDGET = {"Food":800, "Education":500, "Travel":300, "Others":200}

    def __init__(self, capitaStar:CapitaStar):
        self.__expenses: list[Expense] = []
        self.__capitaStar = capitaStar
    
    @classmethod
    def listBudget(cls):
        items = []
        for item, budget in cls._TYPE_BUDGET:
            item.append(f"{item.ljust(15)} ${budget}")
        return "\n".join(items)
    
    @classmethod 
    def updateBudgetByType(cls, type:str, budget:float):
        cls._TYPE_BUDGET[type] = budget

    def add(self, expense:"Expense") -> None:
        # implementation not required 
        pass

    def listExpenses(self, expenseType:str) -> list:
        # implementation not required
        pass 

# Question 5b

import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext

class BudgetGUI:

    def __init__(self):
        self.__win = tk.Tk()
        self.__win.resizable(True, True)
        self.__win.title("MY Budget Plan")
        self.create_widgets()
        self.__win.mainloop()
    
    def create_widgets(self):
        dataFrame = ttk.Frame(self.__win)
        dataFrame.grid(row=0,column=0, padx=0, pady=0)

        type_lbl = ttk.Label(dataFrame, text="Type: ")
        type_lbl.grid(row=0, column=0, sticky="W")
        self.__type = tk.StringVar()
        self.__type_Ety = ttk.Entry(dataFrame, width=15, textvariable=self.__type)
        self.__type_Ety.grid(row=0, column=1, sticky='W', padx=4, pady=4)
    
        budget_lbl = ttk.Label(dataFrame, text="Budget : $")
        budget_lbl.grid(row=1, column=0, sticky='W')
        self.__budget = tk.StringVar()
        self.__budget_Ety = ttk.Entry(dataFrame, width=8, textvariable=self.__budget)
        self.__budget_Ety.grid(row=1,column=1, sticky="W", padx=4, pady=4)

        self.__list_btn = ttk.Button(dataFrame, text="list budget", command=self.list)
        self.__list_btn.grid(row=2, column=0, padx=4, pady=4)
        self.__update_btn = ttk.Button(dataFrame, text="add/update", command=self.update)
        self.__update_btn.grid(row=2, column=1, padx=4, pady=4)

        outputFrame = ttk.Frame(self.__win)
        outputFrame.grid(row=1, column=0, padx=9, pady=4, columnspan=2)
        self.__scrol_stxt = scrolledtext.ScrolledText(outputFrame, width=35, height=10, wrap=tk.WORD)
        self.__scrol_stxt.grid(row=0,column=0,sticky='WE')
        self.__scrol_stxt.config(state=tk.DISABLED)
        self.__type_Ety.focus()
    
    def list(self):
        """
        Required for 5b
        """
        self.__scrol_stxt.config(state=tk.NORMAL)
        self.__scrol_stxt.delete("1.0", tk.END)
        self.__scrol_stxt.insert('1.0', BudgetPlan.listBudget() + "\n")
        self.__scrol_stxt.config(state=tk.DISABLED)

    def update(self):
        """
        Required for 5b
        """
        type = self.__type.get().strip()
        budget = self.__budget.get().strip()

        self.__scrol_stxt.config(state=tk.NORMAL)

        # test for blank 
        type_is_blank = type == ""
        budget_is_blank = budget == ""
        if(budget_is_blank or type_is_blank):
            if type_is_blank:
                self.__scrol_stxt.insert(tk.INSERT, "Type should not be blank.\n")
            if budget_is_blank:
                self.__scrol_stxt.insert(tk.INSERT, "Budget should not be blank.\n")
        else:        
            # test for valid budget value
            budget_numeric = float(0)
            try:
                budget_numeric = float(budget)
            except ValueError:
                self.__scrol_stxt.insert(tk.INSERT, "Invalid inputs. Try again.\n")
            else:
                if budget_numeric <= 0:
                    self.__scrol_stxt.insert(tk.INSERT, "Budget should be positive.\n")
                else:
                    BudgetPlan.updateBudgetByType(type, budget_numeric)
                    self.__scrol_stxt.insert(tk.INSERT, f"Budget for {type} is now ${budget_numeric}\n")

        self.__scrol_stxt.config(state=tk.DISABLED)