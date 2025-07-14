import pygame
import sys

import lastditcheffort as lde
import globals

def menu_screen(screen, clock):
    pygame.display.set_caption("Menu Screen")
    regular_button_theme = lde.ui.button.ButtonTheme(
            source_image="assets/UI/Basic Button.png",
            corners_size=((8, 10), (12, 10), (12, 14), (8, 14)),
            step_size=16, 
            fill_color=(36, 33, 33)
        )
    regular_button = lde.ui.button.BasicButton(size=(100, 50), theme=regular_button_theme)
    regular_button.generate_button_surface()

    running = True
    while running:
        clock.tick()
        screen.fill((210, 0, 0))

        # We regenerate the button surface everytime to scale with the mouse position
        button_position = (50, 50)
        mouse_pos = pygame.mouse.get_pos()
        size = (mouse_pos[0] - button_position[0], mouse_pos[1] - button_position[1])
        if size[0] < 100:
            size = (100, size[1])
        if size[1] < 50:
            size = (size[0], 50)
        
        regular_button.set_size(size)
        regular_button.generate_button_surface()
        regular_button.draw(screen, button_position)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        
        pygame.display.flip()  # Update the display

