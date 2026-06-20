print("EXECUTANDO menu")
#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self, window):
        print("CARREGANDO IMAGEM")
        self.window = window
        self.surf = pygame.image.load("assets/MenuBg.png")
        print("IMAGEM CARREGADA")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()
        pass
