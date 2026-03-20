import pgzrun as p, random as r
WIDTH=500
HEIGHT=500
TITLE='Alien Game'
a=Actor('alien.png')
b='Welcome to the Alien Game!'
c=1
def am():
    a.x=r.randint(125,375)
    a.y=r.randint(150,375)
def draw():
    screen.fill('white')
    a.draw()
    screen.draw.text(b,center=(250,75),fontsize=25,color='blue')
def on_mouse_down(pos):
    global b,c
    if a.collidepoint(pos):
        b='Good Job! You hit the alien!'
        am()
        c=1
am()
clock.schedule_interval(am,c)
p.go()