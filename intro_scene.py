#
# Intro Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

import play_scene

class intro_scene(Scene):
    font = None

    def load(self):
        self.font = pygame.font.Font("art/joystix.otf", 66)

    def cleanup(self):
        pass

    def do_event(self, event):
        if event.type == pygame.KEYUP:
            self.game.gotoScene(play_scene.play_scene(self.game))

    def update(self):
        pass

    def draw(self):
        self.s.screen.fill((0,0,0))

        msg_label = self.font.render("Press any key to play!", 1, (255,255,0))
        self.s.screen.blit(msg_label, ((self.s.size[0] - msg_label.get_width())/2.0, (self.s.size[1] - msg_label.get_height())/2.0))