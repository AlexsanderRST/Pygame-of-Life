"""Alexsander Rosante's creation"""

import pygame
from settings import bg_color


class Cell(pygame.sprite.Sprite):
    def __init__(self, size, pos, color='#1C1B22'):
        super().__init__()
        self.color = color
        self.pos = pos
        self.image = pygame.Surface(2 * [size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(self.pos[0] * size, self.pos[1] * size))
        self.alive = False

    def __repr__(self):
        return f'Cell{self.pos}'

    def update(self):
        if self.alive:
            self.image.fill(self.color)
        else:
            self.image.fill(bg_color)
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, *self.rect.size), 1)
