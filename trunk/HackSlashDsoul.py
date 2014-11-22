__author__ = 'Simon'

import pygame
import Constants
import datetime

from Entities.Dsoul import Dsoul
from Levels.Stage.Stage_01 import Stage_01

def main():
    """ Main Program """
    pygame.init()

    # Manage the screen
    size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("HackSlashDsoul")

    #create the main player
    main_player = Dsoul('Resources/Sprites/phommarath.png')

    # Create the level
    level_list = []
    level_list.append(Stage_01(main_player))

    # Set the level
    current_level_num = 0
    current_level = level_list[current_level_num]

    active_sprite_list = pygame.sprite.Group()
    main_player.level = current_level

    main_player.rect.x = 100
    main_player.rect.y = Constants.SCREEN_HEIGHT - main_player.rect.height
    active_sprite_list.add(main_player)

    last_input_key = None
    last_input_time = None

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    done = False
    while not done:
        for event in pygame.event.get():  # User did something

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if (last_input_key == pygame.K_LEFT and pygame.time.get_ticks()-last_input_time < 100) or main_player._isRunning == True:
                        main_player.run_left()
                    else:
                        main_player.go_left()
                    last_input_key = event.key

                if event.key == pygame.K_RIGHT:
                    if (last_input_key == pygame.K_RIGHT and pygame.time.get_ticks()-last_input_time < 100) or main_player._isRunning == True:
                        main_player.run_right()
                    else:
                        main_player.go_right()
                    last_input_key = event.key

                if event.key == pygame.K_a:
                    main_player.jump()
                    last_input_key = event.key

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and main_player.speed_vector_x < 0:
                    main_player.stop()
                if event.key == pygame.K_RIGHT and main_player.speed_vector_x > 0:
                    main_player.stop()

            last_input_time = pygame.time.get_ticks()

        active_sprite_list.update()

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
