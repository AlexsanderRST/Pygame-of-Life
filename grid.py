"""Alexsander Rosante's creation"""

import pygame
from cell import Cell


class Grid:
    def __init__(self, rows, cols, size):
        self.cells = []
        self.cells_group = pygame.sprite.Group()
        self.set_grid(rows, cols, size)

    def set_grid(self, rows, cols, size):
        for row in range(rows):
            line = []
            for col in range(cols):
                cell = Cell(size, (row, col))
                self.cells_group.add(cell)
                line.append(cell)
            self.cells.append(line)

    def updraw(self, surface):
        self.cells_group.update()
        self.cells_group.draw(surface)
