#
# Intro Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

class first_scene(Scene):
    raspberry_sprite = None

    def load(self):
        self.raspberry_sprite = Sprite("art/raspberry35.png")

    def cleanup(self):
        pass

    def do_event(self, event):
        pass

    def update(self):
        self.raspberry_sprite.x = 100
        self.raspberry_sprite.y = 100
        return

        max_x = self.s.size[0] - self.raspberry_sprite.width()
        x = random.randint(0, max_x)
        max_y = self.s.size[0] - self.raspberry_sprite.height()
        y = random.randint(0, max_y)

        self.raspberry_sprite.x = x
        self.raspberry_sprite.y = y


    def draw(self):
        self.s.screen.fill((0,0,0))

        self.raspberry_sprite.blit(self.s)