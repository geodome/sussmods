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

from abc import ABC, abstractmethod 

class DeliveryPartner(ABC):
    """1(a)"""

    _FEES_PER_ROUND = 32

    def __init__(self, callSign:str, name:str) -> None:
        self._callSign = callSign
        self._name = name
    
    @property 
    def name(self) -> str:
        return self._name 
    
    @property
    def callSign(self) -> str:
        return self._callSign
    
    @abstractmethod
    def computePay(self, rounds:int)->float:
        pass 

    def __str__(self) -> str:
        return f"Name: {self._name}  CallSign: {self._callSign}"

class FullTimeDeliveryPartner(DeliveryPartner):
    """1(b)"""

    def __init__(self, callSign:str, name:str, basicSalary:float) -> None:
        super().__init__(callSign, name)
        self._basicSalary = basicSalary
    
    def computePay(self, rounds: int) -> float:
        return self._basicSalary + rounds*DeliveryPartner._FEES_PER_ROUND
    
class PartTimeDeliveryPartner(DeliveryPartner):
    """1(b)"""

    _BONUS_ROUNDS = 30
    _BONUS_RATE = 1.85

    def computePay(self, rounds: int) -> float:
        if rounds <= PartTimeDeliveryPartner._BONUS_ROUNDS:
            return rounds * DeliveryPartner._FEES_PER_ROUND
        return PartTimeDeliveryPartner._BONUS_ROUNDS*DeliveryPartner._FEES_PER_ROUND + (rounds - PartTimeDeliveryPartner._BONUS_ROUNDS)*(DeliveryPartner._FEES_PER_ROUND * PartTimeDeliveryPartner._BONUS_RATE)

# 1(c)
def question_1c():
    d1 = PartTimeDeliveryPartner("DP-007", "Lim Lim Kee")
    d2 = FullTimeDeliveryPartner("Maverick", "Tom Yam Kong", 1200)
    drivers: list[tuple[DeliveryPartner, int]] = [(d1, 50), (d2, 40)]
    for d, rounds in drivers:
        print(f"{d.name} is paid ${d.computePay(rounds)}")

# 2(a)

class OrderException(Exception):
    pass

# 2(b)

class Customer:
    pass 

class Pizza:
    pass

class Order:

    _NEXT_ORDER_ID = 1
    _MAX_PIZZA = 12

    @classmethod
    def nextId(cls, self) -> int:
        id = cls._NEXT_ORDER_ID
        cls._NEXT_ORDER_ID += 1
        return id
    
    def __init__(self, customer:Customer, pizza:Pizza, qty:int) -> None:
        self._orderID = Order.nextId()
        self._customer = customer
        self._items: list[list[Pizza,int]] = []
        if qty > Order._MAX_PIZZA:
            raise OrderException(f"Cannot order more than {Order._MAX_PIZZA} pizzas")
        self._items.append([pizza, qty])
    
    @property
    def totalPrice(self) -> float:
        total = 0
        for pizza, qty in self._items:
            total += qty * pizza.price 
        return total
    
    @property
    def pizaCount(self) -> int:
        count = 0
        for _, qty in self._items:
            count += qty
        return qty 
    
    def addPizza(self, name:str, size:str, price:float, qty:int) -> None:
        for i in range(len(self._items)):
            pizza, _ = self._items[i]
            if pizza.name == name and pizza.size == size:
                self._items[i][1] += qty
                return
        self._items.append([Pizza(name, size, price), qty])
    
    def __str__(self) -> str:
        output = [f"Order ID: {self._orderID} \n"]
        for pizza, qty in self._items:
            output.append(f"{pizza.name} - {pizza.size} - ${pizza.price:.2f} x {qty}")
        output.append(f"Tota;l price: {self.totalPrice}")
        return "\n".join(output)

# 2(c)

def main():
    o1 = Order(Customer("Herro Tan","999A, Sentosa Cove", 99123665), Pizza("Hawaiian Plus", "M", 9.59), 1)
    orders: list[tuple[str,str,float,int]] = [ ("Super Supreme", "L", 12.59,3), ("Hawaiian Plus", "M", 9.59, 3), ("Chicken Satay", "L", 11.59, 6) ]
    for name, size, price, qty in orders:
        try:
            o1.addPizza(name, size, price, qty)
        except OrderException as e:
            print(e)


# Question 3

# 3(a)

from datetime import datetime 

class DeliveryRound:

    def __init__(self, roundName:str, deliveryPartner:DeliveryPartner) -> None:
        self._roundName = roundName
        self._deliveryPartner = deliveryPartner
        self._deliveryDateTime:datetime = datetime.now()
        self._orders: list[Order] = []
    
    @property
    def deliveryPartner(self) -> DeliveryPartner:
        return self._deliveryPartner
    
    def addOrder(self, newOrder:Order):
        count = 0
        for o in self._orders:
            count += o.pizaCount()
        if count + newOrder.pizaCount() > 12:
            raise OrderException("DeliveryRound cannot exceed 12 pizzas")
        self._orders.append(newOrder)

