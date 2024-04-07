import sys
import pygame
from setting import Setting
from board import Board
from player import Player


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
        self.player1 = Player(self.setting.color['red'], turn=True)
        self.player2 = Player(self.setting.color['green'])
        self.currentplayer = None

    def playermanger(self, player1, player2):
        player1 = self.player1
        player2 = self.player2
        if player1.turn:
            self.currentplayer = player1
            player1.switch()
            player2.switch()
        elif player2.turn:
            self.currentplayer = player2
            player2.switch()
            player1.switch()
        print(self.currentplayer)

    def run_game(self):
        while True:
            self.playermanger(player1=self.player1, player2=self.player2)
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.board.draw(screen=self.screen)
        self.clock.tick(self.setting.FPS)
        pygame.display.flip()

    def get_pos_from_mouse(self, pos):
        x, y = pos
        row = y // self.setting.boxsize
        col = x // self.setting.boxsize
        return row, col


if __name__ == '__main__':
    game = Checkers()
    game.run_game()
