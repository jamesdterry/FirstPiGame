#
# Main Game Scene
#

import pygame
import random

from screen import Screen
from sprite import Sprite
from scene import Scene

import over_scene

SPAWNBUG = pygame.USEREVENT + 1

MAX_BUGS = 5
GAME_LENGTH = 20

class play_scene(Scene):
    eraser_sprite = None
    bug_sprites = []
    down_pressed = False
    up_pressed = False
    left_pressed = False
    right_pressed = False
    start_time = 0
    font = None
    score = 0
    splat_sound = None
    secs = 0

    def spawn_bug(self):
        if len(self.bug_sprites) >= MAX_BUGS:
            return

        print "spawn bug"

        new_bug = Sprite("art/bug1.png")
        new_bug.x = random.randint(0, self.s.size[0] - new_bug.width())
        new_bug.y = random.randint(0, self.s.size[1] - new_bug.height())

        self.bug_sprites.append(new_bug)

    def test_erase_bug(self):
        for bug_sprite in self.bug_sprites:
            if bug_sprite.collide(self.eraser_sprite):
                self.bug_sprites.remove(bug_sprite)
                self.score = self.score + 1
                self.splat_sound.play()
                return

    def load(self):
        self.start_time = pygame.time.get_ticks()

        self.bug_sprites = []

        self.font = pygame.font.Font("art/joystix.otf", 22)

        e = self.eraser_sprite = Sprite("art/eraser.png")
        e.x = self.s.size[0] / 2.0
        e.y = self.s.size[1] / 2.0

        self.splat_sound = pygame.mixer.Sound("art/squish.wav")

        pygame.time.set_timer(SPAWNBUG, 1000)

    def cleanup(self):
        pygame.time.set_timer(SPAWNBUG, 0)

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
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.secs = GAME_LENGTH - int(elapsed_time/1000)
        if (self.secs == 0):
            os = over_scene.over_scene(self.game)
            os.score = self.score
            self.game.gotoScene(os)

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

        # Time Left
        secs_string = str(self.secs)
        if (len(secs_string) < 1):
            secs_string = "0" + secs_string
        time_label = self.font.render(secs_string, 1, (255,255,0))
        self.s.screen.blit(time_label, (4, 10))

        # Score
        score_label = self.font.render("Score: " + str(self.score), 1, (255,255,0))
        self.s.screen.blit(score_label, (self.s.size[0] - 180, 10))

        for bug_sprite in self.bug_sprites:
            bug_sprite.blit(self.s)

        self.eraser_sprite.blit(self.s)
