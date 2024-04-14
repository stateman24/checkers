import pygame
from board import Board
from player import Player
from setting import Setting


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.selected = None
        self.board = Board()
        self.setting = Setting()
        self.player1 = Player(self.setting.color["red"])
        self.player2 = Player(self.setting.color["green"])
        self.turn = self.player1
        self.valid_moves = {}


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
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_player_turn()
        else:
            return False
        return True

    def change_player_turn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        elif self == self.player2:
            self.turn = self.player1
