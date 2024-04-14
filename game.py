import pygame
from board import Board
from piece import Piece
from player import Player
from setting import Setting


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.selected = None
        self.board = Board()
        self.turn = self.player1
        self.valid_moves = {}
        self.setting = Setting()
        self.player1 = Player(self.setting.color["red"])
        self.player2 = Player(self.setting.color["green"])

    def update(self):
        self.board.draw(self.screen)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = None
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select_piece(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select_piece(row, col)
        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn.color:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves()
            return True

        return False


    def _move(self, row, col):
        pass
