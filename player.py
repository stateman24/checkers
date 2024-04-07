from setting import Setting
class Player:
    def __init__(self, color, turn=False):
        self.color = color
        self.pieces = []
        self.num_of_pieces = len(self.pieces)
        self.setting = Setting()
        self.turn = turn
    def move(self, piece):
        pass

    def switch(self):
        if self.turn:
            self.turn = False
        else:
            self.turn = True

    def __str__(self):
        return f"Player {self.color} {self.turn}"
