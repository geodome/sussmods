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

#q1

#q1a
# _winningPoints: class member because this is univerally applicable to every game instance
# _players: instance member because each game instance has a unique set of players
# _setWiningPoints: class method because _winningPoint is a class variable
# _deductPlayerPonts: instance method because points are deducted for a player belonging to a specific game instance

from datetime import datetime

from abc import ABC, abstractmethod

# q1b
class Player:
    
    currentId = 0
    
    def __init__(self) -> None:
        self._id = Player.getNextPlayerId()
        self._points = 5
        self._active = True

    @classmethod
    def getNextPlayerId(cls) -> int:
        """
        Although this class method is not specified for in the class diagram, there should be a
        separation of concerns between class and instance variables. Only class methods should be
        used to modify the class variables. Normally, it is fine for an instance method to directly
        read the class variable but in this context, the currentId needs to be incremented immediately
        after a player has been assigned the currentId.
        """
        cls.currentId += 1
        return cls.currentId

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def points(self) -> int:
        return self._points
    
    @points.setter
    def points(self, newPoints: int) -> None:
        self._points = newPoints
        if self._points < 0:
            self._points = 0
            self._active = False

    @property
    def active(self) -> bool:
        return self._active
    
    def __str__(self) -> str:
        return f"Id: {self._id} Points: {self._points} Active: {self._active}"

# q1c
class Game:

    _gamePoints = 3
    _winningPoints = 15
    
    def __init__(self) -> None:
        p1 = Player()
        self._players = {}
        self._players[p1.id] = p1

    @classmethod
    def getWinningPoint(cls) -> int:
        return cls._winningPoints        
    
    @classmethod
    def setWinningPoints(cls, newPoints: int):
        cls._winningPoints = newPoints
    
    @classmethod
    def getGamePoints(cls) -> int:
        return cls._gamePoints

    def deductPlayerPoints(self, playerId: str) -> bool:
        if playerId in self._players:
            if self._players[playerId].active:
                self._players[playerId].points -= Game.getGamePoints()
                return True
        return False
    
    def getWinners(self) -> list["Player"]:
        winners = []
        for playerId in self._players:
            if self._player[playerId].points > Game.getWinningPoint():
                winners.append(self._players[playerId])
        return winners
    
    def addPlayer(self, player: Player) -> bool:
        if player.id not in self._players:
            self._players[player.id] = player
            return True
        return False

    def removePlayer(self, playerId: str) -> Player:
        if playerId in self._players:
            p = self._players[playerId]
            del(self._players[playerId])
            return p
    
    def getPlayer(self, playerId: str) -> Player:
        if playerId in self._players:
            return self._players[playerId]
    
    def __str__(self) -> str:
        lines = []
        playerIds = self._players.keys()
        playerIds.sorted()
        for playerId in playerIds:
            lines.append(str(self._players[playerId]))
        return "\n".join(lines)

# q1d

def q1d():
    game = Game()
    p = Player()
    if game.addPlayer(p):
        print("Successfully added")
    else:
        print("Unable to add player")
    Game.setWinningPoints(12)
    if game.deductPlayerPoints(p.id):
        print("Points successfully deducted from player", p.id)
        print(p)
    else:
        print("Unsuccessful deducation of points from Player", p.id)

# q2

# q2a
# i.    Pet and Owner: Object Composition. The owner is one of the composition objects of the Pet class.
# ii.   Pet and Cat: Inheritance. Cat is a subclass of Pet.

# q2b

class PetOwner:
    def __init__(self, name: str, address: str) -> None:
        self._name = name
        self._address = address
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def address(self) -> str:
        return self._address
    
    @address.setter
    def address(self, newAddress: str) -> None:
        self._address = newAddress

    def __str__(self) -> str:
        return f"Name: {self.name} Address: {self.address}"

