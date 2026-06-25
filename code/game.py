from code.level import Level
from const import WIN_WIDHT, WIN_HEIGHT, MENU_OPTION
import pygame
import pygame.mixer_music
from code.menu import Menu


# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0] # P1 and P2
                level = Level(self.window, "Level1", menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, "Level2", menu_return, player_score)
                    level_return = level.run(player_score)
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
