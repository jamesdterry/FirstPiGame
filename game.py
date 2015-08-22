#
# Game
#

import pygame
import sys
import os
from screen import Screen
from sprite import Sprite

class Game:
    s = None
    cat_sprite = None

    def load(self):
        self.cat_sprite = Sprite("cat.png")

    def do_event(self, event):
        pass

    def update(self):
        self.cat_sprite.x = self.cat_sprite.x + 1
        self.cat_sprite.y = self.cat_sprite.y + 1

    def draw(self):
        self.s.screen.fill((255,0,0))
        self.cat_sprite.blit(self.s)

    def run(self):

        self.s = Screen()
        self.s.MakeScreen()

        self.load()

        clock = pygame.time.Clock()
        while 1:
            clock.tick(60)
            for event in pygame.event.get():
                print event
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        print clock.get_fps()
                        pygame.quit()
                        exit(0)
            self.update()
            self.draw()
            pygame.display.flip()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()