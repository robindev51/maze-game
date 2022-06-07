import pygame
from pygame import *

from maze import Maze
from player import Player
from generator import generateMaze

import os

os.environ['SDL_VIDEO_CENTERED'] = '1'


class App:
    windowWidth = 600
    windowHeight = 800
    player = 0
    curLevel = 1
    totalLevels = 10
    firstCol = 50
    firstRow = 60

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None

    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.NOFRAME)

        self._gate_images = [
            pygame.image.load("resources/gate0.png").convert_alpha(),
            pygame.image.load("resources/gate1.png").convert_alpha(),
            pygame.image.load("resources/gate2.png").convert_alpha(),
            pygame.image.load("resources/gate3.png").convert_alpha(),
            pygame.image.load("resources/gate2.png").convert_alpha(),
            pygame.image.load("resources/gate1.png").convert_alpha()
        ]

        self._player_images = [
            pygame.image.load("resources/player0.png").convert_alpha(),
            pygame.image.load("resources/player1.png").convert_alpha(),
            pygame.image.load("resources/player2.png").convert_alpha(),
            pygame.image.load("resources/player3.png").convert_alpha(),
            pygame.image.load("resources/player2.png").convert_alpha(),
            pygame.image.load("resources/player1.png").convert_alpha()
        ]

        self._block_surf = pygame.image.load("resources/block.png").convert_alpha()
        self.load_levels()
        self.start_level(self.curLevel)

        pygame.display.set_caption('Maze Game')

        self._running = True

    def start_level(self, level):
        self.firstCol = self.levels[level - 1][0]
        self.firstRow = self.levels[level - 1][1]
        self.aspect = self.levels[level - 1][2]
        self.maze = Maze(self.firstRow, self.firstCol, self.aspect,
                         generateMaze(self.firstRow, self.firstCol), self._block_surf, self._gate_images)
        self.player = Player(self.aspect, self.maze.plX, self.maze.plY, self.maze.rows, self.maze.cols)
        self._display_surf = pygame.display.set_mode((self.firstCol * self.aspect, self.firstRow * self.aspect),
                                                     pygame.HWSURFACE)
        self._hud_top = self.firstCol * self.aspect

    def load_levels(self):
        self.levels = []
        with open('levels/levels.lvl', 'rb') as f:
            lines = [line.split() for line in f.readlines()]
        for l in lines:
            self.levels.append((int(l[0]), int(l[1]), int(l[2])))

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def game_over(self):
        self.player.restart()

    def player_collision(self):
        return self.maze.maze[self.player.y][self.player.x] == '1'

    def on_render(self):
        self.clock.tick(10)
        self._display_surf.fill((0, 0, 0))
        self.maze.draw(self._display_surf)
        self.player.draw(self._display_surf, self._player_images)

        pygame.display.flip()

        if self.player_collision():
            self.game_over()

        if self.finished():
            self.next_level()

    def next_level(self):
        self.curLevel = self.curLevel + 1
        self.start_level(self.curLevel)

    def finished(self):
        return self.maze.maze[self.player.y][self.player.x] == 'X'

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.moveRight()

            if keys[K_LEFT]:
                self.player.moveLeft()

            if keys[K_UP]:
                self.player.moveUp()

            if keys[K_DOWN]:
                self.player.moveDown()

            if keys[K_ESCAPE]:
                self._running = False

            if keys[K_n]:
                self.next_level()

            if keys[K_s]:
                pygame.image.save(self._display_surf, f"sslevel_{self.curLevel}.jpg")
                self.next_level()

            self.on_loop()
            self.on_render()
        self.on_cleanup()
