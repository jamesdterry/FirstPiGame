#
# Screen
#

import pygame
import sys
import os

class Screen:

    screen = None
    size = None

    def __init__(self):
        pass

    def MakeScreen(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
                # Make sure that SDL_VIDEODRIVER is set
                if not os.getenv('SDL_VIDEODRIVER'):
                        os.putenv('SDL_VIDEODRIVER', driver)
                        try:
                                pygame.display.init()
                        except pygame.error:
                                print 'Driver: {0} failed.'.format(driver)
                                continue
                        found = True
                        break

        if not found:
            raise Exception('No suitable video driver found!')

        infoObject = pygame.display.Info()

        self.size = (infoObject.current_w, infoObject.current_h)
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
