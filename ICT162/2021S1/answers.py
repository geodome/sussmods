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

from datetime import datetime

# q1a
# Inheritance is useful when there is a clear hierarchy or a "is-a" relationship between classes, while composition 
# is useful when there is a "has-a" relationship between classes. The relationship between Driver and Trip is composition. 
# This is because a driver can make multiple trips and thus this is a has-a relationship.

# q1b
class Driver:
    _nextId: int = 0

    @classmethod
    def nextId(cls) -> int:
        cls._nextId += 1
        return cls._nextId

    def __init__(self, name: str, contact: str):
        self._driverId = Driver.nextId()
        self._name = name
        self._contact = contact

    @property
    def driverId(self) -> int:
        return self._driverId

    @property
    def name(self) -> str:
        return self._name   
    
    @property
    def contact(self) -> str:
        return self._contact

    @contact.setter
    def contact(self, newContact: str):
        self._contact = newContact
    
    def __str__(self) -> str:
        return "\t".join(["driver Id:" + self.driverId, "name: " + self.name, "Contact: " + self.contact])

# q1c
class Trip:

    def __init__(self, tripDate: datetime, startPoint: str, destination: str, distance: float, driver: Driver):
        self._tripDate = tripDate
        self._startPoint = startPoint
        self._destination = destination
        self._distance = distance
        self._driver = driver
    
    @property
    def driver(self) -> Driver:
        return self._driver
    
    @property
    def driverName(self) -> str:
        return self._driver.name
    
    @property
    def distance(self) -> float:
        return self._distance
    
    @property
    def tripDate(self) -> datetime:
        return self._tripDate
    
    def __str__(self) -> str:
        return "\t".join([self._tripDate.strftime("%d %B %Y %H:%M"), "From: " + self._startPoint, "To: " + self._destination, "Distance: " + str(self.distance) + "km", str(self.driver)])

# q2a

from abc import ABC, abstractmethod

class Trip:

    def __init__(self, tripDate: datetime, startPoint: str, destination: str, distance: float, driver: Driver):
        self._tripDate = tripDate
        self._startPoint = startPoint
        self._destination = destination
        self._distance = distance
        self._driver = driver
    
    @property
    def tripDate(self) -> datetime:
        return self._tripDate

    @property
    def distance(self) -> float:
        return self._distance
    
    @property
    def driver(self) -> Driver:
        return self._driver
    
    @property
    def driverName(self) -> str:
        return self._driver.name

class TravelCard(ABC):

    def __init__(self, cardNo: str, expiryDate: datetime):
        self._cardNo = cardNo
        self._expiryDate = expiryDate
        self._trips: list[Trip] = []
    
    @property
    def cardNo(self) -> str:
        return self._cardNo
    
    @property
    def expiryDate(self) -> datetime:
        return self._expiryDate
    
    def getTripDriverByTripNumber(self, n: int) -> Trip:
        if 0 < n <= len(self._trips):
            return self._trips[n-1].driver
    
    def getTripByDate(self, aDate: datetime) -> list["Trip"]:
        trips = []
        for trip in self._trips:            
            if trip.tripDate.day == aDate.day and trip.tripDate.month == aDate.month and trip.tripDate.year == aDate.year:
                trips.append(trip)
        if len(trips) > 0:
            return trips
    
    def addTrip(self, trip: Trip) -> bool:
        if self.expiryDate > trip.tripDate and self.canTravel(trip.distance):
            self._trips.append(trip)
            self.consumeDistance(trip.distance)
            return True
        return False
    
    @abstractmethod
    def canTravel(self, distance: float) -> bool:
        return False

    @abstractmethod
    def consumeDistance(self, distance: float) -> bool:
        return False 

    @abstractmethod
    def topUp(self):
        pass

    @abstractmethod
    def balanceDetail(self) -> str:
        return ""   
    
    def trips(self):
        for trip in self._trips:
            yield trip

# q2b

