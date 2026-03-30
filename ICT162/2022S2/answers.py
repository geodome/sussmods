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

#   q1a
#   A movie card of price 70 is created and the number of tickets it holds is printed. The output is 10.

#   1b
#   Line 24. This error occurs because self._tickets was computed with MovieCard._TICKET_COUNT instead of HSBCMovieCard._TICKET_COUNT
#   To fix this, append the following line to the constructor of HSBCMovieCard:
#   self._tickets = HSBCMOvieCard._TICKET_COUNT[price]

#   q1c
#   There is no setter method for MovieCard.tickets. To fix this, add the following method to the MovieCard class
#   
#   @tickets.setter
#   def tickets(self, t):
#       self._tickets = t

#   q1d
#
#   add the following class method to the HSBCMovieCard Class
#   @classmethod
#   def addOffer(cls, price, tickets):
#       HSBCMovieCard._TICKET_COUNT[price] = tickets
#
#   add the following class method to the MovieCard Class
#   @classmethod
#   def addOffer(cls, price, tickets):
#       MovieCard._TICKET_COUNT[price] = tickets

#   q2a

from abc import ABC, abstractmethod

class FoodItem(ABC):
    def __init__(self, name:str, cost:float) -> None:
        self._name = name
        self._cost = cost
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def cost(self) -> float:
        return self._cost
    
    @abstractmethod
    def expiryHours(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Name: {self._name} \t Price: ${self._cost:.2f} \t Expiring in {self.expiryHours():.1f} hrs"


#   q2b

class Sandwich(FoodItem):
    def __init__(self, name:str, filling:str, cost:float):
        FoodItem.__init__(self, name, cost)
        self._filling = filling
    
    @property
    def filling(self) -> str:
        return self._filling
    
    def expiryHours(self) -> float:
        return 2

class HotSandwich(Sandwich):
    def __init__(self, name:str, filling:str, cost:float, toasted:bool) -> None:
        Sandwich.__init__(self, name, filling, cost)
        self._toasted = toasted

    def expiryHours(self) -> float:
        if self._toasted:
            return 1.5
        return super().expiryHours()

#   q2c
#   While the method names and signatures remain the same, the underlying implementation differs. This is known as method overloading
#   and the OO concept is called polymorphism.

#   q2d

def q2d():

    # i
    toastedCheese = HotSandwich("Toasted Cheese Sandwich", "cheese", 3.9, True) 
    hotPastrami = HotSandwich("Hot Pastrami Sandwich", "pastrami", 4.8, False)
    coldCut = Sandwich("Cold Cut Sandwich", "cold cut", 4.5)

    # ii
    # The output should be 1.5.
    print(toastedCheese.expiryHours())

#   q3

class Dessert(FoodItem):
    """
    Not required for exam. Added for VSCode hinting
    """
    def __init__(self, name:str, storageTemperature:str, cost:float):
        FoodItem.__init__(self,name, cost)
        self._storageTemperature = storageTemperature
    
    def expiryHours(self) -> float:
        return 2
    
#   q3a

class SnackBoxException(Exception):
    pass

#   q3b

class SnackBox:
    _MIN_ITEMS = 1
    _MAX_ITEMS = 4

    def __init__(self, name:str, fooditem: FoodItem):
        self._name = name
        self._fooditems = [fooditem]
        self._price = fooditem.cost
        self._consumeBy = fooditem.expiryHours()
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def consumeBy(self) -> float:
        return self._consumeBy
    
    def addItem(self, item: FoodItem) -> None:
        if len(self._fooditems) < SnackBox._MAX_ITEMS:
            self._consumeBy = min(self._consumeBy, item.expiryHours())
            self.price += item.cost
            self._fooditems.append(item)
        raise SnackBoxException(f"Cannot add {item.name}. Snack Box has hit max size.")
    
    def removeItem(self, name:str) -> None:
        for i in range(len(self._fooditems)):
            item = self._fooditems[i]
            if item.name == name:
                if len(self._fooditems) == SnackBox._MIN_ITEMS:
                    raise SnackBoxException(f"Cannot remove {name}. Snack Box is of min size.")
                del self._fooditems[i]
                self._consumeBy = min([i.expiryHours() for i in self._fooditems])
                self._price -= item.cost
                break
        else:
            raise SnackBoxException(f"Cannot remove {name}. No such item in Snack Box")
        

    def __str__(self) -> str:
        items = [i.name for i in self._fooditems]
        return f"Name: {self._name} \t Price: {self._price} \t Consume in f{self._consumeBy:.1f} hrs \t with {', '.join(items)}"

#   q3c
#   List is the choice of collection. A list can be used to perform search and maintains the order of which individual 
#   food items are added.

#   q3d

def q3d():

    # i
    chendol = Dessert("Chendol", 4, 3.5)
    chengteng = Dessert("Cheng Teng", 16, 3.2)
    icekachang = Dessert("Ice Kachang", 4, 3.5)
    puluthitam = Dessert("Pulut Hitam", 38, 3.5)
    burburchacha = Dessert("Bubur Cha Cha", 38, 4.2)

    # ii
    sb1 = SnackBox("His Desserts", chendol)
    sb2 = SnackBox("Her Desserts", chengteng)
    
    # iii
    for item in [icekachang, puluthitam, burburchacha]:
        try:
            sb1.addItem(item)
        except SnackBoxException as e:
            print(e)
    
    # iv
    try:
        sb2.removeItem(chengteng.name)
    except SnackBoxException as e:
        print(e)
    
    # v
    # Name: His Snack   Price: $ 13.70    Consume in 2.0 hrs    with Chendol, Ice Kachang, Pulut Hitam, Burbur Chacha
    # Name: Her Sback   Price: $  3.20    Consume in 2.0 hrs    with Cheng Teng


#   q4a

import tkinter as tk
from tkinter import ttk, scrolledtext

class ResultGUI:
    # q4b
    # The test data is added as a parameter of the Constructor.
    def __init__(self, data:dict[str,list[str]]=None):
        self._win = tk.Tk()
        self._win.geometry("330x250")
        self._win.title("ICT162 Result Enquiry")
        self._data = data
        self.create_widgets()
        self._win.mainloop()
    
    # q4a
    def create_widgets(self):
        """
        The problem with the original code is all components are placed in a 4x2 grid
        Instead, the components will be organised into 2 frames that are packed verticically.
        The first frame is called the dataFrame which holds all the GUI widgets for handling input
        The second frame is called the outputFrame which holds all the GUI widgets for displaying output

        Original GUI widget hierachy:
        self._win
        |_  self._lblId
        |_  self._txtId
        |_  self._rbtnAm
        |_  self._rbtnPm
        |_  btnFrame
            |_  self._btnEnquire
            |_  self._btnClear
        |_  self._sclText
        
        New GUI widget hierachy:
        self._win
        |_  dataFrame        
            |_  self._lblId
            |_  self._txtId
            |_  radioFrame
                |_  self._rbtnAm
                |_  self._rbtnPm
            |_  btnFrame
                |_  self._btnEnquire
                |_  self._btnClear
        |_  outputFrame
            |_  self._sclText
    
        """
        # create frames to contain GUI widgets
        dataFrame = tk.Frame(self._win)
        outputFrame = tk.Frame(self._win)
 
        # create widgets for dataFrame         
        self._lblId = ttk.Label(dataFrame, text='Student Id:') 
        self._lblId.grid(row=0, column=0, padx=4, pady=4) 

        self._studentID = tk.StringVar()
        self._txtId = ttk.Entry(dataFrame, width=20, textvariable=self._studentID)
        self._txtId.grid(row=0, column=1, columnspan=2, padx=4, pady=4)

        radFrame = ttk.Frame(dataFrame)
        self._rbtn = tk.IntVar()  
        self._rbtnAm = ttk.Radiobutton(radFrame, text='TMA', value = 0, variable=self._rbtn) 
        self._rbtnPm = ttk.Radiobutton(radFrame, text='TOA', value = 1, variable=self._rbtn)
        # take note if the parent frame uses grid, then the child frame must use grid.
        self._rbtnAm.grid(row=0, column=0)
        self._rbtnPm.grid(row=0, column=1)
        radFrame.grid(row=2, column=1, padx=4, pady=4)

        btnFrame = ttk.Frame(dataFrame) 
        # q4c. added self.enquire and self.clear as event handler for btnEnquire and btnClear
        self._btnEnquire = ttk.Button(btnFrame, text='Enquire', command=self.enquire) 
        self._btnClear = ttk.Button(btnFrame, text='Clear', command=self.clear)
        # take note if the parent frame uses grid, then the child frame must use grid.
        self._btnEnquire.grid(row=0,column=0)
        self._btnClear.grid(row=0,column=1)
        btnFrame.grid(row=3, column=1, padx=4, pady=4) 

        dataFrame.grid(row=0, column=0)


        # create widgets for outputFrame
        self._sclText = scrolledtext.ScrolledText(outputFrame, width=45, height=10) 
        self._sclText.config(state=tk.DISABLED) 
        self._sclText.pack(side=tk.TOP, padx=4, pady=4)
        outputFrame.grid(row=1,column=0)

        self._txtId.focus()
 
    # implemented for q4c
    def enquire(self): 
        self._sclText.config(state=tk.NORMAL)
        id = self._studentID.get().strip()
        if self._data is None:
            self._sclText.insert(tk.END, "No ICT162 TMA/TOA data is provided")
        elif id == "":
            self._sclText.insert(tk.END, "Enter Student Id and try again")
        else:
            assessment = ["TMA", "TOA"][self._rbtn.get()]
            for result in ["Pass", "Fail"]:
                if id in self._data[assessment][result]:
                    self._sclText.insert(tk.END, f"{assessment} result for ICT162: {result}")
                    break
            else:
                self._sclText.insert(tk.END, "You did not enroll for ICT162")
        self._sclText.config(state=tk.DISABLED)

    # implemented for q4c
    def clear(self):
        self._studentID.set("")
        self._sclText.config(state=tk.NORMAL)
        self._sclText.delete("1.0", tk.END)
        self._sclText.config(state=tk.DISABLED)
