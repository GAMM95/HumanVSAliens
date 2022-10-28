# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:34:39 2022

@author: Acer
"""

import pygame
import sys
from configuraciones import Configuraciones
from nave import Nave
def inicia_juego():
    pygame.init() # habilitar el motor de pygame
    obj_Configuraciones = Configuraciones() # instancia de la clase configuraciones
    pantalla = pygame.display.set_mode((obj_Configuraciones.ancho_pantalla,obj_Configuraciones.alto_pantalla)) # atributos autoreferenciados a traves del objeto
    # una vez creada la pantalla, colocar otros atributos
    pygame.display.set_caption("Humans Vs Aliens")
    obj_nave = Nave(pantalla)
    while True:
        for event in pygame.event.get(): #
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pantalla.fill(obj_Configuraciones.color_fondo_pantalla)
        obj_nave.blitme()
        pygame.display.flip() #actualizar lo que sucede en pantalla
        #si usuario presiona teclas arriba, la nave sube
inicia_juego()