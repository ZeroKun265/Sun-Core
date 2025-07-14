import pygame

import globals
from menu_screen import menu_screen
pygame.init()

def main():
    
    screen = pygame.display.set_mode(globals.SCREEN_SIZE, globals.WINDOW_FLAGS)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Sun-Core")
    
    running = True
    while running:
        clock.tick(globals.FPS)
        screen.fill((128, 128, 128))

        if menu_screen(screen, clock) == True:
            running = False
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 
        
        # Fill the screen with black
        pygame.display.flip()  # Update the display

if __name__ == "__main__":    main()