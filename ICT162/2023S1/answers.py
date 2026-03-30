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
#   f1 represents a full-time emploee Jim with Employee ID 102. Jim works from home
#   and his employee grade us 4. 
#
#   The second statement displays Jim's leave entitlement. The output is 22.

#   q1b
#   TypeError occurs because one cannot instantiate an abstract class. FullTimeEmployee
#   remains an abstract class because the method getLeaveEntitlement() is not implemented.
#   To fix, add the following method to the FullTimeEmployee class
# 
#   def getLeaveEntitlement(self):
#       return self.getPartTimeLeaveEntitlement()
#
#   q1c
#   The second line fails because there is no setter method for self._workFromHome.
#   Add the following method to the Employee class to fix
#
#   @workFromHome.setter
#   deg workFromHome(Self, workFromHome):
#       self._workFromHome = workFromHome
#
#   q1d
#   The error is on Line 47. The error is caused by getLeaveEntitlement() accessing 
#   FullTimeEmployee_LEAVE_ENTITLEMENT instead of Manager._LEAVE_ENTITLEMENT. To fix
#   this, add override getLeaveEntitlement() in the the Manager subclass with
#
#   def getLeaveEntitlement(self):
#       minLeave = min([leave for leave in Manager._LEAVE_ENTITLEMENT.values()])
#       return Manager._LEAVE_ENTITLEMENT.get(self._grade, minLeave)
#
#   q1e
#   In polymorphism, difference subclasses of the same parent class share the same interface,
#   ie. each method shares the same function signature while the underlying implementation
#   may be different. This polymorphism is demonstrated in Lines 44=47 whereby the the abstract
#   method getLeaveEntitlement() of the parent class is overed with a custom implementation in
#   the FullTimeEmployee class.

#   q2a
class Deli:
    _STANDARD_EXPIRY = 2
    _COOKING_STYLE_EXPIRY = [["Steam", "Grill", "Roast"], 1.5]

    def __init__(self, name:str, price:float, cookingStyle:str) -> None:
        self._name = name
        self._price = price
        self._cookingStyle = cookingStyle

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, newprice:float) -> None:
        self._price = newprice
    
    def expiryHours(self) -> int:
        styles, expiry = Deli._COOKING_STYLE_EXPIRY
        if self._cookingStyle in styles:
            return expiry
        return Deli._STANDARD_EXPIRY
    
    def __str__(self) -> str:
        p = f"{self._price:.2f}"
        h = f"{self.expiryHours():.1f}"
        return f"Name: {self._name<20} price: ${p:<5} Expiring in {h:<3} hours"

#   q2b

class ColdDeli(Deli):

    def __init__(self, name:str, cost:float, cookingStyle:str, storageTemperature:float) -> None:
        Deli.__init__(self, name, cost, cookingStyle)
        self._storageTemperature = storageTemperature
    
    def expiryHours(self) -> int:
        if self._storageTemperature <= 10:
            return 0.5
        elif self._storageTemperature <= 15:
            return 1.0
        elif self._storageTemperature <= 20:
            return 1.5
        else:
            return ColdDeli._STANDARD_EXPIRY
    
    def __str__(self):
        return Deli.__str__(self) + f" Store at {self._storageTemperature:.1f} degree celcius"
    
#   q2c
#   I use method overloading as the replacement methods share the same function names and 
#   function signatures but different underlying implementation. The OOP concept is polymorphism.

#   q2d
def q2d():
    # i
    pudding = ColdDeli("Srawberry Pudding", 2.00, "Whisk", 2.0)
    beef = Deli("Roast Beef", 3.90, "Roast")
    pie = Deli("Chicken Pie", 2.80, "Bake")
    cake = ColdDeli("Chocolate Steamed Cake", 1.50, "Steam", 15.0)

    # ii
    for item in [pudding, beef, pie, cake]:
        item.price += 0.2

    # iii
    # The output is 1.0

#   q3a
class DeliSetException(Exception):
    pass

#   q3b
class DeliSet:
    _MIN_DELI = 1
    _MAX_DELI = 4

    def __init__(self, name:str, deli:Deli) -> None:
        self._name = name
        self._deliList: list[Deli] = [deli]
        self._price = deli.price
        self._consumeBy = deli.expiryHours()
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def deliList(self) -> list[Deli]:
        return self._deliList
    
    @property
    def price(self) -> float:
        return self._price

    def addDeli(self, deli:Deli) -> None:
        if len(self._deliList) == DeliSet._MAX_DELI:
            raise DeliSetException(f"Max items in Deli Set. Cannot add {deli.name}")
        for d in self._deliList:
                if d.name == deli.name:
                    raise DeliSetException(f"Cannot add duplicate item {deli.name}")
        self._deliList.append(deli)
        self._price += deli.price
        self._consumeBy = min(self._consumeBy, deli.expiryHours())
    
    def removeDeli(self, deliName:str) -> Deli:
        if len(self._deliList) == DeliSet._MIN_DELI:
            raise DeliSetException("Min items in Deli Set. Cannot remove {deli.name}")
        for i in range(len(self._deliList)):
            if deliName == self._deliList[i].name:
                item = self._deliList.pop(i)
                self._price -= item.price
                if item.expiryHours() == self._consumeBy:
                    self._consumeBy = min([i.expiryHours() for i in self._deliList])
                return item
        raise DeliSetException("Cannot remove. {deliName} not found in Deli Set")
    
    def __str__(self) -> str:
        items = ", ".join([d.name for d in self._deliList])
        price = f"{self._price:.2f}"
        hours = f"{self._hours:.1f}"
        return f"Deli: {self._name:<20} Price: ${price<5} Consume in {hours:<4} hrs with {items}"

