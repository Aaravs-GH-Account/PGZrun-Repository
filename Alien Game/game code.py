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
    clock.schedule_unique(ma,1)
def draw():
    screen.fill('white')
    a.draw()
    screen.draw.text(b,center=(250,75),fontsize=25,color='blue')
def ma():
    global b
    b='Oh No! You missed!'
    am()
def on_mouse_down(pos):
    global b,c
    if a.collidepoint(pos):
        b='Good Job! You hit the alien!'
        clock.unschedule(am)
        clock.unschedule(ma)
        am()
        clock.schedule_interval(am,c)
am()
clock.schedule(am,3)
#clock.schedule_interval(am,c)
p.go()
