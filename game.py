#
# Game
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

from intro_scene import intro_scene

class Game:
    s = None
    current_scene = None
    clock = None

    def __init__(self):
        self.s = Screen()
        self.s.MakeScreen()

    def load(self):
        pygame.mixer.music.load("art/FarmFreshFiddlen.ogg")
        pygame.mixer.music.play(-1, 0.0)

    def update(self):
        pass

    def do_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                print self.clock.get_fps()
                pygame.quit()
                exit(0)

    def gotoScene(self, scene):
        if self.current_scene is not None:
            self.current_scene.cleanup()
        self.current_scene = scene
        self.current_scene.load()

    def run(self):

        self.load()

        self.clock = pygame.time.Clock()
        while 1:
            self.clock.tick(60)
            for event in pygame.event.get():
                self.do_event(event)
                self.current_scene.do_event(event)
            self.update()
            self.current_scene.update()
            self.current_scene.draw()
            pygame.display.flip()

def main():
    game = Game()
    game.gotoScene(intro_scene(game))
    game.run()

if __name__ == "__main__":
    main()