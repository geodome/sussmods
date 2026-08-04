// question 1
#include <string>
#include <iostream>

class MovingObject {
private:
    // required for 1(a)
    std::string name;
    double x, y;
    double vx, vy;
    double ax, ay;
public:
    static int count;
    MovingObject(std::string name, double x, double y, double vx, double vy, double ax, double ay) {
        // required for 1(a)
        this->name = name;
        this->x = x;
        this->y = y;
        this->vx = vx;
        this->vy = vy;
        this->ax = ax;
        this->ay = ay;
        // required for 1(e)
        MovingObject::count += 1;
    }

    void updatePosition(double t) {
        // required for 1(b)
        x += vx*t + 0.5*ax*t*t;
        vx += ax*t;
        y += vy*t + 0.5*ay*t*t;
        vy += ay*t;
    }

    void printStatus() {
        // required for 1(c)
        // pass the instance's x, y and name to std::cout to print to screen
        std::cout << "Object " << name << " is at position (" << x << ", " << y << ")" << std::endl;
    }
};

// initialise static variable count at 0
int MovingObject::count = 0;

int main(int argc, char* argv[]) {
    // required for 1(d)
    MovingObject a{"a", 0,0,1,0,0,1}, b{"b",100,100,0,1,0,1};
    for(int i = 0; i < 10; i++) {
        a.updatePosition(1);
        a.printStatus();
        b.updatePosition(1);
        b.printStatus();
    }
    // required for 1(e)
    std::cout << "Total number of Moving Objects: " << MovingObject::count << std::endl;
}