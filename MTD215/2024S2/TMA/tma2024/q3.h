//
//  q3.h
//  mtd215
//
//  Created by Donaldson Tan on 27/7/25.
//
#include <string>
#include <iostream>
#include <cstdlib>

std::string padding(int num) {
    if(num < 10) {
        return "   ";
    }
    if(num < 100) {
        return "  ";
    }
    if (num < 1000) {
        return " ";
    }
    return "";
}

void display(int puzzle[]) {
    int index = 0;
    for(int row=0; row<5; row++) {
        std::cout << "+------+------+------+------+------+" << std::endl;
        std::cout << "| ";
        for(int col=0; col<5; col++) {
            std::cout << padding(puzzle[index]) << puzzle[index] << " | ";
            index += 1;
        }
        std::cout << std::endl;
    }
    std::cout << "+------+------+------+------+------+" << std::endl;

}

bool sorted(int puzzle[]) {
    for(int i=1; i<25; i++) {
        if (puzzle[i-1] > puzzle[i]) {
            return false;
        }
    }
    return true;
}

struct coord {
    int row, col;
    int index() {
        return 5*row + col;
    }
};


void askUser(coord *p1, int location) {
    bool p1_valid = false;
    while(!p1_valid) {
        std::cout << "Location " << location << " - Row: ";
        std::cin >> p1->row;
        std::cout << "Location " << location << " - Col: ";
        std::cin >> p1->col;
        p1_valid = -1 < p1->row && p1->row < 5 && -1 < p1->col && p1->col < 5;
        if(!p1_valid) {
            std::cout << "Location " << location << " not valid. " << std::endl;
        }
    }
}

bool adjacent(coord p1, coord p2) {
    if (p1.row == p2.row) {
        return abs(p1.col - p2.col) == 1;
    }
    if(p1.col == p2.col) {
        return abs(p1.row - p2.row) == 1;
    }
    return false;
}

int main(int argc, char* args[]) {
    // generate puzzle
    int puzzle[25];
    for(int i=0; i<25; i++) {
        puzzle[i] = rand() % 10000; // fill each cell with a random number from 0 to 9999
    }

    coord p1, p2;
    while(!sorted(puzzle)) {
        display(puzzle);
        askUser(&p1, 1);
        askUser(&p2, 2);
        if (adjacent(p1, p2)) {
            int temp = puzzle[p1.index()];
            puzzle[p1.index()] = puzzle[p2.index()];
            puzzle[p2.index()] = temp;
            std::cout << "Locations 1, 2 are swapped" << std::endl;
        } else {
            std::cout << "Illegal move: The two coordinates are not adjacent. " << std::endl;
        }
    }
    
    display(puzzle);
    std::cout << "The puzzle is sorted. Exiting game." << std::endl;
}
