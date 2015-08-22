#
# Game Over Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

import intro_scene

ALLOW_EXIT = pygame.USEREVENT + 2

class over_scene(Scene):
    font = None
    score = 0
    allow_exit = False

    def load(self):
        self.font = pygame.font.Font("art/joystix.otf", 66)
        pygame.time.set_timer(ALLOW_EXIT, 1000 * 5)

    def do_event(self, event):
        if event.type == pygame.KEYUP:
            if self.allow_exit:
                self.game.gotoScene(intro_scene.intro_scene(self.game))
        elif event.type == ALLOW_EXIT:
            self.allow_exit = True
            pygame.time.set_timer(ALLOW_EXIT, 0)

    def cleanup(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.s.screen.fill((0,0,0))

        msg_label = self.font.render("Game Over!", 1, (255,255,0))
        self.s.screen.blit(msg_label, ((self.s.size[0] - msg_label.get_width())/2.0, ((self.s.size[1] - msg_label.get_height())/2.0) - 40))

        score_label = self.font.render("Score: " + str(self.score), 1, (255,255,0))
        self.s.screen.blit(score_label, ((self.s.size[0] - score_label.get_width())/2.0, ((self.s.size[1] - score_label.get_height())/2.0) + 40))