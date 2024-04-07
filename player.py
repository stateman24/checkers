import pygame
from board import Board
from setting import Setting

class Player:
    def __init__(self, color, turn=False):
        self.color = color
        self.num_of_pieces = None
        self.board = Board()
        self.setting = Setting()
        self.turn = turn
    def get_pieces(self, color):
        if color == self.setting.color['green']:
            self.num_of_pieces = self.board.green_piece
        else:
            self.num_of_pieces = self.board.red_piece

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        try:
            if piece.color == self.color:
                piece.selected = True
                return piece
        except AttributeError:
            return None

    def switch(self):
        if self.turn:
            self.turn = False
        else:
            self.turn = True

    def __str__(self):
        return f"Player {self.color} {self.turn}"
