import pygame
from board import Board
from setting import Setting


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.selected = None
        self.board = Board()
        self.setting = Setting()
        self.player1 = self.board.green_player
        self.player2 = self.board.red_player
        self.turn = self.player1
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.screen)
        self.draw_valid_moves(self.valid_moves)
        self.winner()
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
        else:
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
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove_piece(skipped)
            self.change_player_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen,
                               self.setting.color['blue'],
                               (col * self.setting.boxsize + self.setting.boxsize//2, row * self.setting.boxsize + self.setting.boxsize//2),
                               15)

    def change_player_turn(self):
        self.valid_moves = {}
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def winner(self):
        if len(self.player1.pieces) == 0:
            self.reset()
        elif len(self.player2.pieces) == 0:
            self.reset()
