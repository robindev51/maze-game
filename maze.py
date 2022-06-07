import pygame.transform


class Maze:
    def __init__(self, levelFile, aspect, block_surf, gate_images):
        file = open(levelFile, "r")
        rowsCols = list(map(int, file.readline().split()))
        self.rows = rowsCols[1]
        self.cols = rowsCols[0]
        self.maze = list()
        self.aspect = aspect
        self.block_surf = pygame.transform.scale(block_surf, (self.aspect, self.aspect))
        self.gate_frame = 0
        self.gate_images = []
        for image in gate_images:
            self.gate_images.append(pygame.transform.scale(image, (self.aspect, self.aspect)))

        for i in range(0, self.rows):
            row = file.readline().split()
            self.maze.append(row)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.maze[i][j] == 'S':
                    self.plX = i
                    self.plY = j

    def __init__(self, rows, cols, aspect, maze, block_surf, gate_images):
        self.rows = rows
        self.cols = cols
        self.maze = list()
        self.aspect = aspect
        self.block_surf = pygame.transform.scale(block_surf, (self.aspect, self.aspect))
        self.gate_frame = 0
        self.gate_images = []
        for image in gate_images:
            self.gate_images.append(pygame.transform.scale(image, (self.aspect, self.aspect)))
        self.maze = maze

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.maze[i][j] == 'S':
                    self.plY = i
                    self.plX = j

    def draw(self, display_surf):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.maze[i][j] == '1':
                    display_surf.blit(self.block_surf, (j * self.aspect, i * self.aspect))
                if self.maze[i][j] == 'X':
                    display_surf.blit(self.gate_images[self.gate_frame], (j * self.aspect, i * self.aspect))
                    self.gate_frame = (self.gate_frame + 1) % len(self.gate_images)
