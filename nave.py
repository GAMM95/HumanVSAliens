# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:36:46 2022

@author: Acer
"""

import pygame
class Nave():
    def __init__(self, pantalla):
        ## atributos
        self.pantalla = pantalla
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = self.pantalla.get_rect()
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
    def blitme(self):
        self.pantalla.blit(self.imagen,self.rect) # posicionar la pantalla al medio