class Pet(ABC):
    
    def __init__(self, identification: str, name: str, dateOfBirth: datetime, owner: PetOwner) -> None:
        self._identification = identification
        self._name = name
        self._dateOfBirth = dateOfBirth
        self._owner = owner

    @property
    def identification(self) -> str:
        return self._identification
    
    @property
    def dateOfBirth(self) -> datetime:
        return self._dateOfBirthß
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def owner(self) -> PetOwner:
        return self._owner
    
    @owner.setter
    def owner(self, newOwner: PetOwner) -> None:
        self._owner = newOwner
    
    @property
    def address(self) -> str:
        # q3b
        if self._owner is None:
            raise PetAgencyException("Pet has no owner. No owner address to retrieve.")
        return self._owner.address
    
    @address.setter
    def address(self, newAddress: str) -> None:
        # q3b
        if self._owner is None:
            raise PetAgencyException("Pet has no owner. No owner address to update.")
        self._owner.address = newAddress
    
    @abstractmethod
    def ageInHumanYears(self) -> int:
        pass

    @property
    def hdbFriendly(self) -> bool:
        return False

    def __str__(self) -> str:
        lines = [
            f"Id: {self.identification} HDB Friendly: {self.hdbFriendly}",
            f"Name: {self.name} Date of Birth: {self.dateOfBirth.strftime('%d %B %Y')} Age in Human Year: {self.ageInHumanYears()}",
            f"Owner: {str(self.owner)}",
        ]
        return "\n".join(lines)

# q2c

class Dog(Pet):

    def __init__(self, identification: str, hdbFriendly: bool, name: str, dateOfBirth: datetime, owner: PetOwner) -> None:
        Pet.__init__(self, identification, name, dateOfBirth, owner)
        self._hdbFriendly = hdbFriendly

    @property
    def hdbFriendly(self) -> bool:
        return self._hdbFriendly
    
    def ageInHumanYears(self) -> int:        
        timedelta = datetime.today() - self.dateOfBirth 
        days = timedelta.days
        if days <= 365:
            return 15
        if days <= 2*365:
            return 24
        days -= 2*365
        age = 24
        while days > 0:
            days -= 365
            age += 5
        return age
    
    def __str__(self) -> str:
        lines = [
            f"Dog Id: {self.identification} HDB Friendly: {self.hdbFriendly}",
            f"Name: {self.name} Date of Birth: {self.dateOfBirth.strftime('%d %B %Y')} Age in Human Year: {self.ageInHumanYears()}",
            f"Owner: {str(self.owner)}",
        ]
        return "\n".join(lines)

# Cat is a dummy class since it is not required for exam
class Cat(Pet):
    def __init__(self, identification: str, name: str, dateOfBirth: datetime, owner:PetOwner) -> None:
        Pet.__init__(self, identification, name, dateOfBirth, owner)

    def ageInHumanYears(self) -> int:
        return 0

# q3a

class PetAgencyException(Exception):
    
    def __init__(self, msg: str) -> None:
        Exception.__init__(self, msg)

# q3c
class PetAdoptionAgency:

    def __init__(self) -> None:
        self._pets: list["Pet"] = []
    
    def searchPets(self, identification: str) -> Pet:
        for pet in self._pets:
            if pet.identification == identification:
                return pet
    
    def addPet(self, pet: Pet) -> bool:
        found = self.searchPets(pet.identification)
        if found is None:
            self._pets.append(pet)
            return True
        raise PetAgencyException("Duplicate pet identification. Cannot add.")
    
    def adopt(self, owner: PetOwner, identification: str) -> bool:
        pet = self.searchPets(identification)
        if pet is None:
            raise PetAgencyException("Incorrect pet identification. Cannot adopt")
        if pet.owner is not None:
            raise PetAgencyException("Pet already has an owner. Cannot be adopted")
        count = 0
        for p in self._pets:
            if p.owner.name == owner.name and p.owner.address == owner.address:
                count += 1
        if count < 2:
            pet.owner = owner
            return True
        return False

    def updateAddress(self, identification: str, address: str) -> bool:
        pet = self.searchPets(identification)
        if pet is None:
            raise PetAgencyException("Incorrect pet identification. Cannot update address")
        pet.address = address
        return True

# q3d

def PetAdoptionAgencyApp() -> None:
    agency = PetAdoptionAgency()
    agency.addPet(Dog("D123", True, "Jackie", datetime(2019, 12,7), None))
    agency.addPet(Cat("C031", "Sparkle", datetime(2018, 1, 12), None))
    agency.addPet(Cat("C017", "Ginger", datetime(2018, 1, 12), PetOwner("Peter", "12 Dunbar Road")))

    while True:
        print("Menu")
        print("1. Update pet address")
        print("2. Adopt a pet")
        print("0. Exit")
        choice = input("Enter a choice: ")
        try:
            choice = int(choice)
        except:
            continue
        else:
            if choice == 0:
                break
            elif choice == 1:
                updatePetAddress(agency)
            elif choice == 2:
                adoptPet(agency)
            else:
                continue
    

