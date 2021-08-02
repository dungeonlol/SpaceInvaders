from GameGenerics import *


class Enemy(GameGenerics):

    ##Constructor for Enemy class.
    #Initializes the class member variables.
    def __init__(self):
        super(Enemy, self).__init__()
        self.enemy_image = "images/alien.png"
        self.enemy_img = pygame.image.load(self.enemy_image)
        self.flag_move_right = True
        self.flag_move_down = False

    ## enemy function will draw the image across screen.
    # param1 (screen): takes reference to player screen.
    # param2 (x_axis): takes the x axis position which is used to draw image.
    # param3 (y_axis): takes the y axis position which is used to draw image.
    # returns nothing
    def enemy(self, screen, x_axis=0, y_axis=0):
        screen.blit(self.enemy_img, (x_axis, y_axis))

    ## enemy_movements function moves enemies across the screen in the x axis.
    # param1 (x_axis: takes position of x_axis.
    # return integer x_axis
    def enemy_movements(self, x_axis):

        if x_axis < 0:
            self.flag_move_right = True
        elif x_axis > 736:
            self.flag_move_right = False
            self.flag_move_down = True
        elif x_axis == 0:
            self.flag_move_right = False
            self.flag_move_down = True
        elif x_axis < 736:
            self.flag_move_down = False

        if self.flag_move_right:
            x_axis = 1
        else:
            x_axis = -1

        return x_axis

    ## enemy_move_down_one_row function moves enemies one row down after reaching the right edge of our screen.
    # param1 (y_axis): takes position of y_axis.
    # returns integer down_by.
    def enemy_move_down_one_row(self, y_axis):

        down_by = 0

        if self.flag_move_down and y_axis <= 510:
            down_by = 40
        else:
            down_by = 0

        return down_by