class TripTravelCard(TravelCard):
    _shortDistanceMaxLimit = 12
    _topUpLongShortTrips = [1,3]

    def __init__(self, cardNo: str, expiryDate: datetime):
        TravelCard.__init__(self, cardNo, expiryDate)
        self._longTrip, self._shortTrip = TravelCard.topUpLongShortTrips
    
    @classmethod
    def topUpLongShortTrips(cls) -> list[int]:
        return cls._topUpLongShortTrips
    
    @classmethod
    def isShort(cls, distance: float) -> bool:
        return distance <= cls._shortDistanceMaxLimit
    
    def canTravel(self, distance: float) -> bool:
        if TripTravelCard.isShort(distance):
            if self._shortTrip > 0:
                return True
            else:
                if self._longTrip > 0:
                    return True                            
        else:
            if self._longTrip > 0:
                return True
            else:
                if self._shortTrip >= 3:
                    return True                            
        return False
    
    def consumeDistance(self, distance: float) -> bool:
        if TripTravelCard.isShort(distance):
            if self._shortTrip > 0:
                self._shortTrip -= 1
                return True
            else:
                if self._longTrip > 0:
                    self._longTrip -= 1
                    self._shortTrip += 3
                    self._shortTrip -= 1
                    return True                
        else:
            if self._longTrip > 0:
                self._longTrip -= 1
                return True
            else:
                if self._shortTrip >= 3:                    
                    self._shortTrip -= 3
                    return True
        return False
    
    def topUp(self):
        long, short = TripTravelCard.topUpLongShortTrips()
        self._shortTrip += short
        self._longTrip += long

    def balanceDetail(self) -> str:
        return f"Long trips: {self._longTrip} Short trips: {self._shortTrip}"
        
        
# q3a

class CustomerCardException(Exception):
    def __init__(self, msg: str):
        Exception.__init__(self, msg)

# q3b

class Customer:

    def __init__(self, name: str):
        self._name = name
        self._cards: dict["str", TravelCard] = {}
    
    def getCard(self, cardNo: str) -> TravelCard:
        if cardNo in self._cards:
            return self._cards[cardNo]
        
    def addCard(self, card: TravelCard) -> bool:
        if card.cardNo in self._cards:
            raise CustomerCardException("Duplicate card number. Card cannot be added")
        else:
            self._cards[card.cardNo] = card
            return True
    
    def travel(self, cardNo: str, trip: Trip) -> bool:
        if cardNo in self._cards:
            return self._cards[cardNo].addTrip(trip)
        else:
            raise CustomerCardException("Cannot locate card for travel")
        
    def topUp(self, cardNo: str) -> bool:
        if cardNo in self._cards:
            if datetime.today() >= self._cards[cardNo].expiryDate:
                raise CustomerCardException("Card has expired. Cannot topup")
            self._cards[cardNo].topUp()
            return True
        raise CustomerCardException("Cannot locate card for topup.")
    
    def getUsableCardNumbers(self, trip: Trip) -> list[str]:
        cards = []
        for cardNo in self._cards:
            if trip.tripDate < self._cards[cardNo].expiryDate and self._cards[cardNo].canTravel(trip.distance):
                cards.append(cardNo)
        if len(cards) == 0:
            raise CustomerCardException("No card can be used for thettrip. Buy a new card or top up a card first.")
        return cards

    def __str__(self):
        lines = []
        lines.append("Name: " + self.name)
        if len(self._cards) == 0:
            lines.append("No card yet")
            return "\n".join(lines)
        else:
            for cardNo in self._cards:
                card = self._cards[cardNo]
                lines.append(f"Card Number: {cardNo} Expiry Date: {card.expiryDate.strftime('%d %B %Y')} {card.balanceDetail()}")
                for trip in card.trips():
                    lines.append(str(trip))
            return "\n".join(lines)

# q3c

