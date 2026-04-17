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
Question 1a

b, an instance of the BBB class, is created, then its method1() is invoked in the print job.

b._varA = 2
b._varB = 2
b.method1(3) = b._varB * 3 = 6

The output is: 
6

Question 1b

c, an instance of the CCC class, is created, then its method1() is invoked in the print job.

c._varA = 3
c._varC = 3
c.method1(3) = c._varC + 3 = 6

The output is:
6

Question 1c

d, an intance of the DDD class, is created, then its method1() is invoked in the print job.

d._varA = 3
d._varB = 4
d.method1(3) = d._varB * 3 = 12

The output is:
12

Question 1d

d, an intance of the DDD class, is created, then its method2() is invoked in the print job, 
which in turn calls method1().

d._varA = 3
d._varB = 4
d.method1(3) = d._varB * 3 = 12
d.method2(3) = d.method1(3) * 2 = 12 * 2 = 24

The output is:
24

Question 1e

e, an instance of the EEE class is created, then its method1() is invoked in the print job.

e.method1(3) then calls the method1(6) of the parent class.

e._varA = 4
e._varC = 4
e.method1(3) = super().method1(3*2) = e._varC + 6 = 10

The output is:
10

"""

# Question 2a

class ServiceStaff:

    def __init__(self, name:str, skillFactor:float, rate:float) -> None:
        self.__name = name
        self.__skillFactor = skillFactor
        self.__rate = rate
    
    @property
    def skillFactor(self) -> float:
        return self.__skillFactor
    
    @property 
    def rate(self) -> float:
        return self.__rate

# Question 2b

class ServiceJob:
    _BASIC_FEES = 100
    
    def __init__(self, jobId:str, hours:float, staff:ServiceStaff) -> None:
        self.__jobId = jobId
        self.__hours = hours 
        self.__staff = staff 
    
    @property 
    def hours(self) -> float:
        return self.__hours
       
    def computeJobDuration(self) -> float:
        return self.__hours / self.__staff.skillFactor
    
    def getCharges(self) -> float:
        return ServiceJob._BASIC_FEES + self.computeJobDuration()*self.__staff.rate

# Question 2c

class HomeServiceJob(ServiceJob):

    def __init__(self, jobId:str, hours:float, staff:ServiceStaff, address:str):
        super().__init__(jobId, hours, staff)
        self.__address = address
    
    def computeJobDuration(self):
        return self.hours + 1
    
    def getCharges(self):
        return 1.5*super().getCharges()

"""
Question 2d

HomeServiceJob.getCharges() was overrided by refinement. The output of the 
original method from parent class was multiplied by 1.5 to produce a new output.

HomeServiceJob.computeJobDuration() was overrided by replacement. The entire 
computeJobDuration() method was rewritten without invoking super().computeJobDuration().

Question 2e

ServiceJob and HomeServiceJob:
Inheritance. HomeServiceJob is a subclass of ServiceJob.

ServiceJob and ServiceStaff:
Composition. ServiceJob.__staff holds an instance of ServiceStaff

HomeServiceJob and ServiceStaff:
Composition. HomeServiceJob.__staff holds an instance of ServiceStaff.

"""

# Question 3a

class InvalidContactException(Exception):
    pass 

# Question 3b 

class Contact:

    def __init__(self, name:str, number:int) -> None:
        self.__name = name 
        if self.checkNumber(number):
            self.__number = number 
    
    @property 
    def number(self) -> int:
        return self.__number
    
    @property 
    def name(self, str) -> str:
        return self.__name
    
    def checkNumber(self) -> bool:
        if 10000000 <= self.__number <= 99999999:
            raise InvalidContactException("Contact Number must contain exactly 8 digits")
        if self.__number // 10000000 not in [6,8,9]:
            raise InvalidContactException("Contact number must start with a 6, 8, or 9")
        return True 
    
    def __str__(self) -> str:
        return f"Name: {self.__name} \t Number: {self.__number}"

# Question 3c

class PhoneBook:

    def __init__(self):
        self.__contacts: list[Contact] = []
    
    def searchContact(self, name:str) -> Contact|None:
        for contact in self.__contacts:
            if contact.name == name:
                return contact
        return None 
    
    def addContact(self, name:str, number:int) -> bool:
        for contact in self.__contacts:
            if name == contact.name:
                raise InvalidContactException("Duplicate name")
            if number == contact.number:
                raise InvalidContactException("Duplicate number")
        self.__contacts.append(Contact(name, number))
        return True
    
    def removeContact(self, name:str) -> bool:
        for i in range(len(self.__contacts)-1,-1,-1):
            if self.__contacts[i].name == name:
                del self.__contact[i]
                return True 
        return False 
    
    def __str__(self) -> str:
        s = []
        for contact in sorted(self.__contacts, key=lambda x: x.name):
            s.append(str(contact))
        return "\n".join(s)

# Question 4

import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 

class GUI:

    def __init__(self) -> None:
        self._win = tk.Tk()
        self._win.resizable(True,True)
        self._win.title("Celsius to Fahrenheit")
        self.create_widgets()
        self._win.mainloop()

    def create_widgets(self) -> None:
        """
        required by 4a
        """
        celsius_lbl = ttk.Label(self._win, text="Celsius:")
        self._celsius_Ety = ttk.Entry(self._win, width=5)
        convert_btn = ttk.Button(self._win, text="Convert", command=self.convert)
        self._scrol_stxt = scrolledtext.ScrolledText(self._win, width=38, height=5, wrap=tk.WORD)

        # missing code
        celsius_lbl.grid(row=0,column=1)
        self._celsius_Ety.grid(row=0,column=2,sticky="W")
        self._scrol_stxt.grid(row=1,column=0,columnspan=4)
        self._scrol_stxt.config(state=tk.DISABLED)
        convert_btn.grid(row=2,column=1,columnspan=2)

    def convert(self) -> None:
        """
        required by 4b
        """
        self._scrol_stxt.config(state=tk.NORMAL)
        self._scrol_stxt.delete("1.0", tk.END)

        celsius = self._celsius_Ety.get()
        try:
            celsius_numeric = float(celsius)
        except ValueError:
            self._scrol_stxt.insert(tk.END, "Enter only numbers for celsius\n")
        else:
            F = (celsius_numeric * 9 / 5) + 32
            self._scrol_stxt.insert(tk.END, f"Celcius {celsius} is {F:.1f} in Fahrenheit\n")
        
        self._scrol_stxt.config(state=tk.DISABLED)

GUI() 
