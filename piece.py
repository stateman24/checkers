import pygame
from setting import Setting

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.setting = Setting()
        self.x = 0
        self.y = 0
        self.king = False
        self.crown = self.setting.crown
        self.calc_pos()

    def calc_pos(self):
        self.x = self.setting.box_size * self.col + self.setting.box_size // 2
        self.y = self.setting.box_size * self.row + self.setting.box_size // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, screen):
        radius = self.setting.box_size // 2 - self.setting.padding
        pygame.draw.circle(screen, self.color, center=(self.x, self.y), radius=radius)
        if self.king:
            screen.blit(self.crown, (self.x - self.crown.get_width()//2, self.y - self.crown.get_height()//2))

    def make_king(self):
        self.king = True

    def __repr__(self):
        return f"Piece({self.color}, {self.row}, {self.col})"
