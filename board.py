import pygame
from setting import Setting
from player import Player
from piece import Piece


class Board:
    def __init__(self):
        self.setting = Setting()
        self.board = []
        self.green_piece = 12
        self.red_piece = 12
        self.player1 = Player(self.setting.color['green'])
        self.player2 = Player(self.setting.color['red'])
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
                        piece = Piece(row, col, self.player1.color)
                        self.player1.pieces.append(piece)
                        self.board[row].append(piece)
                    elif row > 4:
                        piece = Piece(row, col, self.player2.color)
                        self.player2.pieces.append(piece)
                        self.board[row].append(piece)
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, screen):
        self.draw_cube(screen)
        for row in range(self.setting.row):
            for col in range(self.setting.col):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[row][col], self.board[piece.row][piece.col] = self.board[piece.row][piece.col], self.board[row][col]
        piece.move(row, col)
        if piece.color == self.player1.color:
            self.player1.update_player_pieces(piece, row, col)
        else:
            self.player2.update_player_pieces(piece, row, col)

    def update_board(self):
        pass

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == self.player1.color:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        elif piece.color == self.player2.color:
            moves.update(self._traverse_left(row + 1, min(row + 3, self.setting.row), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, self.setting.row), 1, piece.color, right))

    def _traverse_left(self, start, stop, step, color, left, skipped=None):
        moves = {}
        last = []
        if skipped is None:
            skipped = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[r, left] = last + skipped
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, self.setting.row)
                    moves.update(self._traverse_left(r+step, row, step, current.color, left-1, skipped=last))
                    moves.update(self._traverse_right(r-step, row, step, current.color, left-1, skipped=last))
                    break
                else:
                    moves[(r, left)] = last
            if current.color == color:
                break
            else:
                last = [current]
        left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=None):
        moves = {}
        last = []
        if skipped is None:
            skipped = []
        for r in range(start, stop, step):
            if right >= self.setting.col:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[r, right] = last + skipped
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.setting.row)
                    moves.update(self._traverse_left(r + step, row, step, current.color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r - step, row, step, current.color, right - 1, skipped=last))
                    break
                else:
                    moves[(r, right)] = last
            if current.color == color:
                break
            else:
                last = [current]
        right += 1
        return moves
