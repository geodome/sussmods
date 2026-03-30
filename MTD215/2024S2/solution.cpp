// question 1

#include <iostream>
#include <string>
using namespace std;

class Car {
private:
    string driver;
    string model;
    double max_speed;
    double speed = 0;
    int nitro = 3;
    int max_nitro = 3;
    double acceleration = 2;
public:
    Car(string, string, double);
    double accelerate(double time);
};

Car::Car(string driver, string model, double max_speed) {
    this->driver = driver;
    this->model = model;
    this->max_speed = max_speed;
}

double Car::accelerate(double time) {
    // double acceleration if nitro is available
    if (this->nitro > 0) {
        // assumes 1 unit of nitro is used per acceleration
        this->nitro -= 1;
        // double the acceleration
        this->acceleration = 2*this->acceleration;
        // cap car speed at max_speed
        this->speed = min(this->max_speed, this->speed + this->acceleration*time);
        // restore acceleration
        this->acceleration = this->acceleration / 2;
        return this->speed;
    }
    // cap car speed at max_speed
    this->speed = min(this->max_speed, this->speed + this->acceleration*time);
    return this->speed;
}

/**
2(a)

Abstraction

A minimal set of features that can be used to model an entity. What features are
relevant would depend on the modelling context. 

For example, a Student entity within the context of a university can be sufficiently
described with a name, student id and his student status (enrolled/deferred/graduated/discontinued).
Within the academic context of a university, his other characteristics (e.g. height, weight, 
blood pressure) are not relevant to the model and therefore excluded.

class Student {
private:
    int id;
    string name, status;
public:
    Student(int id, string name, string status)
};

Encapsulation

Encapsulation works by hiding an object's internal state and processes and exposes public
methods to interact with the object's internal states. In this way, it protects the internal
state from accidental modification and also simplifies interaction with other components of
the program as the programmer is not required to know internally how the public method works.

class Student {
private:
    int id;
    string name, status;
public:
    Student(int id, string name, string status)
    int getID();
};

In this example, the Student::id variable is protected by encapsulation. The private modifier
prevents external program from changing it while its value may be retrieved via the Student::getID() 
method.

Inheritance

A child class may inhert properties or behaviors from its parent class. However, inherited
variables or methods can be overrided.

class Rectangle {
private:
    int length, width;
public:
    Rectangle(int l, int w) {
        length = l;
        width = w;
    }
    int Area() {
        return length*width;
    }
    int Perimenter {
        return 2*(length + width);
    }
};

class Square: public Rectangle {
private:
    int side;
public:
    Square(int s):Rectangle(s,s) {
        side = s;
    }
}

The Square class inherits from the Rectangle class. The Square::Area() and Square::Perimeter()
methods may be called.

Polymorphism

Polymorphism means many forms. This is achieved by function overloading and operator overloading in C++.

class ComplexNumber {
    friend ComplexNumber operator+(ComplexNumber&, ComplexNumber&);
private:
    int real, img;
public:
    CompelxNumber(int r, int i) {
        this->real = r;
        this->img = i;
    }
}

ComplexNumber operator+(ComplexNumber& a, ComplexNumber& b) {
    return ComplexNumber(a.real+b.real, a.img+b.img);
}
    
2(b)

The coding blocks of a SDL event driven program are:

1) SDL Initialisation

This block initialises the various visual components such as the Window, Renderer.

2) Initial Render

This setups the initial visualisation

3) Event Listener and Event Handler

This is an event loop that polls the system for events like mouse down, key down,
exit event and assigns an event handler to process these events. The event handlers
may respond in many ways, such as pausing an animation, or updating how a button is
displayed after it is clicked.


4) Close

This block of code is responsible for freeing up resources held by the SDL components.
It is usually invoked when the program exits.


 3(a)

 07: Default Constructor
 14: Parameterised Constructor
 19: Destructor. No clean-up required as no heap memory was allocated.
 22: Handler for overloading the + operator
 41: Create 2 rectangles
 
 3(b)

 Line   Error                                           Correction
 16     Nx is typo                                      width = nx;
 25.    operator+() cannot read p1's private variables  Use p1.getWidth() and p1.getHeight()
 26     cout after return                               swap lines 25 and 26.
 42     ptA() is function prototype                     Rectangle ptA;
 43     missing semicolon                               ectangle ptB(3,4);

 3(c)

 a default rectangle created...
 The sum of RectangleA and RectangleB is:= (8,9)

 */

// Question 4

// 4(a)
void interface(int* length, int* width) {
    cout << "Please input the length of the rectangle in unit of pixels" << endl;
    cin >> *length;
    cout << "Please input the width of the rectangle in unit oif pixels" << endl;
    cin >> *width;
}

// 4(b)
void draw_rect2(SDL_Renderer* renderer, SDL_Rect* rect2) {
    // the dimensions of rect2 are already calculated using user input and RECT_GAP in line 44, 45
    // green colour 
    SDL_SetRenderDrawColor(renderer, 0x00, 0xFF, 0x00, 0xFF);
    // draw green rectangle
    SDL_RenderFillRect(renderer, rect2);
    // update the display
    SDL_RenderPresent(renderer);
}

// 4(c)
void draw_rect1(SDL_Render* renderer, SD:+Rect* rect1, int r, int g, int b) {
    // set color
    SDL_SetRenderDrawColor(renderer, r, g, b, 0xFF);
    // draw rect1
    SDL_RenderFillRect(renderer, rect1);
    // update the display
    SDL_RenderPresent(renderer);
    // set frame rate to 60 frames per second
    // Period of each frame = 1000 ms / 60 frames = 16.66 ms per frame
    SDL_Delay(17);
}

// 4(d)
void change_color(uint8_t* r, uint8_t* g, uint8_t* b) {
    // Uint8 is deprecated and has been replaced with uint8_t
    // set unit of color change
    uint8_t unit = 10;
    // no need to perform modulus as unsigned integers will reset to 0 when 1 is added to 255.
    *r = *r + COLOR_CHANGE_SPEED*unit;
    *g = *g + COLOR_CHANGE_SPEED*unit;
    *b = *b + COLOR_CHANGE_SPEED*unit;
}

