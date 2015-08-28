#
# Out first anything!
#

import pygame

from screen import Screen
from sprite import Sprite

s = None

#
# Your code here!
#
def mycode():
    global s
    raspberry_sprite = Sprite("art/raspberry35.png")
    raspberry_sprite.x = 100
    raspberry_sprite.y = 100
    raspberry_sprite.blit(s)

#
# Don't worry about this stuff for now...
#

def main():
    global s
    s = Screen()
    s.MakeScreen()
    s.screen.fill((0,0,0))
    mycode()
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    pygame.quit()
                    exit(0)

if __name__ == "__main__":
    main()
