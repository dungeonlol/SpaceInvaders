from GameGenerics import *

class Player(GameGenerics):

    ##Constructor for the player class
    #Initialize the class member variables
    def __init__(self):
        super(Player, self).__init__()
        self.playerX_change = 0
        self.player_image_path = "images/rocket.png"
        self.player_img = pygame.image.load(self.player_image_path)
        self.bullet_path = 'images/bullet.png'
        self.bullet_img = pygame.image.load(self.bullet_path)
        self.control_data = [0, "ready"]

    ## Player function will draw the image across screen.
    # param1 (screen): takes reference to player screen.
    # param2 (image): takes a player sprite image.
    # param3 (x_axis): takes the x axis position which is used to draw image.
    # param4 (y_axis): takes the y axis position which is used to draw image.
    # returns nothing
    def player(self, screen,  x_axis=0, y_axis=0):
        screen.blit(self.player_img, (x_axis, y_axis))

    ## player_controls function allows users to move the sprite in the x axis.
    # param1 (event): takes a player's inputs.
    # param2 (fire_state): takes whether the player is shooting or not.
    # returns integer playerX_change
    def player_controls(self, event, fire_state):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -5
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 5
            if fire_state == "ready":
                if event.key == pygame.K_SPACE:
                    fire_state = "fire"
                    bullet_sound = mixer.Sound("sounds/laser.wav")
                    bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0



        self.control_data[0] = self.playerX_change
        self.control_data[1] = fire_state

        return self.control_data

    ## boundary_control makes sure the rocketship sprite cannot move beyond the borders of the screen.
    # param1 (x_axis) takes the x axis position which is used to draw image.
    # returns integer x_axis
    def boundary_control(self, x_axis):
        if x_axis <= 0:
            x_axis = 0
        elif x_axis >= 736:
            x_axis = 736

        return x_axis

    ## fire_bullets function will draw the image across screen.
    # param1 (screen): takes reference to player screen.
    # param2 (x_axis): takes the x axis position which is used to draw image.
    # param3 (y_axis): takes the y axis position which is used to draw image.
    # returns nothing
    def fire_bullets(self, screen, x_axis=0, y_axis=0):
        screen.blit(self.bullet_img, (x_axis + 20, y_axis + 10))