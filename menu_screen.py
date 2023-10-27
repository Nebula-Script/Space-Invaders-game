from variables import *
from PPlay.sprite import *
import variables as var
import pygame as pg
import game_screen
import difficulty_screen


### BOTÕES ###
# Abaixo estão carregadas as imagens e suas posições.
#as variáveis wGame, wDiff, etc. guardam suas posições horizontais



botaoJogar = Sprite('art/botJogar.png')
barraJogar = Sprite('art/barraJogar.png')
wGame = (var.WIDTH/2)-(botaoJogar.width/2)
botaoJogar.set_position(wGame,80)
barraJogar.set_position(wGame,80)


botaoDificuldade = Sprite('art/botDificuldade.png')
barraDificuldade = Sprite('art/barraDificuldade.png')
wDiff = (var.WIDTH/2)-(botaoDificuldade.width/2)
botaoDificuldade.set_position(wDiff,240)
barraDificuldade.set_position(wDiff,240)


botaoRanking = Sprite('art/botRanking.png')
barraRanking = Sprite('art/barraRanking.png')
wRank = (var.WIDTH/2)-(botaoRanking.width/2)
botaoRanking.set_position(wRank,400)
barraRanking.set_position(wRank,400)


botaoSair = Sprite('art/botSair.png')
barraSair = Sprite('art/barraSair.png')
wSair = (var.WIDTH/2)-(botaoSair.width/2)
botaoSair.set_position(wSair,560)
barraSair.set_position(wSair,560)



# Abaixo, dependendo de onde o jogador clicar, uma função diferente será executada. Cada função
# está em seu próprio arquivo, como o game_func() no arquivo game_screen.py, que executa o jogo

# pg.mouse.get_pressed() retorna o estado de todos os botões do mouse. O [0] é para retornar
# especificamente o primeiro estado, do botão esquerdo do mouse. [1] e [2] seriam os outros
# botões, que nesse jogo não importarão.



def menu_func():
    tela.set_background_color(0)
    botaoJogar.draw()
    botaoDificuldade.draw()
    botaoRanking.draw()
    botaoSair.draw()


    if mouse.is_over_object(botaoJogar):
        barraJogar.draw()
        if pg.mouse.get_pressed()[0]:
            game_screen.game_func()


    elif mouse.is_over_object(botaoDificuldade):
        barraDificuldade.draw()
        if pg.mouse.get_pressed()[0]:
            difficulty_screen.diff_func()


    elif mouse.is_over_object(botaoRanking):
        barraRanking.draw()
        if pg.mouse.get_pressed()[0]:
            var.em_menu = False
            var.em_rank = True


    elif mouse.is_over_object(botaoSair):
        barraSair.draw()
        if pg.mouse.get_pressed()[0]:
            pg.QUIT()