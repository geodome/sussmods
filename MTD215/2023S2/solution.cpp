/*
Author: Donaldson Tan

If you need tuition, feel free to contact me at 
maths_and_programming@outlook.sg.  

If you don't understand the solutions provided, you may 
consult me at @geodome via Telegram.  

I provide tuition for the following SUSS undergraduate modules:  

* ENG301  Microprocessor Programming  
* ICT133  Structured Programming  
* ICT162  Object Oriented Programming    
* ICT235  Data Structures and Algorithms
* ICT325  Algorithm Design and Analysis
* ICT330  Database Management Systems
* MTD215  Application of C++ in Multimedia
* MTH105  Fundamentals of Mathematics  
* MTH109  Calculus  
* MTH207  Linear Algebra  
* MTH210  Fundamentals of Probaility
* MTH212  Statistical Analysis
* MTH240  Engineering Mathematics I
* MTH316  Multivariable Calculus  
* MTH321  Engineering Mathematics II
* MTH355  Basic Mathematical Optimisation  

*/

// Question 1

// 1(a) and 1(b)

#include <iostream>
#include <string>
using namespace std;

const int LENGTH = 0;
const int WIDTH = 1;

struct Car {
    string brand;           // this represents the brand
    string model_number;    // this represents the model number
    double dimensions[2];    // the first element is length, 2nd element is width
    int seat_number;        // this represents the seat number
    bool isOMVExceeds40k;   // this represents whether the car's OMV exeeds SGD40k.
};

int main() {
    Car cars[7];
    cars[1] = {"Benz", "CLA180", {4.688, 1.83}, 5, true};
}

// 1(c)

#include <iostream>
using namespace std;

const int LENGTH = 0;
const int WIDTH = 1;

class Car {
    private:
        string brand;
        string model_number;
        double dimensions[2];
        int seat_number;
        bool isOMVExceeds40k;
    public:
        Car();
        Car(string, string, float, float, int, bool);
        ~Car();
};

// Default Constructor
Car::Car() {
    // assign default values
    this->brand = "";
    this->model_number = "";
    this->dimensions[LENGTH] = 0;
    this->dimensions[WIDTH] = 0;
    this->seat_number = 5;
    this->isOMVExceeds40k = false;
}

Car::Car(string brand, string model, float length, float width, int seat, bool exceeds) {
    // used for assigning values this member properties after default constructor was invoked.
    this->brand = brand;
    this->model_number = model;
    this->dimensions[LENGTH] = length;
    this->dimensions[WIDTH] = width;
    this->seat_number = seat;
    this->isOMVExceeds40k = exceeds;
}

// Destructor
Car::~Car() {
    // no further action is needed as no heap memory was allocated.
}

/**
Question 2

2(a)

Line 4:
The purpose of the program is to let the user check the rental price.

Line 6:
Rental Price Table by floor and number of bedrooms.

Line 16:
Ask user what floor

Line 20:
Ask user how many bedrooms

Line 24:
Retrieve rent from the Rental Price Table

2(b)

Line: 7
Bug: The dimension of rents is 4x3 not 4x2.
Solution: int rents[4][3] = {

Line: 9
Bug: Missing comma at the end of the 2nd array.
Solution: Append a comma.

Line 17:
Bug: Missing semi-colon.
Solution: Append semi-colon.

Line: 22
Bug: variable bedroom is misspelled.
Solution: rename bedroom to bedrooms

Line 25:
Bug: The row and column indices for rents[][] are wrong
Solution: The correct row index, column indices are floor-1, bedrooms-1

2(c)

input:
    floor = 1
    bedrooms = 1
output:
    "The cost is S$400"
 */

 // Question 3

#include <string>
#include <iostream>
using namespace std;

class Player {
    private:
        int id;
        string name;
        double cash;
        bool isBankrupt;
        int nAssets;
        string* assets;
    public:
        Player(int,string,bool,int,string[]);
        ~Player();
        bool GameOver_Checker(double payment);
};

// assumes there exists a function that returns the value of a player's asset
double getValue(string asset) {
    // assumes every asset is worthed 100
    return 100;
}

