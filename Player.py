from GameGenerics import *

class Player(GameGenerics):

    #Constructor for the player class
    #Initialize the class member variables
    def __init__(self):
        super(Player, self).__init__()

    def player(self, screen, image, x_axis=0, y_axis=0):
        player_img = pygame.image.load(image)
        screen.blit(player_img, (x_axis, y_axis))