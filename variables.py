from PPlay.mouse import *
from PPlay.window import *
import pygame as pg

### CONSTANTES ###
WIDTH = 1200
HEIGHT = 720

### VARIÁVEIS ###
dificuldade = 1
mouse = Mouse()
clock = pg.time.Clock()
tela = Window(WIDTH,HEIGHT)
keys = tela.get_keyboard()
