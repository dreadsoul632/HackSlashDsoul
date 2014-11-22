__author__ = 'Simon'

import pygame
import Constants
from Platforms import MovingPlatform
from Spritesheet_functions import SpriteSheet


class EntityPlayer(pygame.sprite.Sprite):
    """This class represent the main character, me of course"""

    # Initialise the speed vector
    speed_vector_x = 0
    speed_vector_y = 0

    # This holds all the images for the walking animation
    walking_frames_l = []
    walking_frames_r = []

    # This hold the direction the player is facing
    direction = 'R'
    _isRunning = False

    # List of sprites we can touch
    level = None

    def __init__(self, sprite_path):
        """ Constructor function """

        # Constructor of parent
        pygame.sprite.Sprite.__init__(self)

        self.sprite = sprite_path
        #width : 130
        #height : 194

        """ Set the sprite """
        sprite_sheet = SpriteSheet(sprite_path)

        # Load all the left facing images into a list
        image_x = 40

        for x in range(0, 4):
            image = sprite_sheet.get_image(image_x, 5, 40, 60)
            self.walking_frames_l.append(image)
            image_x += 40

        # Load all the left facing images, then flip them
        # to face right.
        image_x = 40

        for x in range(0, 4):
            image = sprite_sheet.get_image(image_x, 5, 40, 60)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_r.append(image)
            image_x += 40

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.speed_vector_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.speed_vector_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_vector_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # See if we hit the screen limit
        if self.rect.right > Constants.SCREEN_WIDTH:
            self.rect.right = Constants.SCREEN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > Constants.SCREEN_HEIGHT:
            self.rect.bottom = Constants.SCREEN_HEIGHT
        elif self.rect.top < 0:
            self.rect.top = 0

        # Move up/down
        self.rect.y += self.speed_vector_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.speed_vector_y > 0:
                self.rect.bottom = block.rect.top
            elif self.speed_vector_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.speed_vector_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.speed_vector_y == 0:
            self.speed_vector_y = 1
        else:
            self.speed_vector_y += .35

        # See if we are on the ground.
        if self.rect.y >= Constants.SCREEN_HEIGHT - self.rect.height and self.speed_vector_y >= 0:
            self.speed_vector_y = 0
            self.rect.y = Constants.SCREEN_HEIGHT - self.rect.height

    # Player-controlled movement:
    def jump(self):
        """ Called when the user hits the jump button """
        self.rect.y += 3
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 3

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= Constants.SCREEN_HEIGHT:
            self.speed_vector_y = -10

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.speed_vector_x = -2
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.speed_vector_x = 2
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.speed_vector_x = 0
        _isRunning = False

    def run_left(self):
        """ Called when the user hits the right arrow twice """
        self.speed_vector_x = -6
        self.direction = "L"
        _isRunning = True

    def run_right(self):
        """ Called when the user hits the right arrow twice """
        self.speed_vector_x = 6
        self.direction = "R"
        _isRunning = True