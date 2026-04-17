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
Q1

__test is a private variable, so in the child class, child.__test and super().__test are 2 different variables

C. Parent value: 5 Child Value: 10

Q2

Line 19: There is no getter for the property width.
Line 20: area is a property, not a method, so it should be invoked without ().

B. Line 19 and 20

Q3

B. self.__engine = engine

Q4

B. @abstactmethod

Q5

In child_method(), parent_method() triggers the error before the raise statrment.

D. An error occured in Parent

Q6.

C. TypeError: Can't instantiate abstract class Cat with abstract method 'sound'

Q7.

A. def fly(self): return "Flapping Wings"
"""

# Question 8
# Python doesn't support traditional method overloading which distinguishes each
# overloaded method by its parameteric signature. 2 solutions are presented here.

class Operation:
    def multiply(self, x:int|float, y:int|float, z:int|float=1) -> int|float:
        return x*y*z
    
class Operation:
    def multiply(self, *args:list[int|float]) -> int|float:
        """
        This implementation accepts at least 2 multiplication terms to compute the
        multiplication. The variadic *args is used to accept multiple parameters to 
        emulate overloading.
        """
        if len(args) > 1:
            result = 1
            for i in args:
                result *= i
            return result
        raise Exception("Requires at least 2 multiplication terms")

# Question 9 and 10

from abc import ABC, abstractmethod 
from datetime import datetime 

class Tracking:
    """
    Provided by exam paper for Question 10
    """
    def __init__(self) -> None:
        self.__history: list[tuple[str,str]] = []
    
    def update_status(self, status:str) -> None:
        formatted_datetime = datetime.now().strftime("%Y-%m-%d")
        self.__history.append((formatted_datetime, status))
    
    def get_history(self) -> list[tuple[str,str]]:
        if not self.__history:
            raise Exception("No tracking history available")
        return self.__history

class Shipment(ABC):
    """
    Answer for Q9a
    """

    _base_cost = 1.5

    def __init__(self, id:str, weight:float, destination:str) -> None:
        self.__id = id 
        self.__weight = weight 
        self.__destination = destination 
        # added for Q10
        self.__tracking: Tracking = Tracking()
    
    @property
    def weight(self) -> float:
        return self.__weight 

    @property
    def destination(self) -> str:
        """
        added for coherence with Q11
        """
        return self.__destination
    
    @property
    def id(self) -> str:
        """
        added for coherence with Q11
        """
        return self.__id 
    
    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def __str__(self) -> str:
        """
        Question 9c
        """
        return f"Shipment ID {self.__id} to {self.__destination}: Cost = {self.calculate_cost()}"
    
    def start_tracking(self) -> None:
        """
        Added for Question 10
        """
        self.__tracking.update_status("Initialised")
    
    def update_status(self, status:str) -> None:
        """
        Added for Question 10
        """
        self.__tracking.update_status(status)
    
    def get_status_history(self) -> list[tuple[str, str]]:
        """
        Added for question 10
        """
        return self.__tracking.get_history()

class PriorityShipment(Shipment):
    """
    Required by Q9b
    """

    _priority_fee = 10

    def __init__(self, id:str, weight:float, destination:str) -> None:
        super().__init__(id, weight, destination)
    
    def calculate_cost(self) -> float:
        return self.weight*PriorityShipment._base_cost + PriorityShipment._priority_fee

class RefrigeratedShipment(Shipment):
    """
    Required by Q9b
    """
    _refrigeration_fee = 20

    def __init__(self, id:str, weight:float, destination:str) -> None:
        super().__init__(id, weight, destination)
    
    def calculate_cost(self) -> float:
        return self.weight*RefrigeratedShipment._base_cost + RefrigeratedShipment._refrigeration_fee

# Question 11

import tkinter as tk 

class ShipmentTrackerGUI:
    def __init__(self, shipment_list:list[Shipment]):
        """
        Code provided by exam question.
        """
        win = tk.Tk()
        win.title("Shipment Tracker")
        self.__shipment_list = shipment_list
        # shipment listbox
        self.__listbox = tk.Listbox(win)
        for shipment in self.__shipment_list:
            self.__listbox.insert(tk.END, f"{shipment.destination} (ID: {shipment.id})")
        # label to display current status
        self.__status_label = tk.Label(win, text="Current Status: N/A")
        
        # missing code for 11a to create the GUI window
        self.__listbox.pack(side=tk.TOP)
        self.__status_label.pack(side=tk.TOP)

        # added event handler for listbox for coherence with 11b
        self.__listbox.bind('<<ListboxSelect>>', self.on_select)

        win.mainloop()
    
    def on_select(self, event:tk.Event) -> None:
        """
        Required for 11b
        """
        selected_index: tuple[int] = self.__listbox.curselection()
        if selected_index:
            # get the shipment object from the list
            shipment = self.__shipment_list[selected_index[0]]
            # missing line for 11b
            # display the latest status of the selected shipment
            try:
                date, status = shipment.get_status_history()[-1]
            except IndexError:
                self.__status_label.config("Current Status: N/A")
            else:
                self.__status_label.config(text=f"Current Status: ({date}, {status})")

def main():
    """
    Code provideed by Q11
    """
    shipment_list: list[Shipment] = [
        PriorityShipment("102", 5, "San Francisco"),
        RefrigeratedShipment("103", 8, "Chicago")
    ]
    # start tracking for shipments
    for shipment in shipment_list:
        shipment.start_tracking()
    
    shipment_tracker = ShipmentTrackerGUI(shipment_list)

