__author__ = 'Simon'

import pygame

import Constants

class Level():
    """ Class to create Level """
    platform_list = None

    """
    TBD
    enemy_list = None
    """
    background = None
    #world_shift = 0
    #level_limit = -1000

    def __init__(self, player):
        """ Constructor """
        self.platform_list = pygame.sprite.Group()
        # self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        """ Update everything in this level """
        self.platform_list.update()
        # self.enemy_list.update()

    def draw(self, screen):

        # Draw background
        screen.fill(Constants.BLACK)
        screen.blit(self.background, (0, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        # self.enemy_list.draw(screen)

    """
    def shift_world(self, shift_x):
        # When the user moves left/right and we need to scroll everything:

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    """