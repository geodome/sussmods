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
#include <iostream>
using namespace std;

class Cart {
    friend void displayCart(const Cart&);
    private:
        int id;
        int quantity;
        string owner;
        string* items;
    public:
        Cart();
        Cart(int, string, int, string*);
    ~Cart();
};

Cart::Cart() {
    // assign default values
    this->id = 0;
    this->quantity = 2;
    this->owner = "owner";
    this->items = new string[2];
    this->items[0] = "Pencil";
    this->items[1] = "Eraser";
}

Cart::Cart(int id, string owner, int qty, string* items) {
    this->id = id;
    this->quantity = qty;
    this->owner = owner;
    this->items = new string[qty];
    for(int i=0; i<qty; i++) {
        this->items[i] = items[i];
    }
}

Cart::~Cart() {
    delete [] this->items;
}

void displayCart(const Cart& c) {
    cout << "In friend function" << endl;
    cout << "Card Id: " << c.id << " Owner: " << c.owner << " Number of Items: " << c.quantity << endl;
    if(c.quantity > 0) {
        cout << "Items are: " << endl;
        for(int i=0; i<c.quantity; i++) {
            cout << c.items[i] << endl;
        }
    }
}

int main() {
    Cart c1;
    displayCart(c1);

    string items[3] = {"Pen", "Pencil", "Eraser"};
    Cart c2 = Cart(1, "Tiffany Tan", 3, items);
    displayCart(c2);
}

// Question 2

#include <iostream>
using namespace std;

const double PI = 3.14159;

class Cylinder {
    friend istream& operator>>(istream&, Cylinder&); // 2d
    friend ostream& operator<<(ostream&, Cylinder&); // 2e
    friend bool operator>(Cylinder&, Cylinder&); // 2f
    private:
        int radius;  // 2a
        int height;  // 2a
    public:
        Cylinder(); // default constructor required for 2g implementation
        Cylinder(int,int); // 2b
        double volume(); //2c
};

// default constructor is required when invoking >>
Cylinder::Cylinder() {
    this->radius = 0;
    this->height = 0;
}

// parameterised constructor
Cylinder::Cylinder(int radius, int height) {
    this->radius = radius;
    this->height = height;
}

// calculate cylinder volume
double Cylinder::volume() {
    return PI*this->radius*this->radius*this->height;
}

// overloading >> operator
istream& operator>>(istream& in, Cylinder& c) {
    cout << "Enter radius: ";
    in >> c.radius;
    cout << "Enter height: ";
    in >> c.height;
    return in;
}

// overloading << operator
ostream& operator<<(ostream& out, Cylinder& c) {
    out << "Radius of Cylinder: " << c.radius << " and height of Cylinder: " << c.height << endl;
    out << "Volume of Cylinder: " << c.volume() << endl;
    return out;
}

// overloading the > operator
bool operator>(Cylinder& c1, Cylinder& c2) {
    return c1.volume() > c2.volume();
}
// 2g
int main() {
    int n;
    cout << "number of cylinders: ";
    cin >> n;
    cout << endl;
    // create n cylinders
    Cylinder* cylinders = new Cylinder[n];
    int biggest = 0;
    for(int i=0; i<n; i++) {
        // ask for user input
        cout << "Cylinder details" << endl;
        cin >> cylinders[i];
        cout << endl;
        // find the  bigget cylinder
        if(cylinders[i] > cylinders[biggest]) {
            biggest = i;
        }
    }
    cout << "The largest colume of Cylinder is " << cylinders[biggest].volume() << endl;
    // destroy cylinders
    delete [] cylinders;
}

// Question 3

#include <string>
#include <iostream>
using namespace std;

// added Bank Class from question paper. This is not part of the answer.
class Bank {
private:
    int bankCode;
    string bankName;
    int branchCode;
public:
    Bank(int,string,int);
    void display();
};

Bank::Bank(int bc, string bn, int branch) {
    bankCode = bc;
    bankName = bn;
    branchCode = branch;
}

void Bank::display() {
    cout << "Bank Name: " << bankName << " Branch Code: " << branchCode <<  endl;
}

// answwer for q4 starts here
class BankAccount: public Bank {
    private:
        int account;
        int type;
        string username;
    public:
        BankAccount(int, string, int, int, int, string);
        void display();
};

BankAccount::BankAccount(int bankCode, string bankName, int branchCode, int account, int type, string username):Bank(bankCode, bankName, branchCode)
{
    this->account = account;
    this->type = type;
    this->username = username;
}

void BankAccount::display(){
    Bank::display();
    cout << "Account name: " << this->username << " and Account number: " << this->account << endl;
}

int main() {
    BankAccount ann = BankAccount(123, "ABC Bank", 1, 12345, 1, "Ann Lim");
    ann.display();
}
// Question 4

