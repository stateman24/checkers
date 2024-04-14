from setting import Setting
class Player:
    def __init__(self, color, turn=False):
        self.color = color
        self.pieces = []
        self.num_of_pieces = len(self.pieces)
        self.setting = Setting()
        self.turn = turn

    def update_player_pieces(self, piece, row, col):
        for playerpiece in self.pieces:
            if playerpiece.row == piece.row and playerpiece.col == piece.col:
                playerpiece.row = row
                playerpiece.col = col

    def switch(self):
        if self.turn:
            self.turn = False
        else:
            self.turn = True

    def __str__(self):
        return f"Player {self.color} {self.turn}"