def q3c():
    # i
    john = Driver("John", "98989898")
    tom = Driver("Tom", "88998899")
    # ii
    cust = Customer("Peter")
    # iii
    c123 = TripTravelCard("C123", datetime(2021, 6, 30))
    c123.addTrip(Trip(datetime(2020, 5, 30, 12, 35), "Jurong Point", "Parkway Parade", 20.3, tom))
    c123.addTrip(Trip(datetime(2020, 5, 30, 17, 45), "Parkway Parade", "Tampinese Mall", 11, john))
    d31 = TripTravelCard("D031", datetime(2020, 1, 1))

# q3d

import random

def takeATrip(cust: Customer, trip: Trip, drivers: list["Driver"]):
    try:
        tripdate = input("Enter trip date in d/m/YYYY hh:mm format: ")
        date, time = tripdate.split(" ")
        d, m, y = date.split("/")
        hh, mm = time.split(":")
    except:
        print("Trip date must be in d/m/YYYY hh:mm format")
        return
    else:
        try:
            tripDate = datetime(int(y), int(m), int(d), int(hh), int(mm))
        except ValueError:
            print("Date must be numeric")
            return

    startingPoint = input("Enter starting point: ")
    destination = input("Enter destination: ")
    distance = input("Enter distance: ")
    try:
        distance = float(distance)
    except ValueError:
        print("Distance must be a number")
        return
    else:
        if distance <= 0:
            print("Distance must be positive")
            return
    
    driver = random.choice(drivers)
    trip = Trip(tripDate, startingPoint, destination, distance, driver)

    try:
        cardNos = cust.getUsableCardNumbers(trip)
    except CustomerCardException as e:
        print(e)
    else:
        cardNo = cardNos[0]
        card = cust.getCard(cardNo)
        card.addTrip(trip)
        print("Utilising", cardNo, card.balanceDetail())
        print("Take trip: ", True)
        

# q4 a
# containment hierachy of GUI opponents:
# self._win
# |_ dataFrame
# |  |
# |  |_ radioFrame 
# |  |  |_ trip_rdbtn
# |  |  |_ distance_rdbtn
# |  | 
# |  |_ actionFrame
# |     |_ self._travel_btn
# |     |_ self._clear_btn
# |     |_ self._reset_btn
# |
# |_ outputFrame
#    |_ self._scrol_stxt

# q4 b

import tkinter as tk
from tkinter import ttk, scrolledtext

