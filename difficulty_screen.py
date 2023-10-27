from PPlay.sprite import *
from variables import *
import pygame as pg


diff = Sprite("art/Dificuldade.png")
diff.set_position((WIDTH/2) - (diff.width/2), HEIGHT/3)

diff_1 = Sprite("art/1.png")
diff_2 = Sprite("art/2.png")
diff_3 = Sprite("art/3.png")
barraNum1 = Sprite("art/barraNum.png")
barraNum2 = Sprite("art/barraNum.png")
barraNum3 = Sprite("art/barraNum.png")

diff_1.set_position(WIDTH/2 - 320,HEIGHT/2)
diff_2.set_position(WIDTH/2 - 64,HEIGHT/2)
diff_3.set_position(WIDTH/2 + 192,HEIGHT/2)

barraNum1.set_position(WIDTH/2 - 320,HEIGHT/2)
barraNum2.set_position(WIDTH/2 - 64,HEIGHT/2)
barraNum3.set_position(WIDTH/2 + 192,HEIGHT/2)


# No momento, tudo que a tela de dificuldade faz é desenhar as imagens. Não ocorre
# mudanças de dificuldade ainda.


def diff_func():
    while True:

        if keys.key_pressed('B'):
            break
        
        tela.set_background_color(0)

        diff.draw()

        diff_1.draw()
        diff_2.draw()
        diff_3.draw()

        barraNum1.draw()
        barraNum2.draw()
        barraNum3.draw()

        tela.update()