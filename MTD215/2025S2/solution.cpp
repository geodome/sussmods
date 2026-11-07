// Q1

#include <string>
#include <iostream>

class MovingObject {
    private:
    std::string name;
    double x, y;
    double vx, vy;
    double ax, ay;
    static int counter;

    public:

    MovingObject(std::string name, double x, double y, double vx, double vy, double ax, double ay) {
        this->name = name;
        this->x = x;
        this->y = y;
        this->vx = vx;
        this->vy = vy;
        this->ax = ax;
        this->ay = ay;
        MovingObject::counter += 1;
    }

    void updatePosition(float t) {
        x += vx*t + 0.5*ax*t*t;
        y += vy*t + 0.5*ay*t*t;
        vx += ax*t;
        vy += ay*t;
    }

    void printStatus() {
        std::cout << "Object " << name << " is at position (" << x << ", " << y << ")" << "\n";
    }

    static int get_counter() {
        return counter;
    }
};

int MovingObject::counter = 0;

int main(int argc, char* argv[]) {
    MovingObject a{"a", 10,10,10,10,10,10}, b{"b", 0, 0,50,50,-10,-10};
    for(int i=0; i<10; i++) {
        a.updatePosition(1);
        a.printStatus();
        b.updatePosition(1);
        b.printStatus();
    }
    std::cout << "Number of MovingObject: " << MovingObject::get_counter() << "\n";
}

/*
  
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
    bool availability;
public:
    Student(int id, string name, string status)
    int getID();
};

In this example, the Student::id variable is protected by encapsulation. The private modifier
prevents external program from changing it while its value may be retrieved via the Student::getID() 
method.

Inheritance

A child class may inherit properties or behaviors from its parent class. Inheritance represents the
is-a relationship between the parent and child. However, inherited variables or methods can be overrided.

class DeliveryPartner {
private:
    string bric, driver_license;
public:
    DeliveryPartner(string nric, string license) {
        this->nric = nric;
        this->driver_license = license;
        this->availability = false;
    }
    string get_nric() {
        return this0>nric;
    }
    string get_license() {
        return this->driver_licnese;
    }
    void add_job(string job_id) {
        // some implementation
    }
    void complete_job(string job_id) {
        // some implementation
    }
    float get_cpf() {
        return 0;
    }
    bool is_available() {
        // some implementation 
        // ...
        return this->availability;
    }
    void clock_in() {
        // some implementation..
        this->availability = true;
    }
    voiid clock_out() {
        // some implementation;
        this->availability = false;
    }
};

class FullTimeDeliveryParnter: public DeliveryPartner {
public:
    FullTimeDeliveryPartner(string nric, string license): DeliveryPartner(nric, driver) {}
    float get_cpf() {
        // some implementation
        // ....
        return cpf;
    }
    void apply_leave(const Date& start, const Date& end) {
        // some implementation
    }
};

class PartTimeDeliveryPartner: public Delivery Partner {
public:
    PartimeDeliveryPartner(string nric, string license): DeliveryPartner(nric, driver) {}

};

Both FullTimeDeliveryPartner and PartTimeDeliveryPartner are child classes of DeliveryPartner. THey inaherit all the methods of DeliveryPartner,
including the getters get_licnse() and get_nric(). fullTimeDeliveryPartner;:get_nric() invokes the DeliveryPartner::get_nric()

The nric and driver-license are private variables of the DeliveryParnter class, so the onnly way to access them is via the getter methods. 
Observe the parent class is initialised in the constructuor of the child classes FullTimeDeliver

FullTimeDeliveryPartner overrides the DeliveryPartner::get_cpf() implementation with its own implementation. Also FulLTimeDelveryPartner can apply leaves.
so it has additional method to support that, which is not available in the parent class.

Polymorphism

Polymorphism means many forms. 

Static polymorphism (aka compile-time polymorphism) is achieved by function overloading and operator overloading in C++.

Runtime polymorphism is achieved

class ComplexNumber {
    friend std::ostream& operator<<(std::ostream&, const ComplexNumber&);
private:
    int real, img;
public:
    CompelxNumber(int r, int i) {
        this->real = r;
        this->img = i;
    }
    ComplexNumber operator+(const ComplexNumber& other) {
        return {this->real + other->real, this->img + other->img};
    }
}

std::ostream& operator+(ComplexNumber& a, ComplexNumber& b) {
    return ComplexNumber(a.real+b.real, a.img+b.img);
}

In this example, we overload the insertion operator << to perform a std::cout with the ComplexNumber class.

Another type of polymorphism is run-time polymorphism with abstract base classess (ABC).

An ABC is a class with virtual methodw. During method resolution, C++ will invoke the most latest implementation
of the virtual method instead of defaulting to the virtuak method that was originally declared in the definition of 
the ABC parent.

class Shape {
public:
    Shape() {}
    virtual ~Shaoe() {}
    virtual double Area() {
        return 0;
    }
 };

class Circle: public Shape {
private:
    double r
 public:
    Circle(double radius): Shape() {
        r = radius;
    }
    double Area() override {
        return 3.14*r*r;
    }

 };

class Square: public Shape {
private:
    double s;
 public:
    Circle(double side): Shape() {
        s = side;
    }
    double Area() override {
        return s*s;
    }

 };

 #define SIZE 2
 int main(int argc, char* argv{}) {
    Shape* shapes[SIZE] = {new Circle(1), new Squar(2)};
    // demostrate dynamic pokymorphism by sharing different classes invoke different implementation of the same method name
    for(int i = 0 i < SIZE; i++) {
        std::cout << "Area of Shape " << i << " is " << shapes[i]->Area() << "\n";
    }
    // memory ckeanup
    for(int i = 0 i < SIZE; i++) {
        delete shapes[i];
    }

 } 

 */
    
