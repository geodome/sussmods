#include <SDL2/SDL.h>
#include <iostream>

using namespace std;

class Rectangle {
    friend void render(const Rectangle&);
    
private:
    int Length, Width;
    
public:
    Rectangle(int l, int w) {
        Length = l;
        Width = w;
    }
    
    int perimeter() { return 2 * (Length + Width); }
    
    double aspectRatio() { return double(Length) / double(Width); }
    
    int area() { return Length * Width; }
    
};

const int SCREEN_WIDTH = 800;
const int SCREEN_LENGTH = 600;
SDL_Window *gWindow;
SDL_Surface *gSurface;

Rectangle promptUser() {
    int length, width;
    
    do {
        cout << "Enter rectangle width (max width " << SCREEN_WIDTH << "): ";
        cin >> width;
    } while (width < 0 || width > SCREEN_WIDTH);
    
    do {
        cout << "Enter rectangle length (max length " << SCREEN_LENGTH << "): ";
        cin >> length;
    } while (length < 0 || length > SCREEN_LENGTH);
    
    cout << endl;

    Rectangle r = Rectangle(length, width);
    cout << "rectangle perimieter is " << r.perimeter() << endl;
    cout << "rectangle aspect ratio is " << r.aspectRatio() << endl;
    cout << "rectangle area is " << r.area() << endl << endl;

    return r;
}

bool init() {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        cout << SDL_GetError() << endl;
        return false;
    }
    gWindow = SDL_CreateWindow(
        "Displaying Rectangle", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        SCREEN_WIDTH, SCREEN_LENGTH, SDL_WINDOW_SHOWN);
    if(gWindow == NULL) {
        cout << SDL_GetError() << endl;
        return false;
    }
    
    gSurface = SDL_GetWindowSurface(gWindow);
    if(gSurface == NULL) {
        cout << SDL_GetError() << endl;
        return false;
    }
    
    return true;
}

void render(const Rectangle& r) {
    SDL_FillRect(gSurface, NULL, SDL_MapRGB(gSurface->format, 0xFF, 0xFF, 0xFF));
    SDL_Rect sr = SDL_Rect((SCREEN_WIDTH - r.Width) / 2,
                           (SCREEN_LENGTH - r.Length) / 2,
                           r.Width,
                           r.Length);
    SDL_FillRect(gSurface, &sr, SDL_MapRGB(gSurface->format, 0xFF, 0x00, 0x00));
    SDL_UpdateWindowSurface(gWindow);
}

void close() {
    SDL_FreeSurface(gSurface);
    SDL_DestroyWindow(gWindow);
    SDL_Quit();
}

int main(int argc, char* args[]) {

    Rectangle r = promptUser();

    if (!init()) {
        cout << "Failed to initialise SDL2" << endl;
        return 1;
    }

    render(r);
    
    SDL_Event event;
    bool quit = false;
    while (!quit) {
        // event handling
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
                cout << "quiting" << endl;
            }
        }
    }
    
    close();
    return 0;
}
