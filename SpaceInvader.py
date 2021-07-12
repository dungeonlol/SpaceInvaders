import random

import pygame.display
from Player import Player
from Enemy import Enemy
from GameGenerics import *


class SpaceInvader(GameGenerics):

    ## Constructor for SpaceInvader
    # Initialize the class member variables.
    def __init__(self):
        super(SpaceInvader, self).__init__()
        self.screen = self.get_screen(800, 600)
        self.x_axis = 370
        self.y_axis = 480
        self.x_axis_enemy = random.randint(0, 736)
        self.y_axis_enemy = random.randint(0, 150)
        self.set_display_caption_and_icon("Space Invaders", "images/ufo.png")
        self.background = pygame.image.load("images/background.png")
        self.main_game_loop()


    ## main_game_loop function sets the image of the rocket sprite, makes it so that everytime the sprite draws it erases the previous drawing, and initializes everything.
    def main_game_loop(self):
        active = True
        my_player = Player()
        my_enemy = Enemy()
        player_image = "Images/rocket.png"
        changes = 0

        while active:
           self.screen.fill((0, 0, 0))
           self.screen.blit(self.background, (0, 0))
           for event in pygame.event.get():
               active = self.close_screen(event, active)
               changes = my_player.player_controls(event)

           self.x_axis += changes
           self.x_axis = my_player.boundary_control(self.x_axis)

           enemy_x_changes = my_enemy.enemy_movements(self.x_axis_enemy)
           self.x_axis_enemy += enemy_x_changes
           self.y_axis_enemy += my_enemy.enemy_move_down_one_row(self.y_axis_enemy)


           my_player.player(self.screen, player_image, self.x_axis, self.y_axis)
           my_enemy.enemy(self.screen, self.x_axis_enemy, self.y_axis_enemy)
           pygame.display.update()




