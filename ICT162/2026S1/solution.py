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

The search hierachy for property starts at self, then the class.
Gadget._OS = "PyOS"
g1._os = "uOS"
after delete, g2._os = Gadget._os = "PyOS"

B

Q2
b._v = 0
b._x = 5

Hence the missing line is suoer().__init__()
B. 

Q3

Shape.area() is not implemented.

C.

Q4

vals = [1, 2, 3]
sum(vals) = 1 + 2 + 3 = 6

C.

Q5

A

Q6

"42x" cannot be converted to integer, so yields ValueError which was caught.

A.

Q7

1/0 triggers ZeroDivisionError, so print('A') and print('B') are executed.

A.

Q8

A refers to abstract
A

Q9

Vec(3) + 4 yields None, so v = None and doesn't have the n attribute.

D.

Q10

B.

"""

# Q11a

from abc import ABC, abstractmethod

class SmartDevice:
    _electricityRate:float = 0.30
    def __init__(self, model:str, power:float):
        self.__model  = model 
        self.__power = power 
    
    @property
    def model(self) -> str:
        return self.__model 
    
    @property 
    def power(self) -> float:
        return self.__power 
    
    @abstractmethod
    def monthlyCost(self, hours:float) -> float:
        pass
    

# Q11b

class LightBulb(SmartDevice):

    def __init__(self, model:str, power:float, lumens:int):
        super().__init__(model, power)
        self.__lumens = lumens 
    
    @property
    def lumens(self) -> int:
        return self.__lumens 
    
    def monthlyCost(self, hours:float) -> float:
        return hours * self.power/1000 * SmartDevice._electricityRate

class Thermostat(SmartDevice):

    def __init__(self, model:str, power:float, hvacCapacity:int):
        super().__init__(model, power)
        self.__hvacCapacity = hvacCapacity
    
    @property
    def hvacCapacity(self) -> int:
        return self.__hvacCapacity
    
    def monthlyCost(self, hours:float) -> float:
        return hours * 1.2 * self.power/1000 * SmartDevice._electricityRate

"""
11c

LightBulb : $0.41
Thermostat : $3.24

11d

This form of polymorphism is called dynamic polymorphism which is determined at runtime and is achieved through either overriding by inheritance or duck-typing.

In the loop, duck-typing is used.

"""

# 12a

class deviceException(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)
class SmartRoom:

    def __init__(self, name:str):
        self._name = name 
        self._devices: list[SmartDevice] = []
    
    def addDevice(self, device:SmartDevice) -> bool:
        for dev in self._devices:
            if dev.model == device.model:
                raise deviceException("Duplicate Device")
        self._devices.append(device)
        return True
    
    def removeDevice(self, model:str) -> bool:
        for i in range(len(self.__devices)):
           device = self._devices[i]
           if device.model == model:
               del self._devices[i]
               return True 
        return False
    
    def totalMonthlyCost(self, hours:float) -> float:
        total = 0
        for device in self._devices:
            total += device.monthlyCost(hours)
        return total
    
    def toString(self):
        return self.__str__()
    
    def __str__(self) -> str:
        if len(self._devices) == 0:
            return f"Smart Room '{self._name}' contains no devices"
        else:
            device_list = ", ".join([device.model for device in self._devices])
            return f"Smart Room '{self._name}' contains: {device_list}"

"""
12b

"""

def q12c():
    lb = LightBulb("LB-900", 9, 800)
    th = Thermostat("TH-2200", 60, 12000)
    bedroom = SmartRoom("Master Bedroom")
    bedroom.addDevice(lb)
    bedroom.addDevice(th)
    total_bedroom_cost = bedroom.totalMonthlyCost(150)
    print(bedroom)
    print(f"Total monthly cost for '{bedroom._name}' (150hrs): ${total_bedroom_cost:.2f}")

"""
Q13
"""

import tkinter as tk
from tkinter import messagebox 

class SmartRoomGUI:
    def __init__(self, smart_room:SmartRoom):
        # Q13a
        self._root = tk.Tk()
        self._root.geometry("400x400")
        self._room = smart_room
        # line 8
        self._root.title(f"Smart Room: {self._room._name}")

        # line 10
        self._room_name_label = tk.Label(self._root, text=f"Room: {self._room._name}", font=("Inter",24))
        self._room_name_label.pack(pady=10)

        self._hours_label = tk.Label(self._root, text="Enter Usage Hours (e.g. 150): ", font=("Inter",12))
        self._hours_label.pack(pady=10)

        self._hours_entry = tk.Entry(self._root, width=30, font=("Inter",12))
        self._hours_entry.pack(pady=5)
        self._hours_entry.insert(0, "150")

        self._compute_button = tk.Button(
            self._root, text="Compute Total Monthly Cost", command=self.computeCost,
            font=("Inter",12), bg="#4caf50", fg="white", activebackground="#45a049",
            relief=tk.RAISED, bd=3, highlightbackground="#4caf50"
        )
        self._compute_button.pack(pady=10)

        self._cost_display_var = tk.StringVar()
        self._cost_display_var.set("Total Cost: $0.00")
        # line 29
        self._cost_label = tk.Label(self._root, textvariable=self._cost_display_var, fg="blue", font=("Inter",24))
        self._cost_label.pack(pady=10)

        # line 32, 33
        self._room_desc_label = tk.Label(self._root, text=self._room.toString(), font=("Inter",24))
        self._root.mainloop()
    
    def computeCost(self):
        # Q13b
        try:
            hours = float(self._hours_entry.get())
        except ValueError:
            messagebox.showerror(title="Input Error", message="Please enter a valid numeric value for usage hours")
        else:
            if hours <= 0:
                messagebox.showerror(title="Input Error", message="Usage hours must be a positive number")
            else:
                cost = self._room.totalMonthlyCost(hours)
                self._cost_display_var.set(f"Total Cost: ${cost:.2f}")