class TravelCardGui:

    def __init__(self):
        self._longTrip = 0
        self._shortTrip = 0
        self._distance = 0.0
        self._win = tk.Tk()
        self._win.title("Travel Card Trip Planner")
        self.create_widgets()
        self._win.geometry("650x310")
        self._win.mainloop()
    
    def enableOutput(self):
        self._scrol_stxt.config(state=tk.NORMAL)
    
    def disableOutput(self):
        self._scrol_stxt.config(state=tk.DISABLED)
    
    def clearOutput(self):
        self.enableOutput()
        self.scrol_stxt.delete(1.0, tk.END)
        self.disableOutput()
        
    def create_widgets(self):
        dataFrame = ttk.Frame(self._win)
        self._distance_lbl = ttk.Label(dataFrame, text="Distance:")
        self._distanceValue = tk.StringVar()
        self._distance_Ety = tk.Entry(dataFrame, width=18, textvariable=self._distanceValue)
        self._distance_lbl.grid(column=0, row=0)
        self._distance_Ety.grid(column=1, row=0, sticky=tk.EW)

        radioFrame = ttk.Frame(dataFrame)
        radioFrame.grid(column=1, row=1, sticky=tk.EW)
        self._cardType = tk.IntVar()
        self._cardType.set(0)
        trip_rdbtn = tk.Radiobutton(radioFrame, text="By Trip", variable=self._cardType, value = 0)
        distance_rdbtn = tk.Radiobutton(radioFrame, text="By Distance", variable=self._cardType, value=1)
        trip_rdbtn.grid(column=1, row=0, sticky=tk.W)
        distance_rdbtn.grid(column=2, row=0, sticky=tk.W)

        actionFrame = ttk.Frame(dataFrame)
        actionFrame.grid(column=1, row=3)
        self._travel_btn = ttk.Button(actionFrame, text="Add Trip", command=self.addTrip)
        self._travel_btn.pack(side=tk.LEFT)
        self._total_btn = ttk.Button(actionFrame, text="Get Total", command=self.getTotal)
        self._total_btn.pack(side=tk.LEFT)
        self._clear_btn = ttk.Button(actionFrame, text="Clear", command=self.clear)
        self._clear_btn.pack(side=tk.LEFT)
        self._reset_btn = ttk.Button(actionFrame, text="Reset", command=self.reset)
        self._reset_btn.pack(side=tk.LEFT)

        dataFrame.pack(side=tk.TOP)
        outputFrame = ttk.Frame(self._win)
        outputFrame.pack(side=tk.TOP)
        self._scrol_stxt = scrolledtext.ScrolledText(outputFrame, width=60, height=10, wrap=tk.WORD)
        self._scrol_stxt.grid(column=0, row=0, sticky="WE", columnspan=2)

    def addTrip(self):
        byTrip, byDistance = 0, 1
        self.enableOutput()
        try:
            distance = float(self._distanceValue.get())
        except ValueError:
            self._scrol_stxt.insert(tk.END, "Invalid input\n")
        else:
            if self._cardType == byTrip:
                if distance <= 12:
                    details = f"long trips = {self._longTrip} short trips = {self._shortTrip} distance = {self._distance}\n"
                    self._scrol_stxt.insert(tk.END, "Before adding trip, accummulated " + details)
                    self._shortTrip += 1
                    details = f"long trips = {self._longTrip} short trips = {self._shortTrip} distance = {self._distance}\n"
                    self._scrol_stxt.insert(tk.END, "After adding trip, accummulated " + details)

                else:
                    details = f"long trips = {self._longTrip} short trips = {self._shortTrip} distance = {self._distance}\n"
                    self._scrol_stxt.insert(tk.END, "Before adding trip, accummulated " + details)
                    self._longTrip += 1
                    details = f"long trips = {self._longTrip} short trips = {self._shortTrip} distance = {self._distance}\n"
                    self._scrol_stxt.insert(tk.END, "After adding trip, accummulated " + details)

            else:
                    # if self._cardType == byDistance:
                    details = f"long trips = {self._longTrip} short trips = {self._shortTrip} distance = {self._distance}\n"
                    self._scrol_stxt.insert(tk.END, "Before adding trip, accummulated " + details)
                    self._distance += distance
                    details = f"long trips = {self._longTrip} short trips = {self._shortTrip} distance = {self._distance}\n"
                    self._scrol_stxt.insert(tk.END, "After adding trip, accummulated " + details)
        self.disableOutput()


    def getTotal(self):
        self.enableOutput()
        longtrips = f"{'long trips':<12} = {str(self._longTrip):>5}X20 = ${str(self._longTrip*20):>6}\n"
        shorttrips = f"{'short trips':<12} = {str(self._shortTrip):>5}X10 = ${str(self._shortTrip*10):>6}\n"
        dist = f"{self._distance:.2f}"
        distance = f"{'distance':<12} = {dist:>6}km = ${dist:>6}\n"
        self._scrol_stxt.insert(tk.END, longtrips)
        self._scrol_stxt.insert(tk.END, shorttrips)
        self._scrol_stxt.insert(tk.END, distance)
        self.disableOutput()

    def clear(self):
        self.enableOutput()
        self._scrol_stxt.delete("1.0", tk.END)
        self._distanceValue.set("")
        self._distanceValue.set(0)
        self.disableOutput()

    def reset(self):
        self._longTrip = 0
        self._shortTrip = 0
        self._distance = 0
        self.clear()

TravelCardGui()