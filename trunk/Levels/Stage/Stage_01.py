__author__ = 'Simon'
from Levels.Levels import Level
import pygame
import Constants
import Platforms


# Create platforms for the level
class Stage_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Resources/Backgrounds/black.png").convert()
        self.background.set_colorkey(Constants.WHITE)
        #self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [
            [Platforms.STONE_PLATFORM_LEFT, 300, 450],
            [Platforms.STONE_PLATFORM_MIDDLE, 370, 450],
            [Platforms.STONE_PLATFORM_RIGHT, 440, 450],
            [Platforms.STONE_PLATFORM_LEFT, 520, 330],
            [Platforms.STONE_PLATFORM_MIDDLE, 590, 330],
            [Platforms.STONE_PLATFORM_RIGHT, 660, 330],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = Platforms.MovingPlatform(Platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)