// Constructor
 Player::Player(int id, string name, bool isBankrupt, int n, string assets[]) {
    this->id = id;
    this->name = name;
    this->cash = 10000;
    this->isBankrupt = isBankrupt;
    this->nAssets = n;
    this->assets = new string[n];
    for(int i=0; i<n; i++) {
        this->assets[i] = assets[i];
    }
 }

// Destructor to free this->assets from the heap
 Player::~Player() {
    delete[] this->assets;
 }

// Checks if player will game over if he makes the payment
 bool Player::GameOver_Checker(double payment) {
    // first sum the value of all assets
    double assetsValue = 0;
     for(int i=0; i<this->nAssets; i++) {
        assetsValue += getValue(this->assets[i]);
    }
    // compare payment against player's cash and total asset value
    if(payment > this->cash + assetsValue) {
        cout << "Game over" << endl;
        return true;
    }
    cout << "Continue with game" << endl;
    return false;
 }

 // Question 4

 // 4(a)

 void drawTrapezoid() {
    // Consider the trapezoid defined by 4 points in clockwise direction:
    // (x1, y1) -> (x2, y2) -> (x3, y3) -> (x4, y4) -> (x1, y1)

    int unit = SCREEN_WIDTH / 8;
    int x1 = 2*unit, y1 = 2*unit;
    int x2 = x1 + 4*unit, y2 = y1;
    int x3 = x1 + 3*unit, y3 = y1 + 4*unit;
    int x4 = x1 + unit, y4 = y3;

    SDL_SetRenderDrawColor(gRenderer, 0xFF, 0x00, 0x00, 0xFF);
    SDL_RenderDrawLine(gRenderer, x1, y1, x2, y2); 
    SDL_RenderDrawLine(gRenderer, x2, y2, x3, y3);
    SDL_RenderDrawLine(gRenderer, x3, y3, x4, y4); 
    SDL_RenderDrawLine(gRenderer, x4, y4, x1, y1); 
 
 }

 // 4(b)
 
 void drawStar() {
    // The 5 points of the star actually form a pentagon inside a circle
    // Hence, the 5 points shall be defined with reference to the center of the circle
    // and its angle.

    const double PI = 3.1459;

    // center of circle
    int x0 = SCREEN_WIDTH/2;
    int y0 = SCREEN_HEIGHT/2;
    // radius of circle
    int r = SCREEN_WIDTH/4;

 
    // since the vertex of the star corresponds to the vertex of a pentagon
    int x[5], y[5];
    double increment = 360/5;
    double angle = 0;
    for(int i=0; i<5; i++) {
        x[i] = x0 + (int) r*cos(angle/180*PI);
        y[i] = y0 + (int) r*sin(angle/180*PI);
        angle += increment;
    }

    // set red color
    SDL_SetRenderDrawColor(gRenderer, 0xFF, 0xFF, 0x00, 0x00);
    // draw star in counter-clockwise direction
    SDL_RenderDrawLine(gRenderer, x[0], y[0], x[2], y[2]); 
    SDL_RenderDrawLine(gRenderer, x[2], y[2], x[4], y[4]);
    SDL_RenderDrawLine(gRenderer, x[4], y[4], x[1], y[1]); 
    SDL_RenderDrawLine(gRenderer, x[1], y[1], x[3], y[3]);
    SDL_RenderDrawLine(gRenderer, x[3], y[3], x[0], y[0]);

 }

// 4(c)

void drawCircle() {
    // center of circle
    int x0 = SCREEN_WIDTH/2, y0 = SCREEN_HEIGHT/2;
    int r = SCREEN_WIDTH/4;
    for(int x = 0; x <= r; x++) {
        int y = sqrt(r^2 - x^2);
        SDL_RenderDrawPoint(gRenderer, x0 + x, y0 + y);
        SDL_RenderDrawPoint(gRenderer, x0 + x, y0 - y);
        SDL_RenderDrawPoint(gRenderer, x0 - x, y0 + y);
        SDL_RenderDrawPoint(gRenderer, x0 - x, y0 - y);
    }
}
 