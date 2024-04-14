class Setting:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.row = 8
        self.col = 8
        self.boxsize = self.screen_width // self.col
        self.color = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255)
        }
        self.FPS = 100
        self.padding = 20
        self.outline = 5
