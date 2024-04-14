import sys
import pygame
from setting import Setting
from game import Game


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
        self.game = Game(self.screen)

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = self.get_pos_from_mouse(pos)
                self.game.select_piece(row, col)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.game.update()
        self.clock.tick(self.setting.FPS)
        pygame.display.flip()

    def get_pos_from_mouse(self, pos):
        x, y = pos
        row = y // self.setting.box_size
        col = x // self.setting.box_size
        return row, col


if __name__ == '__main__':
    game = Checkers()
    game.run_game()
