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

// question 1(a) and 1(b)

#include <string>
using namespace std;

struct Person {
    string name;
    float bmi;
    int age;
    bool isSingaporean;
};

int main() {
    Person persons[10];
    persons[9] = {"John Tan", 25.12, 34, true};
}

// question 1(c)

#include <string>
using namespace std;

class Person {
    private:
        string name;
        float bmi;
        int age;
        bool isSingaporean;
    public:
        Person(); // array requires default constructor
        Person(string, float, int, bool);
};

Person::Person() {}

Person::Person(string name, float bmi, int age, bool isSingaporean) {
    this->name = name;
    this->bmi = bmi;
    this->age = age;
    this->isSingaporean = isSingaporean;
}

int main() {
    Person persons[10];
    persons[9] = Person("John Tan", 25.12, 34, true);
}

// question 2
#include <iostream>
using namespace std;

class Soldier {
    friend ostream& operator<<(ostream&, const Soldier&); // 2d
    friend Soldier operator+(const Soldier&, const Soldier&); // 2c
    private:
        double weight;  // 2a
        double height;  // 2a
        double bmi;     // 2a
    public:
        Soldier(double,double);
        ~Soldier();
};

// 2b
Soldier::Soldier(double weight, double height) {
    this->weight = weight;
    this->height = height;
    this->bmi = weight/(height*height);
}

// 2b
// no heap memory is used, so destructor is an empty function
Soldier::~Soldier() {}

// 2c
Soldier operator+(const Soldier& s1, const Soldier& s2) {
    double height = (s1.height + s2.height)/2;
    double weight = (s1.weight + s2.weight)/2;
    return Soldier(weight, height);
}

// 2d
ostream& operator<<(ostream& o, const Soldier& s) {
    o << "(" << s.weight << "kg, " << s.height <<"m, BMI=" << s.bmi << ")";
    return o;
}

// 2d
int main() {
    Soldier s1 = Soldier(70, 1.7);
    Soldier s2 = Soldier(80, 1.8);
    cout << s1 << " + " << s2 << " = " << s1 + s2 << endl;
}

// question 3

#include <string>
#include <iostream>
using namespace std;

string salesman[10] = {
    "Karter",  "Tristin",  "Rene",  "Brock",  "Antony",  "Phillip", "Charles", "Adriel", "Gregory", "Rudy"
};

int sales[10] = {905,1006,364,2300,1800,2000,1800,2400,364,2400 };

// 3(a)
void totalSales() {
    // sum the total
    double total = 0;
    for(int i = 0; i<10; i++) {
        total += sales[i];
    }
    cout << "The total sales is $" << total << endl;
}

// 3(b)
void averageSales() {
    // calculate total
    double total = 0;
    for(int i = 0; i<10; i++) {
        total += sales[i];
    }
    // divide total by number of salesmen
    double average = total/10;
    cout << "The average sales is $" << average << endl;
}

// 3(c)
void lowestSales() {
    // find lowest sale
    int lowest = sales[0];
    for(int i=0;i<10;i++) {
        if (sales[i] < lowest) {
            lowest = sales[i];
        }
    }
    // find salesman(s) with lowest sales
    cout << "Sales person(s) with lowest sales: ";
    bool hasPrevious = false;
    for(int i=0; i<10; i++) {
        if(sales[i] == lowest) {
            if (hasPrevious) {
                cout << ", ";
            } else {
                hasPrevious = true;
            }
            cout << salesman[i];
        }
    }
    cout << endl;
}

// 3(d)
void highestSales() {
    // find highest sale
    int highest = sales[0];
    for(int i=0;i<10;i++) {
        if (sales[i] > highest) {
            highest = sales[i];
        }
    }
    // find salesman(s) with highest sales
    cout << "Sales person(s) with highest sales: ";
    bool hasPrevious = false;
    for(int i=0; i<10; i++) {
        if(sales[i] == highest) {
            if (hasPrevious) {
                cout << ", ";
            } else {
                hasPrevious = true;
            }
            cout << salesman[i];
        }
    }
    cout << endl;
}

int main() {
    totalSales();
    averageSales();
    lowestSales();
    highestSales();
}

// Question 4

// 4(a)

void drawMultipleRect() {
    int unit = SCREEN_WIDTH/64;
    int x = unit, y = unit;
    bool blue = true;
    for(int row=0; row<10; row++) {
        // to alternate between blue and red colours for each row
        if(blue) {
            SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0xFF, 0xFF);
        } else {
            SDL_SetRenderDrawColor(gRenderer, 0xFF, 0x00, 0x00, 0xFF);
        }
        blue = !blue;
        // begin rendering square for each column
        x = unit;
        for(int col=0; col<10; col++) {
            SDL_Rect r = {x, y, 4*unit, 4*unit};
            SDL_RenderFillRect(gRenderer, &r);
            x += 5*unit;
        }
        // move to next row
        x = unit;
        y += 5*unit;
    }
}

// 4(b)

void drawMultipleTriangle() {
    // setup dimensions
    int unit = SCREEN_WIDTH / 64;
    int x = unit, y = unit;
    // set black color
    SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0x00, 0xFF);
    // start drawing triangles
    for(int n=1; n<7; n++) {
        for(int i=0; i<n; i++) {
            // calculate triangle coordinates
            int x1 = x + 4*unit, y1 = y;
            int x2 = x + 8*unit, y2 = y + 8*unit;
            int x3 = x, y3 = y + 8*unit;
            // draw triangle
            SDL_RenderDrawLine(gRenderer, x1, y1, x2, y2);
            SDL_RenderDrawLine(gRenderer, x2, y2, x3, y3);
            SDL_RenderDrawLine(gRenderer, x3, y3, x1, y1);
            x += 10*unit;
        }
        // move to next row
        x = unit;
        y += 10*unit;
    }
}