void drawTriangles(int x, int y, int unit) {    
    for(int i = 0; i<4; i++) {
        // Setup coordinates for blue triangle
        int x1 = x + 4*unit, y1 = y;
        int x2 = x + 8*unit, y2 = y + 8*unit;
        int x3 = x, y3 = y + 8*unit;
        // Draw Blue Triangle
        SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0xFF, 0xFF);
        SDL_RenderDrawLine(gRenderer, x1, y1, x2, y2);
        SDL_RenderDrawLine(gRenderer, x2, y2, x3, y3);
        SDL_RenderDrawLine(gRenderer, x3, y3, x1, y1);
        // Setup Coordinates for Red Triangle
        int x4 = x + 6*units, y4 = y;
        int x5 = x4 + 8*units, y5 = y;
        int x6 = x4 + 4*units, y6 = y2;
        // Draw Red Triangle
        SDL_SetRenderDrawColor(gRenderer, 0xFF, 0x00, 0x00, 0xFF);
        SDL_RenderDrawLine(gRenderer, x4, y4, x5, y5);
        SDL_RenderDrawLine(gRenderer, x5, y5, x6, y6);
        SDL_RenderDrawLine(gRenderer, x6, y6, x4, y4);
        x += 14*unit;
    }
}
    
void drawIrregularRectangles(int x, int y, int unit) {
    for(int i=0; i<4; i++) {
        // Setup coordinate for red trapezoid
        int x1 = x + 2*unit, y1 = y;
        int x2 = x + 4*unit, y2 = y1;
        int x3 = x + 8*unit, y3 = y + 8*unit;
        int x4 = x, y4 = y3;
        // Draw red trapezoid
        SDL_SetRenderDrawColor(gRenderer, 0xFF, 0x00, 0x00, 0xFF);
        SDL_RenderDrawLine(gRenderer, x1, y1, x2, y2);
        SDL_RenderDrawLine(gRenderer, x2, y2, x3, y3);
        SDL_RenderDrawLine(gRenderer, x3, y3, x4, y4);
        SDL_RenderDrawLine(gRenderer, x4, y4, x1, y1);
        // Setup coordinate for blue trapezoid
        int x5 = x + 9*unit, y5 = y;
        int x6 = x5 + 8*unit, y6 = y;
        int x7 = x + 13*unit,  y7 = y + 8*unit;
        int x8 = x + 9*unit, y8 = y7;
        // Draw blue trapezoid
        SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0xFF, 0xFF);
        SDL_RenderDrawLine(gRenderer, x5, y5, x6, y6);
        SDL_RenderDrawLine(gRenderer, x6, y6, x7, y7);
        SDL_RenderDrawLine(gRenderer, x7, y7, x8, y8);
        SDL_RenderDrawLine(gRenderer, x8, y8, x5, y5);
        // move to next pair of trapezoid
        x += 13*unit;
    }
}

void drawMixShapes(int x, int y, int unit) {
    for(int i=0; i<4; i++) {
        // setup coordinates for blue triangle
        int x1 = x + 4*unit, y1 = y;
        int x2 = x + 8*unit, y2 = y + 8*unit;
        int x3 = x, y3 = y2;
        // draw blue triangle
        SDL_SetRenderDrawColor(gRenderer, 0x00, 0x00, 0xFF, 0xFF);
        SDL_RenderDrawLine(gRenderer, x1, y1, x2, y2);
        SDL_RenderDrawLine(gRenderer, x2, y2, x3, y3);
        SDL_RenderDrawLine(gRenderer, x3, y3, x1, y1);
        // setup coordinate for red trapezoid
        int x4 = x + 8*unit, y4 = y;
        int x5 = x5 + 8*unit, y5 = y;
        int x6 = x + 13*unit, y6 = y + 8*unit;
        int x7 = x + 9*unit, y7 = y6;
        // draw red trapzoid
        SDL_SetRenderDrawColor(gRenderer, 0xFF, 0x00, 0x00, 0xFF);
        SDL_RenderDrawLine(gRenderer, x4, y4, x5, y5);
        SDL_RenderDrawLine(gRenderer, x5, y5, x6, y6);
        SDL_RenderDrawLine(gRenderer, x6, y6, x7, y7);
        SDL_RenderDrawLine(gRenderer, x7, y7, x4, y4);
        // proceed to next pair of shapes        
        x += 14*unit;
    }
}

int main(int argc, const char *argv[]) { 
     
    SDL_Init(SDL_INIT_VIDEO); 
    // Remmeber to replace student name and PI
    gWindow = SDL_CreateWindow("Student Name and PI", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN); 
     
    gRenderer = SDL_CreateRenderer(gWindow, -1, SDL_RENDERER_ACCELERATED); 
    SDL_SetRenderDrawColor(gRenderer, 0xFF, 0xFF, 0xFF, 0xFF); 
     
    SDL_Event event; 
    bool quit = false; 
     
    while(!quit) { 
        while (SDL_PollEvent(&event)) { 
            if (event.type == SDL_QUIT) { 
                quit = true; 
            } 
             
            SDL_SetRenderDrawColor(gRenderer, 0xFF, 0xFF, 0xFF, 0xFF); 
            SDL_RenderClear(gRenderer); 

            int unit = SCREEN_WIDTH/64;
            int x = unit, y = unit;

            drawTriangles(x, y, unit);
            y += 10*unit;
            drawIrregularRectangles(x, y, unit);
            y += 10*unit;
            drawMixShapes(x, y, unit); 

            SDL_RenderPresent(gRenderer); 
        } 
    } 
 
    SDL_DestroyRenderer(gRenderer); 
    SDL_DestroyWindow(gWindow); 
    gWindow = NULL; 
    gRenderer = NULL; 
    SDL_Quit(); 
} 