#   q3c
class DeliDispenser:
    """
    added DeliDispense class for VSCode hinitng
    """

    def __init__(self, name:str, deliInventory:list[Deli]) -> None:
        self._name = name
        self._deliInventory = deliInventory
    
    def searchDeli(self, name:str) -> Deli|None:
        pass

    def addDeli(self, deli:Deli):
        self._deliInventory.append(deli)

    def removeDeli(self, deliList:list[Deli]) -> bool:
        pass

    def listDeliInventory(self)  -> str:
        pass

#   q3c i
def createDeliSet(cafe:DeliDispenser) -> DeliSet|None:
    name = ""
    while name == "":
        name = input("Enter your customised set name: ")
    print("Available Deli")
    print(cafe.listDeliInventory())

    deliset:DeliSet = None
    itemNo = 1
    nextItem = True
    print("Select Deli by entering the name, <Enter> to stop.")
    while nextItem:
        deliName = input(f"Deli <{itemNo}>: ").strip()
        if deliName == "":
            nextItem = False
        else:
            foundItem = cafe.searchDeli(deliName)
            if foundItem is None:
                print("No such Deli. Select again.")
            else:
                if itemNo == 1:
                    deliset = DeliSet(name, foundItem)
                else:
                    try:
                        deliset.addDeli(foundItem)
                    except DeliSetException as e:
                        print(e)
                itemNo += 1

    if deliset is None:
        print("No Deli Set created")
    else:
        print(deliset)
        cafe.removeDeli(deliset.deliList)
    print()
    return deliset

#   q3c ii
def removeDeli(cafe:DeliDispenser, deliSet:DeliSet) -> None:
    print(deliSet)
    deliName = input("Enter Deli Name to remove: ").strip()
    try:
        item = deliSet.removeDeli(deliName)
    except DeliSetException as e:
        print(e)
    else:
        cafe.addDeli(item)
        print("Removed successfully. Please verify set.")
        print(deliSet)
    print()

#   q4a

from tkinter import *
from tkinter import scrolledtext
from tkinter.scrolledtext import *

#   q4
class BookingGUI:
    # q4c: the hardcoded booking data is passed into the constructor
    def __init__(self, booking:dict[str,list[str]]={}):
        self._booking = booking
        self._tk = Tk()
        self._tk.geometry('314x250')
        self._tk.title("Facility Booking")
        self.initWidgets()
        self._tk.mainloop()
    
    def initWidgets(self):
        self._lblId = Label(text="Member Id:")
        self._txtId = Entry(width=20)
        self._lblDate = Label(text="Booking Date:")
        self._txtDate = Entry(width=20)
        # q4a: created radioFrame and add radio buttons to radioFrame
        radioFrame = Frame(self._tk)
        self._rbtn = IntVar()
        self._rbtnAm = Radiobutton(radioFrame,text="AM", value=0, variable=self._rbtn)
        self._rbtnPm = Radiobutton(radioFrame, text="PM", value=1, variable=self._rbtn)
        btnFrame = Frame(self._tk)
        # q4d: added command to the btnBook and btnCancel
        self._btnBook = Button(btnFrame, text="Book", command=self._book)
        self._btnCancel = Button(btnFrame, text="Cancel", command=self._cancel)
        self._sclText = ScrolledText(width=40, height=8, padx=4, pady=4)
        self._lblId.grid(row=0, column=0)
        self._txtId.grid(row=0, column=1)
        self._lblDate.grid(row=1, column=0)
        self._txtDate.grid(row=1,column=1)
        # a4a: use grid manager for layout of radio button and inserting radioFrame into main window
        self._rbtnAm.grid(row=0, column=0)
        self._rbtnPm.grid(row=0, column=1)
        radioFrame.grid(row=2,column=1)
        self._btnBook.grid(row=0, column=0)
        self._btnCancel.grid(row=0,column=1)
        btnFrame.grid(row=3,column=1)
        self._sclText.grid(row=4,column=0,columnspan=2)
        self._sclText.config(state=DISABLED)
    
    def _cancel(self):
        # not implemented because not required by the TOA.
        pass

    # q4d: implemented event handler for the book button
    def _book(self):
        self._sclText.config(state=NORMAL)
        member = self._txtId.get().strip()
        booking_day = self._txtDate.get().strip()
        booking_mode = ["AM", "PM"][self._rbtn.get()]
        self._sclText.delete("1.0", "end")
        if "" in [member, booking_day]:
            self._sclText.insert("1.0", "Enter id and booking date")
        else:
            if member in self._booking:
                day, mode = self._booking[member]
                self._sclText.insert("1.0", f"{member} has already made a booking on {day} {mode}")
            else:
                self._booking[member] = [booking_day, booking_mode]
                self._sclText.insert("1.0", f"Booking for {member} on {booking_day} {booking_mode} confirmed")
        self._sclText.config(state=DISABLED)                
    
#   q 4b
#   Without columnspan, the scrolled text component width would be halved as it is only occupying 1 column instead of 2.

BookingGUI({"m1": ["1/10", "AM"], "m2":["1/10","AM"], "m3":["1/10","AM"] })