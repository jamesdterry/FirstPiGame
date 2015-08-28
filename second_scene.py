#
# Intro Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

class second_scene(Scene):
    raspberry_sprite = None
    left_pressed = False
    right_pressed = False

    def load(self):
        self.raspberry_sprite = Sprite("art/raspberry35.png")
        self.raspberry_sprite.x = (self.s.size[0] - self.raspberry_sprite.width()) / 2.0
        self.raspberry_sprite.y = (self.s.size[1] - self.raspberry_sprite.height()) / 2.0

    def cleanup(self):
        pass

    def do_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = False

    def update(self):
        if self.left_pressed:
            self.raspberry_sprite.x = self.raspberry_sprite.x - 1
        if self.right_pressed:
            self.raspberry_sprite.x = self.raspberry_sprite.x + 1


    def draw(self):
        self.s.screen.fill((0,0,0))

        self.raspberry_sprite.blit(self.s)