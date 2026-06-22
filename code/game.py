from const import WIN_WIDHT, WIN_HEIGHT
import pygame
import pygame.mixer_music
from code.menu import Menu
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()





