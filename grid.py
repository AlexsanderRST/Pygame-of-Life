"""Alexsander Rosante"""

import pygame
from cell import Cell


class Grid:
    def __init__(self, rows, cols, size, color='#1C1B22'):
        self.cells = []
        self.cells_group = pygame.sprite.Group()
        self.set_grid(rows, cols, size, color)

    def set_grid(self, rows, cols, size, color):
        for row in range(rows):
            line = []
            for col in range(cols):
                cell = Cell(size, (row, col), color)
                self.cells_group.add(cell)
                line.append(cell)
            self.cells.append(line)

    def updraw(self, surface):
        self.cells_group.update()
        self.cells_group.draw(surface)
