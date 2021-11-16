"""Alexsander Rosante's creation"""

import pygame
from pygame.locals import *
from settings import *
from grid import Grid

pygame.init()


class Game:
    def __init__(self):
        # display
        self.display = pygame.display.set_mode((display_w, display_h))
        pygame.display.set_caption('Game of life')

        # events
        self.events = pygame.event.get()
        self.APPLY_RULES = pygame.USEREVENT + 1

        # time
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.APPLY_RULES, 500)

        # grid
        self.grid = Grid(40, 40, 16)
        for i in range(10):
            for j in range(10):
                self.grid.cells[i][j].alive = True

        # setup
        self.gen = 0
        self.font = pygame.font.Font(None, 30)
        self.cells_alive = 0

        self.loop = True

    def check_cells(self):
        """Check grid, apply rules and return the number of cells alive"""
        cells_alive = 0
        for row, cells_row in enumerate(self.grid.cells):
            for col, cell in enumerate(cells_row):
                neighbs_alive, neighbs_dead = 0, 0

                # check neighbors
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

                cells_alive += int(cell.alive)

        return cells_alive

    def check_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == QUIT:
                self.loop = False
            elif event.type == self.APPLY_RULES:
                self.cells_alive = self.check_cells()
                self.gen += 1

    def draw_info(self):
        # gen
        self.display.blit(self.font.render(f'Gen: {self.gen}', True, 'white', 'black'), (10, 10))
        # cells alive
        text = self.font.render(f'Cells: {self.cells_alive}', True, 'white', 'black')
        rect = text.get_rect(bottomleft=(10, display_h - 10))
        self.display.blit(text, rect)

    def draw_grid(self, size, color='#1C1B22'):
        # vertical lines
        for i in range(round(display_w / size)):
            x = i * size
            pygame.draw.line(self.display, color, (x, 0), (x, display_h))
        # horizontal lines
        for i in range(round(display_h / size)):
            y = i * size
            pygame.draw.line(self.display, color, (0, y), (display_w, y))

    def run(self):
        while self.loop:
            self.check_events()

            #
            self.display.fill(bg_color)
            self.grid.updraw(self.display)
            self.draw_info()
            #

            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
