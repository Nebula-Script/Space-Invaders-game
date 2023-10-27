from PPlay.sprite import *
from variables import *
import pygame as pg
from PPlay.sound import *

player = Sprite("art/Player.png")
shot = Sprite("art/Shot.png")
shoot_sfx = Sound("audio/laserShoot.ogg")

def game_func():
    player.set_position(WIDTH/2,HEIGHT-40)
    shot.set_position(-64,-64)

    while True:
        clock.tick(60)    
        if keys.key_pressed('B'):
            break


        # MOVIMENTAÇÃO #

        if keys.key_pressed('LEFT'):
            player.x -= 6
        elif keys.key_pressed('RIGHT'):
            player.x += 6
        
        if player.x > WIDTH - 68:
            player.x = WIDTH - 68
        elif player.x < 4:
            player.x = 4


        ### TIRO ###

        # Baseado na forma que o tiro está programado, sempre que ele sair da tela, o jogador
        # poderá atirar novamente



        if keys.key_pressed('SPACE') and shot.y < -16:
            shot.set_position(player.x+24,player.y-8)
            shoot_sfx.play()
        shot.y -= 12

        tela.set_background_color(0)
        player.draw()
        shot.draw()
        tela.update()