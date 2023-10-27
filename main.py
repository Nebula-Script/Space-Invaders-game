### IMPORTAÇÕES ###

import pygame as pg
from PPlay.sprite import *

from variables import *
from menu_screen import *
from difficulty_screen import *
from game_screen import *
from ranking_screen import *


### TELA ###

tela.set_title("Space Invaders")
pg.init()



### LOOP ###

# O jogo acessa a função "menu_func" no arquivo menu_screen.py

while True:
    if keys.key_pressed('ESC'):
        pg.QUIT()

    menu_func()

    tela.update()