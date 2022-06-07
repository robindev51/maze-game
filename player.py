import pygame

class Player:

    def __init__(self, _aspect_, _x_, _y_, rows, cols):
        self._startX_ = _x_
        self._startY_ = _y_
        self.x = _x_
        self.y = _y_
        self.speed = _aspect_
        self.rows = rows
        self.cols = cols
        self.frame = 0

    def moveRight(self):
        if self.x < self.cols - 1:
            self.x = self.x + 1

    def moveLeft(self):
        if self.x > 1:
            self.x = self.x - 1

    def moveUp(self):
        if self.y > 1:
            self.y = self.y - 1

    def moveDown(self):
        if self.y < self.rows - 1:
            self.y = self.y + 1

    def restart(self):
        self.x = self._startX_
        self.y = self._startY_

    def draw(self, _surface_, _player_images):
        _player_surface = pygame.transform.scale(_player_images[self.frame], (self.speed, self.speed))
        _surface_.blit(_player_surface, (self.x * self.speed, self.y * self.speed))
        self.frame = (self.frame + 1) % len(_player_images)

