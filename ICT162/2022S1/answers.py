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

# q1a
class ClubHead(ABC):

    def __init__(self, loft: float, weight: int) -> None:
        self._loft = loft
        self._weight = weight

    @property
    def weight(self) -> int:
        """
        Weight is in grams
        """
        return self._weight
    
    @abstractmethod
    def getHeight(self) -> float:
        pass

    def __str__(self) -> str:
        loft = f"{self._loft:.1f}"
        return f"Loft: {loft:>4} degrees \t Weight: {self._weight:>4}g"

# q1b

class WoodHead(ClubHead):

    def __init__(self, loft: float, weight: int, size: int):
        ClubHead.__init__(self, loft, weight)
        self._size = size
    
    def getHeight(self) -> float:
        """
        Height is in inches
        """
        return self._size / 400
    
    def __str__(self):
        return ClubHead.__str__(self) + f" \t {'Head Size':<9}: {self._size}cc"


class BadMaterialException(Exception):

    def __init__(self, material:str):
        Exception.__init__(self, f"{material} is not a valid Iron Head material")

CAST = "Cast"
FORGED = "Forged"

class IronHead(ClubHead):

    def __init__(self, loft: float, weight: int, material:str) -> None:
        ClubHead.__init__(self, loft, weight)
        if material not in [CAST, FORGED]:
            raise BadMaterialException()
        self._material = material
    
    def getHeight(self) -> float:
        """
        Height is in inches
        """
        return 1
    
    def __str__(self) -> str:
        return ClubHead.__str__(self) + f" \t {'Material':<9}: {self._material}"

class BadStyleException(Exception):

    def __init__(self, style:str):
        Exception.__init__(self, f"{style} is not a valid Putter Head style")

BLADE = "Blade"
MALLET = "Mallet"

class PutterHead(ClubHead):

    def __init__(self, loft:float, weight:int, style:str) -> None:
        ClubHead.__init__(self, loft, weight)
        if style not in [BLADE, MALLET]:
            raise BadStyleException(style)
        self._style = style
    
    def getHeight(self) -> float:
        if self._style == BLADE:
            return 1
        return 0.5
    
    def __str__(self) -> str:
        return ClubHead.__str__(self) + f" \t {'Style':<9}: {self._style}"

# q1c

def q1c():
    Putter = PutterHead(3.5, 365, BLADE)
    Iron = IronHead(37.5, 285, FORGED)
    Wood = WoodHead(9.5, 206, 450)
    print(Putter)
    print(Iron)
    print(Wood)

# q2

class Shaft:
    """
    The exam did not ask for the implementation of Shaft class but this is to facilitate VSCode's type hinting feature
    """

    def __init__(self, length:float, weight:int, material:str, flex:str):
        self._length = length
        self._weight = weight
        self._material = material
        self._flex = flex
    
    @property
    def length(self) -> float:
        return self._length
    
    @property
    def weight(self) -> int:
        """
        weight is in grams
        """
        return self._weight
    

class Grip:
    """
    The exam did not ask for the implementation of Shaft class but this is to facilitate VSCode's type hinting feature
    """
    def __init__(self, diameter:float, weight:int, material:str) -> None:
        self._diameter = diameter
        self._weight = weight
        self._material = material
    
    @property
    def weight(self) -> int:
        """
        weight is in grams
        """
        return self._weight

# q2a

class Club:
    
    def __init__(self, label:str, head:ClubHead, shaft:Shaft, grip:Grip) -> None:
        self._label = label
        self._head = head
        self._shaft = shaft
        self._grip = grip

    @property
    def label(self) -> float:
        return self._label

    @property
    def weight(self) -> int:
        return self._head.weight + self._shaft.weight + self._grip.weight
    
    @property
    def length(self) -> float:
        return self._head.getHeight() + self._shaft.length
    
    def changeGrip(self, newGrip:Grip) -> None:
        self._grip = newGrip
    
    def __str__(self) -> str:
        length = f"{self.length:.2f}"
        return f"Club: {self._label:<10} \t Length: {length:>7}in \t Weight: {self.weight:> 4}g" 

# q2b

def q2b():
    # i
    driver = Club("Driver", WoodHead(10.5, 203, 450), Shaft(45, 65, "Graphite", "Stiff"), Grip(0.6, 62, "Rubber"))
    iron8 = Club("8-Iron", IronHead(34.5, 268, CAST), Shaft(35.5, 109, "Steel", "Regular"), Grip(0.6, 62, "Rubber"))
    sunset = Club("Sunset", PutterHead(3, 380, MALLET), Shaft(33, 120, "Steel", "Stiff"), Grip(0.6, 62, "Rubber"))


    # ii
    print(f"Total Weight: {driver.weight + iron8.weight + sunset.weight}g")

    # iii
    for club in [driver, iron8, sunset]:
        club.changeGrip(Grip(0.58, 65, "Leather"))
    
    # iv
    # In polymorphism, the implementation of a subclass overrides a method from its parent class with another method 
    # that shares the same function signature. This is evident in q2b whereby different subclasses [WoodHead, IronHead.
    # PutterHead] of the ClubHead class are used to create the objects corresponding to Driver, 8-Iron and Sunset.


# q2c
#
# i.   Club and Shaft: Composition
# ii.  ClubHead and PutterHead: Inheritance
# iii. Club abd IronHead: Composition

# q3a

