// Q4 implementation including main() and the proposed modifications 

#include <SDL2/SDL.h>
#include <iostream>
using namespace std;

const int WIDTH = 640; 
const int HEIGHT = 480; 
const int GAP = 50; 
const int COLOR_SPEED = 2; 

void get_rectangle_data(int* w, int* h) { 
    cout << "Enter width: "; 
    cin >> *w; 
    cout << "Enter height: "; 
    cin >> *h; 
} 

void draw_outer_rect(SDL_Renderer* renderer, SDL_Rect* rect) { 
    SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255); 
    SDL_RenderFillRect(renderer, rect); 
} 

void draw_inner_rect(SDL_Renderer* renderer, SDL_Rect* rect, int r, int g, int b) { 
    SDL_SetRenderDrawColor(renderer, r, g, b, 255); 
    SDL_RenderFillRect(renderer, rect); 
} 

void cycle_rgb_color(int* r, int* g, int* b) { 
    *r = (*r + COLOR_SPEED) % 256; 
    *g = (*g + COLOR_SPEED) % 256; 
    *b = (*b + COLOR_SPEED) % 256; 
} 

// SDL2 requires this version of the main() function. It won't work with the int main() version.
int main(int argc, char* argv[]) {

    int width, height;
    get_rectangle_data(&width, &height);
    int x = (WIDTH - width)/2;
    int y = (HEIGHT - height)/2;
    SDL_Rect outer{x, y, width, height};
    SDL_Rect inner{x + GAP, y + GAP, width - 2*GAP, height-2*GAP};

    int r = rand() % 256;
    int g = rand() % 256;
    int b = rand() % 256;

    int r1 = 0;
    int g1 = 255;
    int b1 = 0;

    // First initialise SDL2 subsystems
    if(SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        // SD_Init() returns 0 if successful
        std::cerr << SDL_GetError() << "\n";
        // By convention, main() returns non-zero value if error happens
        return 1;
    }

    // SDL_CreateWindow() returns null pointer if error
    // the flags parameter is set 0, so no window flag is turned on.
    SDL_Window* gWindow = SDL_CreateWindow("July 2025 Q4", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, 0);
    if(gWindow == nullptr) {
        std::cerr << SDL_GetError() << "\n";
        return 1;
    }

    SDL_Renderer* gRenderer = SDL_CreateRenderer(gWindow, -1, 0);
    if(gRenderer == nullptr) {
        std::cerr << SDL_GetError() << "\n";
        return 1;
    }

    // The main loop consists of
    // * event loop

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
                case SDL_KEYDOWN:
                if(e.key.keysym.scancode == SDL_SCANCODE_W) y = std::max(y - 5, 0);
                if(e.key.keysym.scancode == SDL_SCANCODE_S) y = std::min(y + 5, HEIGHT - height);
                if(e.key.keysym.scancode == SDL_SCANCODE_A) x = std::max(x - 5, 0);
                if(e.key.keysym.scancode == SDL_SCANCODE_D) x = std::min(x + 5, WIDTH - width);
                break;
            }
        }

        // update phase
        // The update phase is empty because there are no graphical objects to update
        cycle_rgb_color(&r, &g, &b);
        cycle_rgb_color(&r1, &g1, &b1);
        outer.x = x;
        outer.y = y;
        inner.x = x + GAP;
        inner.y = y + GAP;

        // render phase
        // fill the window with white color
        // when rect is set as nullptr, SDL_FilLRect() updates the entire surface instead of the rectangular region defined by rect

        draw_inner_rect(gRenderer, nullptr, 0xff, 0xff, 0xff);
        draw_inner_rect(gRenderer, &outer, r1, g1, b1);
        draw_inner_rect(gRenderer, &inner, r, g, b);
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