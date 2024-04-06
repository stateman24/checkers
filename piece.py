import pygame
from setting import Setting
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.setting = Setting()
        self.direction = 0
        if self.color == "green":
            self.direction -= 1
        else:
            self.direction += 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.setting.boxsize * self.col + self.setting.boxsize // 2
        self.y = self.setting.boxsize * self.row + self.setting.boxsize // 2

    def draw(self, screen):
        radius = self.setting.boxsize // 2 - self.setting.padding
        pygame.draw.circle(screen, self.color, center=(self.x, self.y), radius=radius)

