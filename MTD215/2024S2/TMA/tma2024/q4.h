//
//  q4.h
//  mtd215
//
//  Created by Donaldson Tan on 27/7/25.
//
#include <string>
#include <iostream>
#include <SDL2/SDL.h>

const int WIDTH = 1612/4 + 5;
const int HEIGHT = 726/2 + 10;
const int SCREEN_WIDTH = WIDTH - 20;
const int SCREEN_HEIGHT = HEIGHT - 20;

SDL_Window *gWindow;
SDL_Surface *gSurface, *stickman;
SDL_Rect rects[8] = {
    SDL_Rect(5,0,WIDTH,HEIGHT),
    SDL_Rect(5+WIDTH,0,WIDTH,HEIGHT),
    SDL_Rect(5+2*WIDTH,0,WIDTH,HEIGHT),
    SDL_Rect(5+3*WIDTH,0,WIDTH,HEIGHT),
    SDL_Rect(5,HEIGHT,WIDTH,HEIGHT),
    SDL_Rect(5+WIDTH,HEIGHT,WIDTH,HEIGHT),
    SDL_Rect(5+2*WIDTH,HEIGHT,WIDTH,HEIGHT),
    SDL_Rect(5+3*WIDTH,HEIGHT,WIDTH,HEIGHT),
};
SDL_Rect btnRect = SDL_Rect(2,5,35,35);

bool init() {
    if(SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cout << SDL_GetError() << std::endl;
        return false;
    }
    gWindow = SDL_CreateWindow("Stickman Animation", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if(gWindow == NULL) {
        std::cout << SDL_GetError() << std::endl;
        return false;
    }
    gSurface = SDL_GetWindowSurface(gWindow);
    return true;
}

bool loadMedia() {
    stickman = SDL_LoadBMP("./stickman.bmp");
    if(stickman == NULL) {
        std::cout << SDL_GetError() << std::endl;
        return false;
    }
    return true;
}

void close() {
    SDL_FreeSurface(stickman);
    SDL_FreeSurface(gSurface);
    SDL_DestroyWindow(gWindow);
    SDL_Quit();
}

int main(int argc, char* argv[]) {
    // initialise SDL
    if(!init()) {
        std::cout << "Initialisation failed" << std::endl;
        close();
        return 1;
    }
    
    // load the stickman sprite sheet
    if(!loadMedia()) {
        std::cout << "Failed to load stickman sprite sheet" << std::endl;
        close();
        return 1;
    }
    
    // start the event loop
    bool animated = true;
    int i = 0;
    bool quit = false;
    SDL_Event e;
    while(!quit) {
        // process the event queue until it is exhuasted
        while(SDL_PollEvent(&e)) {
            switch(e.type) {
                case SDL_QUIT:
                // quit program
                    quit = true;
                    animated = false;
                    break;
                case SDL_MOUSEBUTTONDOWN:
                // toggle animation 
                    if(!quit && e.motion.x >= btnRect.x && e.motion.x - btnRect.x <= btnReact.w) {   
                        if(e.motion.y >= btnRect.y && e.motion.y - btnReact.y <= btnRect.h) { 
                            animated = !animated;
                        }
                    }
                    break;
            }
        }
        // update the stickman animation with next frame
        if(animated) {
            // add stickman
            SDL_BlitSurface(stickman, &rects[i], gSurface, NULL);
            // add red button
            SDL_FillRect(gSurface, &btnRect, SDL_MapRGB(gSurface->format, 0xFF, 0x00, 0x00 ));
            // update surface
            SDL_UpdateWindowSurface(gWindow);
            // move to next frame
            i = (i + 1) % 8;
            SDL_Delay(100);
        }
    }
    close();
    return 0;
}