def updatePetAddress(agency: PetAdoptionAgency) -> None:
    id = input("Enter pet identification: ")
    address = input("Enter new address: ")
    try:
        print("Update address:", agency.updateAddress(id, address))
    except PetAgencyException as e:
        print(e)


def adoptPet(agency: PetAdoptionAgency) -> None:
    name = input("Enter owner name:")
    address = input("Enter address:")
    id = input("Enter pet identification: ")
    try:
        print("Adoption:", agency.adopt(PetOwner(name, address), id))
    except PetAgencyException as e:
        print(e)

# q4a

import tkinter as tk
from tkinter import ttk

class PetAgeCalculatorGui:

    def __init__(self) -> None:
        self._win = tk.Tk()
        self._win.title("Pet Age Calculator")
        self._win.resizable(False, False)
        self.create_widgets()
        self._win.geometry('350x150')
        self._win.mainloop()

    def create_widgets(self) -> None:
        dataFrame = ttk.Frame(self._win)
        self._age = tk.StringVar(dataFrame)
        self._age_lbl = ttk.Label(dataFrame, text="Age: ")
        self._age_lbl.grid(column=0, row=0, sticky=tk.EW)
        self._ageValue_Ety = ttk.Entry(dataFrame, width=18, textvariable=self._age)  
        self._ageValue_Ety.grid(column=1, row=0, sticky=tk.EW)         
        for_lbl = ttk.Label(dataFrame, text="For")  
        for_lbl.grid(column=0, row=1)    
        radioFrame = ttk.Frame(dataFrame) 
        radioFrame.grid(column=1, row=1, sticky=tk.EW)  
        self._animal = tk.IntVar(radioFrame, 0)            
        cat_rdbtn = tk.Radiobutton(radioFrame, text = 'Cat', value=0, variable=self._animal)                                  
        dog_rdbtn = tk.Radiobutton(radioFrame, text = 'Dog', value=1, variable=self._animal)
        cat_rdbtn.grid(column=1, row=0, sticky=tk.W) 
        dog_rdbtn.grid(column=2, row=0, sticky=tk.W)                         
        actionFrame = ttk.Frame(dataFrame)   
        actionFrame.grid(column=1, row=3)  
        self._convert_btn = ttk.Button(actionFrame, text="To Human Years", command=self.convert)    
        self._convert_btn.pack(side = tk.LEFT)       
        self._clear_btn = ttk.Button(actionFrame, text="Clear", command=self.clear)   
        self._clear_btn.pack(side = tk.LEFT)     
        self._output_lbl = ttk.Label(dataFrame, text="Output:", justify=tk.LEFT)  
        self._output_lbl.grid(column=0, row=4, columnspan = 2, sticky=tk.EW) 
        dataFrame.pack(side = tk.TOP)
    
    def clear(self) -> None:
        self._ageValue_Ety.delete(0, "end")
        self._output_lbl.configure(text="Output:")
    
    def convert(self) -> None:
        animal = self._animal.get()
        age = self._age.get()
        cat, dog = 0, 1
        if animal == cat:
            if age.isnumeric() and int(age) > 0:
                age = int(age)
                if age == 0:
                    self._output_lbl.config(text="output: Cat 0 year = 0 human years")
                elif age ==  1:
                    self._output_lbl.config(text="output: Cat 1 year = 19 human years")
                elif age == 2:
                    self._output_lbl.config(text="output: Cat 2 year = 24 human years")
                else:
                    catAge = 24
                    i = age - 2
                    while i > 0:
                        catAge += 4
                        i -=1
                    self._output_lbl.config(text=f"output: Cat {age} year = {catAge} human years")
            else:
                self._output_lbl.config(text="output: bad age value")
        else:
            if age.isnumeric() and int(age) > 0:
                age = int(age)
                if age == 0:
                    self._output_lbl.config(text="output: Dog 0 year = 0 human years")
                elif age ==  1:
                    self._output_lbl.config(text="output: Dog 1 year = 15 human years")
                elif age == 2:
                    self._output_lbl.config(text="output: Dog 2 year = 24 human years")
                else:
                    dogAge = 24
                    i = age - 2
                    while i > 0:
                        dogAge += 5
                        i -=1
                    self._output_lbl.config(text="output: Dog {age} year = {dogAge} human years")
            else:
                self._output_lbl.config(text="output: bad age value")
