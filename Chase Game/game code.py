import random as r, pgzrun as p
WIDTH=750
HEIGHT=420
TITLE='Slime Chase Game'
slime=Actor('slime.png')
slime.pos=(250,250)
food=Actor('food.png')
food.pos=(r.randint(0,600),())
def draw():
    screen.blit('grass.jpg',(0,0))
    slime.draw()
    food.draw()
p.go()