from setting import Setting
class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.king_pieces = 0
        self.num_of_pieces = len(self.pieces)
        self.setting = Setting()

    def update_player_pieces(self, piece, row, col):
        for player_piece in self.pieces:
            if player_piece.row == piece.row and player_piece.col == piece.col:
                player_piece.row = row
                player_piece.col = col
        for king_piece in self.pieces:
            if king_piece.king:
                self.king_pieces += 1

    def __str__(self):
        return f"Player {self.color}"
