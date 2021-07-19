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
        self.x_axis_bullet = 0
        self.y_axis_bullet = 480
        self.set_display_caption_and_icon("Space Invaders", "images/ufo.png")
        self.background = pygame.image.load("images/background.png")
        self.main_game_loop()


    ## main_game_loop function handles all the operations of the game.
    def main_game_loop(self):
        active = True
        my_player = Player()
        my_enemy = Enemy()
        changes = 0
        fire_state = "ready"

        while active:
           self.screen.fill((0, 0, 0))
           self.screen.blit(self.background, (0, 0))

           for event in pygame.event.get():
               active = self.close_screen(event, active)
               control_data = my_player.player_controls(event, fire_state)
               changes = control_data[0]

               if fire_state == "ready":
                   fire_state = control_data[1]
                   self.x_axis_bullet = self.x_axis

           # Draws the player across the x axis.
           self.x_axis += changes
           self.x_axis = my_player.boundary_control(self.x_axis)
           my_player.player(self.screen, self.x_axis, self.y_axis)

            # Draws the enemy across the x and y axis.
           enemy_x_changes = my_enemy.enemy_movements(self.x_axis_enemy)
           self.x_axis_enemy += enemy_x_changes
           self.y_axis_enemy += my_enemy.enemy_move_down_one_row(self.y_axis_enemy)
           my_enemy.enemy(self.screen, self.x_axis_enemy, self.y_axis_enemy)
           pygame.display.update()

           if fire_state == "fire":

               self.y_axis_bullet -= 4
               my_player.fire_bullets(self.screen, self.x_axis_bullet, self.y_axis_bullet)

               # If bullet goes past the screen this will reset bullet to starting position and make it stop moving.
               if self.y_axis_bullet <= -5:
                   fire_state = "ready"
                   self.y_axis_bullet = 480

           pygame.display.update()






