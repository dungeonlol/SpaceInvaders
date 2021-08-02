import random
import math
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
        self.number_of_enemies = 4
        self.x_axis_enemy = []
        self.y_axis_enemy = []
        self.x_axis_bullet = 0
        self.y_axis_bullet = 480
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 28)
        self.collided_enemy_index = 0
        self.set_display_caption_and_icon("Space Invaders", "images/ufo.png")
        self.background = pygame.image.load("images/background.png")
        self.enemy_starting_pos()
        self.main_game_loop()

    ## main_game_loop function handles all the operations of the game.
    def main_game_loop(self):
        active = True
        my_player = Player()
        my_enemy = Enemy()
        changes = 0
        fire_state = "ready"
        mixer.music.set_volume(1)
        mixer.music.load("sounds/backgroundmusic.wav")
        mixer.music.play(-1)

        while active:
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
            for i in range(self.number_of_enemies):
                enemy_x_change = my_enemy.enemy_movements(self.x_axis_enemy[i])
                self.x_axis_enemy[i] += enemy_x_change

                # If one enemy hits left all the enemies move down by one row.
                move_down = my_enemy.enemy_move_down_one_row(self.y_axis_enemy[i])
                if move_down == 40:
                    for j in range(self.number_of_enemies):
                        self.y_axis_enemy[j] += 40

                # Handles logic for game over screen
                # If our spaceship y axis position is 480 the game will end.

                if self.y_axis_enemy[i] > 480:

                    for k in range(self.number_of_enemies):
                        self.y_axis_enemy[k] = 700
                        self.game_over_screen()
                    break

                my_enemy.enemy(self.screen, self.x_axis_enemy[i], self.y_axis_enemy[i])

            if fire_state == "fire":

                self.y_axis_bullet -= 6
                my_player.fire_bullets(self.screen, self.x_axis_bullet, self.y_axis_bullet)

                # If bullet goes past the screen this will reset bullet to starting position and make it stop moving.
                if self.y_axis_bullet <= -5:
                    fire_state = "ready"
                    self.y_axis_bullet = 480

            fire_state = self.handle_collisions(fire_state, self.is_collide())
            self.show_score()
            pygame.display.update()

    def enemy_starting_pos(self):

        for i in range(self.number_of_enemies):
            self.x_axis_enemy.append(random.randint(0, 735))
            self.y_axis_enemy.append(random.randint(0, 150))

    ## is_collide function checks the collision between the bullet and enemy.
    # It returns boolean variable true if the bullet hits the enemy and false of it doesn't
    # This function uses the distance formula to calculate distance between bullet and enemy.
    # distance == square root of ( (x2-x1)^2 + (y2-y1)^2 )
    def is_collide(self):

        for i in range(self.number_of_enemies):
            x_diff_into_two = math.pow(self.x_axis_enemy[i] - self.x_axis_bullet, 2)
            y_diff_into_two = math.pow(self.y_axis_enemy[i] - self.y_axis_bullet, 2)

            distance = math.sqrt(y_diff_into_two + x_diff_into_two)

            if distance < 27:
                self.collided_enemy_index = i
                self.score += 1
                explosion_sound = mixer.Sound("sounds/explosion.wav")
                explosion_sound.play()
                return True

        return False

    ## handle_collisions function resets the enemy and the bullet if the bullet hits the enemy.
    # param1 (fire_state): takes a reference to fire_state.
    # param2 (is_collide): takes is_collide flag.
    # return boolean fire_state.
    def handle_collisions(self, fire_state, is_collide):

        if is_collide:
            for i in range(self.number_of_enemies):
                fire_state = "ready"
                self.y_axis_bullet = 480
                self.x_axis_enemy[self.collided_enemy_index] = random.randint(0, 735)
                self.y_axis_enemy[self.collided_enemy_index] = random.randint(0, 150)

        return fire_state

    def show_score(self, text_x_axis=10, text_y_axis=10):
        score = self.font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score, (text_x_axis, text_y_axis))

    def game_over_screen(self):
        game_over_font = pygame.font.Font("freesansbold.ttf", 64)
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, (200, 250))