"""
3(b)

DeliveryRound and Order: 
Composition. Each DeliveryRound object contains a list of orders.

DeliveryRound and FullTimeDeliveryPartner: 
Composition. Each delivery round is assigned to a full time delivery partner.

DeliveryRound and Pizza: 
Nested composition. Each delivery round contains a list of orders whereby each order represents a quantity of pizzas.

3(c)

The addPiza() method of the Order class should not be creating a new Pizza object. Instead, it should retrieve a unique
Pizza object from a singleton catalog of pre-created Pizza objects based on name and size. In this way, we can ensure 
data consistency on name, price, size when it comes to ordering pizza.

"""

# Question 4

import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 
 
class DrawRectangleGUI: 

    def __init__(self): 
        self._win = tk.Tk() 
        self._win.resizable(True, True)
        self._win.title("Draw me a rectangle") 
        self.create_widgets() 
        self._win.mainloop() 
 
    def create_widgets(self): 
        dataFrame = ttk.Frame(self._win) 
        dataFrame.grid(row=0, column=0, padx=8, pady=4) 
      
        width_lbl = ttk.Label(dataFrame, text="Width:") 
        width_lbl.grid(row=0, column=0, sticky='W') 
 
        self._width_Ety = ttk.Entry(dataFrame, width=5) 
        self._width_Ety.grid(row=0, column=1, padx=4, pady=4) 
 
        height_lbl = ttk.Label(dataFrame, text="Height:") 
        height_lbl.grid(row=1, column=0, sticky='W') 
 
        self._height_Ety = ttk.Entry(dataFrame, width=5) 
        self._height_Ety.grid(row=1, column=1, padx=4, pady=4) 
 
        radioFrame = ttk.Frame(dataFrame) 
        radioFrame.grid(row=2, column=1, padx=8, pady=4) 
 
        self._radValue = tk.IntVar() 
        self._radValue.set(0) 
         
        self._hash_rdbtn = ttk.Radiobutton(radioFrame, text='#', 
                                       variable=self._radValue, value=0) 
        self._at_rdbtn = ttk.Radiobutton(radioFrame, text='@', 
                                       variable=self._radValue, value=1) 
         
        self._hash_rdbtn.grid(row=0, column=0, padx=8, pady=4) 
        self._at_rdbtn.grid(row=0, column=1, padx=8, pady=4) 
 
        self._draw_btn = ttk.Button(dataFrame, text="draw", command=self.draw) 
        self._draw_btn.grid(row=3, column=0, padx=4, pady=4) 
 
        self._clear_btn = ttk.Button(dataFrame, text="clear", command=self.clear) 
        self._clear_btn.config(state=tk.DISABLED) 
        self._clear_btn.grid(row=3, column=1, padx=4, pady=4) 
 
        outputFrame = ttk.Frame(self._win) 
        outputFrame.grid(row=1, column=0, padx=8, pady=4, columnspan=2) 
      
        self._scrol_stxt = scrolledtext.ScrolledText(outputFrame, 
                                                    width=50, height=12, 
                                                    wrap=tk.WORD) 
        self._scrol_stxt.grid(column=0, row=0, sticky='WE') 
        self._scrol_stxt.config(state=tk.DISABLED) 
        self._width_Ety.focus() 
 
    def _display(self, msg:str) -> None:
        self._scrol_stxt.config(state=tk.NORMAL)
        self._scrol_stxt.insert("end", msg+"\n")
        self._scrol_stxt.config(state=tk.DISABLED)

    def draw(self): 
        # missing codes to draw the rectangle 
        # first check for valid width and height
        width = self._width_Ety.get().strip()
        height = self._height_Ety.get().strip()
        if width == "" or height == "":
            self._display("Height or weight is missing")
        elif not (width.isnumeric() and height.isnumeric()):
            self._display("Enter only numbers for height and width.")
        elif (int(width) < 0 or int(height) < 0):
            self._display("Height or width should be positive")
        else:
            symbol = ["#","@"][self._radValue.get()]
            nwidth = int(width)
            nheight = int(height)
            for _ in range(nheight):
                self._display(symbol*nwidth)
        self._clear_btn.config(state=tk.NORMAL)

    def clear(self): 
        # missing codes to clear and reset the GUI 
        # clear scrolled text
        self._scrol_stxt.config(state=tk.NORMAL)
        self._scrol_stxt.delete("1.0", "end")
        self._scrol_stxt.config(state=tk.DISABLED)
        # clear width and height entries
        self._width_Ety.delete(0, "end")
        self._height_Ety.delete(0, "end")
        # disable clear button
        self._clear_btn.config(state=tk.DISABLED)