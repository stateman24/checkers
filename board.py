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
        self.green_player = Player(self.setting.color['green'])
        self.red_player = Player(self.setting.color['red'])
        self.create_board()

    def draw_cube(self, screen):
        screen.fill(self.setting.color['white'])
        for row in range(self.setting.row):
            for col in range(row % 2, self.setting.col, 2):
                pygame.draw.rect(screen, self.setting.color['black'], (row*self.setting.box_size,
                                                                       col*self.setting.box_size,
                                                                       self.setting.box_size,
                                                                       self.setting.box_size))

    def create_board(self):
        for row in range(self.setting.row):
            self.board.append([])
            for col in range(self.setting.col):
                if (col % 2) == ((row + 1) % 2):
                    if row < 3:
                        piece = Piece(row, col, self.red_player.color)
                        self.red_player.pieces.append(piece)
                        self.board[row].append(piece)
                    elif row > 4:
                        piece = Piece(row, col, self.green_player.color)
                        self.green_player.pieces.append(piece)
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
        if piece.color == self.green_player.color:
            self.check_move_to_make_king(piece, row)
            self.green_player.update_player_pieces(piece, row, col)
        else:
            self.check_move_to_make_king(piece, row)
            self.red_player.update_player_pieces(piece, row, col)

    def check_move_to_make_king(self, piece, row):
        if piece.color == self.green_player.color:
            if piece.row == 0:
                piece.make_king()
        else:
            if piece.row == self.setting.row - 1:
                piece.make_king()

    def remove_piece(self, pieces):
        for piece in pieces:
            if piece.color == self.green_player.color:
                self.board[piece.row][piece.col] = 0
                self.green_player.pieces.remove(piece)
            else:
                self.board[piece.row][piece.col] = 0
                self.red_player.pieces.remove(piece)

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.king:
            moves.update(self._traverse_left_king(row - 1, 0, -1, piece.color, left))
            moves.update(self._traverse_right_king(row - 1, 0, -1, piece.color, right))
            moves.update(self._traverse_left_king(row + 1, self.setting.row, 1, piece.color, left))
            moves.update(self._traverse_right_king(row + 1, self.setting.row, 1, piece.color, right))
        if piece.color == self.green_player.color:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        elif piece.color == self.red_player.color:
            moves.update(self._traverse_left(row + 1, min(row + 3, self.setting.row), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, self.setting.row), 1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.setting.row)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= self.setting.col:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.setting.row)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def _traverse_left_king(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.setting.row)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right_king(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        piece_hit = 0
        for r in range(start, stop, step):
            if piece_hit >= 2:
                break
            elif right >= self.setting.col:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.setting.row)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
            elif current.color == color:
                break
            else:
                last = [current]
                piece_hit += 1
            right += 1
        return moves