class GolfBag:

    def __init__(self, owner:str, weight:int) -> None:
        self._owner = owner
        self._weight = weight
        self._compartments: dict[str, list[Club]] = {}
    
    def addClub(self, newCLub: Club) -> None:
        if newCLub.label in self._compartments:
            self._compartments[newCLub.label].append(newCLub)
        else:
            self._compartments[newCLub.label] = [newCLub]
    
    def removeClub(self, label:str) -> bool:
        if label in self._compartments:
            if len(self._compartments[label]) == 1:
                del self._compartments[label]
            else:
                self._compartments[label].pop()
            return True
        return False

    def getTotalWeight(self) -> int:
        """
        weight in grams
        """
        weight = self._weight
        for clubs in self._compartments.values():
            for club in clubs:
                weight += club.weight
        return weight
    
    def __str__(self) -> str:
        s = [f"Golf Bag Owner: {self._owner}"] 
        for clubs in self._compartments.values():
            for club in clubs:
                s.append(str(club))
        s.append(f"Total weight: {self.getTotalWeight()}g")
        return "\n".join(s)

# q3b
# I used the Dict[str, List[Club]] data structure to implement the collection.
# The first reason is a dictionary allows me to perform O(1) lookup based on the club's label. 
# This is espeically useful when there are many clubs. The second reason is this method also
# aggregates all the clubs of the same label together.

# q3c

class GolfEquipmentException(Exception):
    pass

class GolfBag:

    MAX_CLUBS = 14
    MAX_WEIGHT = 7500

    def __init__(self, owner:str, weight:int) -> None:
        self._owner = owner
        self._weight = weight
        self._compartments: dict[str, list[Club]] = {}
    
    def addClub(self, newCLub: Club) -> None:
        count = sum([len(clubs) for clubs in self._compartments.values()])
        if count == GolfBag.MAX_CLUBS:
            raise GolfEquipmentException()
        if self.getTotalWeight() + newCLub.weight > GolfBag.MAX_WEIGHT:
            raise GolfEquipmentException()
        if newCLub.label in self._compartments:
            self._compartments[newCLub.label].append(newCLub)
        else:
            self._compartments[newCLub.label] = [newCLub]

    def removeClub(self, label:str) -> bool:
        if label in self._compartments:
            if len(self._compartments[label]) == 1:
                del self._compartments[label]
            else:
                self._compartments[label].pop()
            return True
        return False

    def getTotalWeight(self) -> int:
        """
        weight in grams
        """
        weight = self._weight
        for clubs in self._compartments.values():
            for club in clubs:
                weight += club.weight
        return weight
    
    def __str__(self) -> str:
        s = [f"Golf Bag Owner: {self._owner}"] 
        for clubs in self._compartments.values():
            for club in clubs:
                s.append(str(club))
        s.append(f"Total weight: {self.getTotalWeight()}g")
        return "\n".join(s)

# q4

# q4a
# 
# self._win
# |_ dataFrame
# | |_ swingSpeed_lbl
# | |_ actionFrame
# |    |_ self._calculate_btn
# |    |_ self._clear_btn
# |_ outputFrame
#    |_ self._scrol_stxt


import tkinter as tk
from tkinter import ttk, scrolledtext

class GolfDistanceCalculatorGUI:

    def __init__(self):
        self._win = tk.Tk()
        self._win.title("Golf Distance Calculator")
        self._win.resizable(True, True)
        self._win.geometry("320x180")
        self.create_widgets()
        self._win.mainloop()
    
    def create_widgets(self):
        dataFrame = ttk.Frame(self._win)
        dataFrame.grid(column=0, row=0, padx=2, pady=4)

        swingSpeed_lbl = ttk.Label(dataFrame, text="Swing Speed (mph):")
        swingSpeed_lbl.grid(column=0, row=0, padx=4, pady=4)
        # q4b: added swingSpeed entry widget
        self._swingSpeed = tk.StringVar()
        swingSpeed_entry = ttk.Entry(dataFrame, textvariable=self._swingSpeed, width=25)
        swingSpeed_entry.grid(column=1,row=0)

        actionFrame = ttk.Frame(dataFrame)
        actionFrame.grid(column=0,row=1, columnspan=2)

        # q4c: added event handling
        self._calculate_btn = ttk.Button(actionFrame, text="Calculate", command=self._calculate)        
        self._calculate_btn.pack(side=tk.LEFT, padx=4, pady=4)
        self._clear_btn = ttk.Button(actionFrame, text="Clear", command=self._clear)
        self._clear_btn.pack(side=tk.LEFT, padx=4, pady=4)

        outputFrame = ttk.Frame(self._win)
        outputFrame.grid(column=0,row=1, padx=8, pady=4, columnspan=2)
        self._scrol_stxt = scrolledtext.ScrolledText(outputFrame, width=35, height=5, wrap=tk.WORD)
        self._scrol_stxt.grid(column=0,row=0)
        # disabled to disallow data entry into scrolledtext
        self._scrol_stxt.config(state=tk.DISABLED)

    # q4c
    def _clear(self):
        self._swingSpeed.set("")
        self._scrol_stxt.config(state=tk.NORMAL)
        self._scrol_stxt.delete("1.0", "end")
        self._scrol_stxt.config(state=tk.DISABLED)
    
    # q4c
    def _calculate(self):
        self._scrol_stxt.config(state=tk.NORMAL)
        self._scrol_stxt.delete("1.0", "end")
        swingSpeed = self._swingSpeed.get()
        try:
            ss = float(swingSpeed)
        except ValueError:
            self._scrol_stxt.insert(tk.INSERT, "Error(s) in input values.\n Please <clear> and try again.")
        else:
            dist = ss * 2.6
            self._scrol_stxt.config(state=tk.NORMAL)
            self._scrol_stxt.insert(tk.INSERT, f"Estimated distance: {dist:.0f} yards")
        self._scrol_stxt.config(state=tk.DISABLED)

if __name__ == "__main__":
    GolfDistanceCalculatorGUI()