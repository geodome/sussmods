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
#include <string>
using namespace std;

// 1(a) and 1(b)

struct harddisk {
    string model;
    char colour;
    float price;
    int capacity;
};

int main() {
    harddisk items[10];
    items[9].model = "MTD215 Smart Drive";
    items[9].colour ='R';
    items[9].price = 98.76;
    items[9].capacity = 2;
}

// 1(c)

#include <string>
using namespace std;

class HardDisk {
    private:
        string model;
        char colour;
        float price;
        int capacity;
    public:
        HardDisk();
        HardDisk(string, char, float, int);
};

HardDisk::HardDisk() {
    // assign default values
    this->model = "Generic";
    this->colour = 'R';
    this->price = 0;
    this->capacity = 1;
};

HardDisk::HardDisk(string model, char colour, float price, int capacity) {
    this->model = model;
    this->colour = colour;
    this->price = price;
    this->capacity = capacity;
}

int main() {
    HardDisk items[10];
    items[9] = HardDisk("MTD215 Smart Drive", 'R', 98.76, 2);
}


// Question 2

#include <iostream>
using namespace std;

class ComplexNumber {
    friend ostream& operator<<(ostream&, const ComplexNumber&);
    friend ComplexNumber operator+(const ComplexNumber&, const ComplexNumber&);
    friend ComplexNumber operator*(const ComplexNumber&, const ComplexNumber&);
    private:
        int real;
        int img;
    public:
        ComplexNumber(int,int);
        ~ComplexNumber();
};

ComplexNumber::ComplexNumber(int real, int img) {
    this->real = real;
    this->img = img;
}

ComplexNumber::~ComplexNumber() {
    // no clean-up required as there was no memory allocation from the heap.
}

ComplexNumber operator+(const ComplexNumber& c1, const ComplexNumber& c2) {
    int a = c1.real;
    int b = c1.img;
    int c = c2.real;
    int d = c2.img;
    return ComplexNumber(a+c, b+d);
}

ComplexNumber operator*(const ComplexNumber& c1, const ComplexNumber& c2) {
    int a = c1.real;
    int b = c1.img;
    int c = c2.real;
    int d = c2.img;
    // this is the formula from the exam paper
    return ComplexNumber(a*c - b*d, a*d + b*c);
}

ostream& operator<<(ostream& s, const ComplexNumber& c) {
    s << c.real << " + " << c.img << "i";
    return s;
}

int main() {
    ComplexNumber c1 = ComplexNumber(5,8);
    ComplexNumber c2 = ComplexNumber(2,7);
    cout << "(" << c1 << ") + (" << c2 << ") = (" << c1 + c2 << ")" << endl;
    cout << "(" << c1 << ") * (" << c2 << ") = (" << c1 * c2 << ")" << endl;
}

// Question 3

/* 3(a)

i.      The output is 1 because index 3 refers to the 4th element of the mtdArray array.
ii.     The output is 7 because the result is the sum of elements at indices 0 and 4 of the mtdArray array.
iii.    The output is 3 because mtdArray[4] - mtdArray[3] = 7 - 1 = 6, so the element at index 6 is retrieved
*/

/* 3(b)

char c = 'M';
char* pChar = &c;
*pChar = c + 1;
cout << *pChar << endl;

The output for cout is N.
*/

// 3(c)

#include <string>
using namespace std;

class MyBook {
    private:
        int numOfBooks;
        string* titles;
    public:
        MyBook(int, string[]);
        ~MyBook();
};

MyBook::MyBook(int num, string titles[]) {
    this->numOfBooks = num;
    this->titles = new string[num];
    for(int i=0; i<num; i++) {
        this->titles[i] = titles[i];
    }
}

MyBook::~MyBook() {
    delete[] this->titles;
}

int main() {
    string titles[2] = {"Lord of the Ring", "The Jackal"};
    MyBook m = MyBook(2, titles);
}


// Question 4

// (a)i. Sixteen squares

void drawShape() {
    int unit = SCREEN_WIDTH / 32;
    int x = unit, y = unit;
    bool fillBlack = true;
    for(int i = 0; i < 4; i++) {
        for(int j=0; i<4; j++) {
            // alternate between black and white squares
            if(fillBlack) {
                SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0x00, 0xFF);
            } else {
                SDL_SetRenderDrawColor(gRenderer, 0xFF, 0xFF, 0xFF, 0xFF);
            }
            fillBlack = !fillBlack;
            // fill rectangle
            SDL_Rect r = {x, y, 4*unit, 4*unit};
            SDL_RenderFillRect(gRenderer, r);
            // move to next rectange
            x += 5*unit;
        }
        fillBlack = !fillBlack;
        x = unit;
        y += 5*unit;
    }
}

// (a)ii. Ten Triangles

void drawShape() {
    // Setup dimensions
    int n = 4;
    int unit = SCREEN_WIDTH / 32;
    int x = unit, y = unit;

    // Draw in black colour
    SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0x00, 0xFF);     

    while(n > 0) {
        for(int i=0; i<n; i++) {
            // Setup coordinates for each triangle
            int x1 = x + 2*unit, y1 = y;
            int x2 = x + 4*unit, y2 = y + 4*unit;
            int x3 = x, y3 = y2;
            // Draw Triangle
            SDL_RenderDrawLine(gRenderer, x1, y1, x2, y2);     
            SDL_RenderDrawLine(gRenderer, x2, y2, x3, y3);     
            SDL_RenderDrawLine(gRenderer, x3, y3, x1, y1);
            // move to next triangle
            x += 5*unit;
        }
        n--;
        // move to next row
        x = unit;
        y += 5*unit;
    }
}

/* 4(b)
Initialisation: TTF_Init()
Load: TTF_OpenFont()
Close: TTF_CloseFont()
Render: TTF_RenderText_Blended()
*/