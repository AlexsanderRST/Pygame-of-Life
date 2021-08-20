"""Alexsander Rosante's creation"""

import random
import pygame
from pygame.locals import *
from settings import *
from grid import Grid

pygame.init()


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((display_w, display_h))
        pygame.display.set_caption('Game of life')
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.loop = True

        #
        self.APPLY_RULES = pygame.USEREVENT + 1
        pygame.time.set_timer(self.APPLY_RULES, 500)

        self.grid = Grid(40, 40, 16)

        for i in range(10):
            for j in range(10):
                self.grid.cells[i][j].alive = True

        self.gen = 0
        self.font = pygame.font.Font(None, 20)
        #

    def run(self):
        #

        #

        while self.loop:
            self.event_check()

            #
            self.display.fill(bg_color)
            self.grid.updraw(self.display)
            self.draw_gen()
            #

            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()

    def event_check(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == QUIT:
                self.loop = False

            #
            elif event.type == self.APPLY_RULES:
                self.check_cells()
                self.gen += 1
            #

    def draw_grid(self, size, color='#1C1B22'):
        # vertical lines
        for i in range(round(display_w / size)):
            x = i * size
            pygame.draw.line(self.display, color, (x, 0), (x, display_h))
        # horizontal lines
        for i in range(round(display_h / size)):
            y = i * size
            pygame.draw.line(self.display, color, (0, y), (display_w, y))

    def draw_gen(self):
        self.display.blit(
            self.font.render(f'Gen: {self.gen}', True, Color('white')),
            (10, 10)
        )

    def check_cells(self):
        for row, cells_row in enumerate(self.grid.cells):
            for col, cell in enumerate(cells_row):
                neighbs_alive, neighbs_dead = 0, 0

                if 0 < cell.pos[0] < len(self.grid.cells) - 1:
                    if 0 < cell.pos[1] < len(cells_row) - 1:
                        # top
                        status = self.grid.cells[row - 1][col].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # bottom
                        status = self.grid.cells[row + 1][col].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # left
                        status = self.grid.cells[row][col - 1].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # right
                        status = self.grid.cells[row][col + 1].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # topleft
                        status = self.grid.cells[row - 1][col - 1].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # topright
                        status = self.grid.cells[row - 1][col + 1].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # bottomleft
                        status = self.grid.cells[row + 1][col - 1].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)
                        # bottomright
                        status = self.grid.cells[row + 1][col + 1].alive
                        neighbs_alive += int(status)
                        neighbs_dead += int(not status)

                # rule 1
                if cell.alive and neighbs_alive < 2:
                    cell.alive = False
                # rule 2
                if cell.alive and 2 <= neighbs_alive <= 3:
                    cell.alive = True
                # rule 3
                if cell.alive and neighbs_alive > 3:
                    cell.alive = False
                # rule 4
                if not cell.alive and neighbs_alive == 3:
                    cell.alive = True


if __name__ == '__main__':
    game = Game()
    game.run()