/** 2(b)

The coding blocks of a SDL event driven program are:

1) Initialisation

This block initialises the various visual components such as the Window, Renderer.

2) Main Loop

Each loop of the Main Loop block performs the following in sequence:
* Event Listening Loop
* Update
* Render
* Delay

The Event Listening Loop polls the event queue and assign a handler for each event. A handler 
may update the state of an entity (e.g. pressing an arrow key moves a Player sprite), pauses 
the animation or terminate thes Main Loop. The Event Listening Loop terminates when the event 
queue is exhusted.

During the Update phase, each entity may have default update action such as updating its 
coordinates for a moving sprite.

During the render phase, first the entire canvas is cleared. Then each entity is rendered.

The Delay block specifies how long each Main Loop will sleep. 16ms of sleep corresponds to
60 frames per second of animation.

4) Close

This block of code is responsible for freeing up resources held by the SDL components.
It is usually invoked when the program exits.

*/

 /** 2(c)

Step 1: import the SDL2_image extension
#include <SDL2/SDL_image.h>

// Step 2: initialise the SDL2_image extension. 
//IMG_INIT_PNG is the flag for loading PNG images.
int img_status = IMG_Init(IMG_INIT_PNG);

// Step 3: Check if initialisation was successful
if(img_status != IMG_INIT_PNG) {
    std::cerr << "SDL2_image error: " << IMG_GetError() << std::endl;
    SDL_Quit();
}

// Step 4: Load the image
SDL_Texture* image = IMG_LoadTexture(gRenderer, "path/to/image.png");

// Step 5: Check if image was loaded
if(image = nullptr) {
    std::cerr << "SDL2_image error: " << IMG_GetError() << std::endl;
    SDL_Quit();
}
*/

// Q3
#include <iostream>
using namespace std;

class Shape {
public:
    // default constructor
    Shape() { 
        // set width, height as 10
        width = height = 10; 
        // increase counter
        Shape::count += 1;
    }
    // parameterised constructor that set width as w, height as h
    Shape(int w, int h): width(w). height(h) {
        // increase counter
        Shape::count += 1;
    }
    // destructor
    ~Shape() {
        // print message to indicate object is destroyed, required by 3c
        cout << "Shaoe(" << width << ", " << height << ") destroyed";
    }
    // overloading the multiplication (*) operator
    Shape operator*(const Shape& s) {
        return Shape(width*s.width, height*s.height);
    }
    // evaulate the area of the shape
    int getArea() { 
        return width*height; 
    }
    // function to display static counter, required by 3b
    static void display_count() {
        cout << "Shape::count = " << Shape::count << "\n";
    }
private:
    int width;
    int height;
    static int count; // added static counter
}; 

