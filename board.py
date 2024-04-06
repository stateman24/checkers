import pygame
from setting import Setting
from piece import Piece
class Board:
    def __init__(self):
        self.setting = Setting()
        self.board = []


        self.create_board()

    def draw_cube(self, screen):
        screen.fill(self.setting.color['white'])
        for row in range(self.setting.row):
            for col in range(row % 2, self.setting.col, 2):
                pygame.draw.rect(screen, self.setting.color['black'], (row*self.setting.boxsize,
                                                                       col*self.setting.boxsize,
                                                                       self.setting.boxsize,
                                                                       self.setting.boxsize))

    def create_board(self):
        for row in range(self.setting.row):
            self.board.append([])
            for col in range(self.setting.col):
                if (col % 2) == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, self.setting.color['red']))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, self.setting.color['green']))
                    else:
                        self.board[row].append(0)
        print(self.board)

    def draw_piece(self, screen):
        for row in range(self.setting.row):
            for col in range(self.setting.col//2):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)
