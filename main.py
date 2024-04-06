import sys
import pygame
from setting import Setting
from board import Board
class Checkers:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.icon = pygame.image.load('assets/icon.png')
        pygame.display.set_caption('Checkers')
        pygame.display.set_icon(self.icon)
        self.bg_color = self.setting.color['white']
        self.clock = pygame.time.Clock()
        self.board = Board()

    def run_game(self):
        while True:
            self.clock.tick(self.setting.FPS)
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.board.draw_cube(screen=self.screen)
        self.board.draw_piece(screen=self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Checkers()
    game.run_game()