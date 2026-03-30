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


# Question 1

"""
1(a)
Reuse by inheritance: 23, 32, 36, 40
Reuse by object composition: 32
Method overriding by replacement: 42
Method overriding by refinement: 30
Polymorphism: 52
Overloading of method: 5, 39

1(b)

Code Tracing
============

objA = ClassA(7)
.methodA() -> 35
.__str__() -> "Variable A: 7"

objB  = ClassB(6)
.methodA() -> 12
.__str__() -> "Variable B: 6"

objC = ClassC(5,4,objB)
.ClassA(5)
    .methodA() -> 25
    .__str__() -> "Variable A: 5"
.methodA() -> 16
.__str__() -> "Variable A: 5  Variable C1: 4  Variable C2: Variable B: 6"

objD = ClassD(3,2)
.ClassA(3)
    .methodA() -> 15
    .__str__() -> "Variable A: 5"
.methodA() -> classA(3).methodA(2) -> 6
.__str__() -> "Variable D: 2"

Output
======

35
12
16
6
Variable A: 5  Variable C1: 4  Variable C2: Variable B: 6
"""

# Question 2

from abc import ABC, abstractmethod

class CCA(ABC):
    _STANDARD_FEES = 15
    
    def __init__(self, name:str) -> None:
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    @abstractmethod
    def getFees(self) -> float:
        pass

class SportsGroup(CCA):

    def __init__(self, name:str, gender:str, competitive:bool) -> None:
        super().__init__(name)
        self._gender = gender
        self._competitive = competitive
    
    def getFees(self) -> float:
        if self._competitive:
            return 0
        return CCA._STANDARD_FEES
    
    def __str__(self) -> str:
        return f"{self._name} ({self._gender}), monthly: ${self.getFees():.2f}"

class InterestGroup(CCA):
    _MAJOR_BASED_FEES = {"HRM":32, "ECE":25}

    def __init__(self, name:str, major:str=None) -> None:
        super().__init__(name)
        self._major = major
    
    def getFees(self) -> int:
        return InterestGroup._MAJOR_BASED_FEES.get(self._major, CCA._STANDARD_FEES)
    
    def __str__(self) -> str:
        return f"{self._name}, monthly: ${self.getFees():.2f}"
    
    @classmethod
    def getFeesByMajor(cls, name:str, major:str) -> float:
        """Required by 4(a)"""
        try:
            return cls._MAJOR_BASED_FEES[major]
        except KeyError:
            pass
    
    @classmethod
    def updateFeesByMajor(cls, major:str, fees:float) -> None:
        """Requried by 4(a)"""
        cls._MAJOR_BASED_FEES[major] = fees

# Question 3

# 3(a)

class CcaException(Exception):
    pass

class Student:
    _MAX_CCA = 3
    _MAX_CCA_FEES = 45

    def __init__(self, id:str, name:str) -> None:
        self._id = id
        self._name = name
        self._ccaRecord: list[CCA] = []
    
    def getCcaFees(self) -> float:
        total:float = 0
        for cca in self._ccaRecord:
            total += cca.getFees()
        return total
    
    def addCca(self, cca:CCA):
        # this exception should be checked first because there is no point adding the cca if it is already in the record list.
        for c in self._ccaRecord:
            if c.name == cca.name:
                raise CcaException("You already enrolled in this CCA")
            
        if len(self._ccaRecord) + 1 > Student._MAX_CCA:
            raise CcaException("Cannot enrol more than 3 CCAs")
        
        if self.getCcaFees() + cca.getFees() > Student._MAX_CCA_FEES:
            raise CcaException(f"Cannot enrol as total CCA fees will exceed ${Student._MAX_CCA_FEES}")

        self._ccaRecord.append(cca)

def main() -> None:
    s = Student("B123", "Bu Ah Ya")
    cca1 = SportsGroup("Ultimate Frisbee", "Coed", False)
    cca2 = SportsGroup("Tennis", "Male", True)
    cca3 = InterestGroup("Playpen for Teachers", "ECE")
    cca4 = InterestGroup("Dance(X)")

    for cca in [cca1, cca2, cca3, cca4]:
        try:
            s.addCca(cca)
        except CcaException as e:
            print(e)
    
    print(f"Monthly CCA fees: ${s.getCcaFees():.2f}")

# Question 4

# 4(a) is implemented in the Interest Group class of Question 2

# 4(b)

import tkinter as tk

class CcaFeesGUI:
    
    def __init__(self) -> None:
        pass

    def create_widgets(self) -> None:
        pass

    def _insert_text(self, text:str, toDelete=False)->None:
        self._scrol_stxt.config(state=tk.NORMAL)
        if toDelete:
            self._scrol_stxt.delete("1.0", "end")     
        self._scrol_stxt.insert("end", text)
        self._scrol_stxt.config(state=tk.DISABLED)

    def action(self) -> None:
        major = self._major.get().strip()
        fee = self._major.get().strip()
        if major == "":
            """Empty major field"""
            self.insert_text("Major should not be blank...")
        elif fee == "":
            """enquire cca fee for major"""
            fee = InterestGroup.getFeesByMajor(major)
            if fee is None:
                self._insert_text("No fees setup for this major...")
            else:
                self._insert__text(f"Fees for {major}-based is ${fee:.2f}")
        else:
            """To update fees"""
            # at this point, fee is an non-empty string
            if isnumeric(fee):
                fee = float(fee)
                if fee < 0:
                    self._insert_text("Fees should be positive number")
                else:
                    InterestGroup.updateFeesByMajor(major, fee)         
                    self._insert_text(f"Fees for {major} is now ${fee:.2f}")       
            else:
                self._insert_text("Fees should be positive numberr")

def isnumeric(fee:str) -> bool:
    try:
        float(fee)
    except ValueError:
        return False
    else:
        return True