// initialise counter at 0
int Shape::count = 0;

int main() {
    Shape A;        // A is a default Shape
    Shape B(4,5);   // B ia a Shaoe of with width 4, height 5
    Shape C = A*B;  // Create C by multiplying A and B
    cout << "Area of Shaoe C: " << C.getArea() << endl;
}

// Q4

// SDL2 requires this version of the main() function. It won't work with the int main() version.
int main(int argc, char* argv[]) {

    // 4(b) missing variables to store rectangle dimensions after prompting user
    int width, height;
    get_rectangle_data(&width, &height);

    // 4(b) missing variable: required for draw_outer_rect() and draw_inner_rect())
    // position the rectangle at the center of the window
    int x = (WIDTH - width)/2;
    int y = (HEIGHT - height)/2,
    SDL_Rect outer{x, y, width, height};
    SDL_Rect inner{(x + GAP, y + GAP, width - 2*GAP, height-2*GAP};

    // 4(b) added missing variables r, g, b for color cycling
    int r, g, b;
    // set the initial color at white
    r = g = b = 255;

    // First initialise SDL2 subsystems
    if(SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        // SD_Init() returns 0 if successful
        std::cerr << SDL_GetError() << "\n";
        // By convention, main() returns non-zero value if error happens
        return 1;
    }

    // 4(b) Missing variable gWindow for the SDL Window
    // SDL_CreateWindow() returns null pointer if error
    // the flags parameter is set 0, so no window flag is turned on.
    SDL_Window* gWindow = SDL_CreateWindow("July 2025 Q4", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, 0);
    if(gWindow == nullptr) {
        std::cerr << SDL_GetError() << "\n";
        SDL_Quit();
        return 1;
    }

    // 4(b) Missing variable gRenderer for the SDL Renderer associated to gWindow
    // required to use with draw_inner_rect()
    SDL_Renderer* gRenderer = SDL_CreateRenderer(gWindow, -1, 0);
    if(gRenderer == nullptr) {
        std::cerr << SDL_GetError() << "\n";
        SDL_DestroyWindow(gWindow);
        SDL_Quit();
        return 1;
    }

    // The main loop

    bool quit = false;
    SDL_Event e;
    while(!quit) {
        // The event loop polls the event queue for GUI events.
        // responsible for assigning event handlers
        while(SDL_PollEvent(&e)) {
            switch(e.type) {
                case SDL_QUIT:
                quit = true;
                std::cout << "quit event triggered\n";
                break;
            }
        }

        // update phase
        // The update phase is empty because there are no graphical objects to update
        // cycle the rgb colors
        cycle_rgb_color(&r, &g, &b);

        // render phase
        // fill the window with white color
        // when rect is set as nullptr, SDL_FilLRect() updates the entire surface instead of the rectangular region defined by rect

        // Render white background
        draw_inner_rect(gRenderer, nullptr, 0xff, 0xff, 0xff);
        // Draw outer green rectangle
        draw_outer_rect(gRenderer, &outer);
        // Draw inner rectangle
        draw_inner_rect(gRenderer, &inner, r, g, b);
        // Update the Window
        SDL_RenderPresent(gRenderer);
        

        // Sleep phase
        // This determines the refresh rate
        // For refresh rate of 60fps, 1000ms/60fps = 17ms per frame
        SDL_Delay(17);
    }

    // Begin cleanup
    SDL_DestroyRenderer(gRenderer);
    SDL_DestroyWindow(gWindow);

    return 0;
}

/*
4(a) For explaination, see the comments in main()

4(c)
Program draws a rectangle on a white background. The rectangle has a green border 
while the color inside the rectangle transistions from black to white in a cycle.

4(d) 
1) Add key down handler for WASD to move the ractangle
2) Apply color cycling wffect to the green rectangle border
*/