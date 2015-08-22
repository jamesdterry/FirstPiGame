#
# Game
#

import pygame

import sys
import os
import random

from screen import Screen
from sprite import Sprite

SPAWNBUG = pygame.USEREVENT + 1

class Game:
    s = None
    eraser_sprite = None
    bug_sprites = []
    down_pressed = False
    up_pressed = False
    left_pressed = False
    right_pressed = False

    def spawn_bug(self):
        if len(self.bug_sprites) >= 3:
            return

        new_bug = Sprite("art/bug1.png")
        new_bug.x = random.randint(0, self.s.size[0] - new_bug.width())
        new_bug.y = random.randint(0, self.s.size[1] - new_bug.height())

        self.bug_sprites.append(new_bug)

    def test_erase_bug(self):
        for bug_sprite in self.bug_sprites:
            if bug_sprite.collide(self.eraser_sprite):
                self.bug_sprites.remove(bug_sprite)
                return

    def load(self):
        e = self.eraser_sprite = Sprite("art/eraser.png")
        e.x = self.s.size[0] / 2.0
        e.y = self.s.size[1] / 2.0

        pygame.time.set_timer(SPAWNBUG, 1000)

    def do_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.down_pressed = True
            elif event.key == pygame.K_UP:
                self.up_pressed = True
            elif event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = True
            elif event.key == pygame.K_SPACE:
                self.test_erase_bug()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.down_pressed = False
            elif event.key == pygame.K_UP:
                self.up_pressed = False
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = False
        elif event.type == SPAWNBUG:
            self.spawn_bug()

    def update(self):
        if self.down_pressed:
            self.eraser_sprite.y = self.eraser_sprite.y + 1
        if self.up_pressed:
            self.eraser_sprite.y = self.eraser_sprite.y - 1
        if self.left_pressed:
            self.eraser_sprite.x = self.eraser_sprite.x - 1
        if self.right_pressed:
            self.eraser_sprite.x = self.eraser_sprite.x + 1

    def draw(self):
        self.s.screen.fill((0,0,0))

        for bug_sprite in self.bug_sprites:
            bug_sprite.blit(self.s)

        self.eraser_sprite.blit(self.s)

    def run(self):

        self.s = Screen()
        self.s.MakeScreen()

        self.load()

        clock = pygame.time.Clock()
        while 1:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        print clock.get_fps()
                        pygame.quit()
                        exit(0)
                self.do_event(event)
            self.update()
            self.draw()
            pygame.display.flip()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()