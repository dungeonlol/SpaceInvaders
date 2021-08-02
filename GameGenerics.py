import pygame
from pygame import mixer

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class GameGenerics:

    ## Constructor for the GameGenerics class.
    def __init__(self):
        pygame.init()

    ## get_screen function creates a screen for the game.
    # param1 (height): sets default height of screen.
    # param2 (width): sets default width of screen.
    def get_screen(self, height=250, width=250):
        screen = pygame.display.set_mode((height, width))
        return screen

    ## close_screen function allows users to close the screen using the icon and esc key.
    # param1 (event): takes a player's inputs
    # param2 (active): takes a boolean type to determine whether to close the screen or not.
    def close_screen(self, event, active=True):

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                active = False

        if event.type == pygame.QUIT:
            active = False

        return active

    ## set_display_caption_and_icon function gives capabilities to set a custom icon and caption for the program or to keep it as default.
    # param1 (caption): sets default caption of program
    # param2 (image): sets default image of program.
    def set_display_caption_and_icon(self, caption="pygame", image="default"):
        pygame.display.set_caption(caption)

        if image != 'default':
            icon = pygame.image.load(image)
            pygame.display.set_icon(icon)
