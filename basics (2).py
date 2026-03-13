import pgzrun,random
WIDTH=500
HEIGHT=500
TITLE='Pygame Zero: Patterns'
def draw():
    w=500
    h=250
    for i in range(50):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        a=Rect((250,250),(w,h))
        a.center=250,250
        screen.draw.rect(a,(r,g,b))
        w=w-5
        h=h+5
        r=r-8
        g=g+8
def update():
    pass
pgzrun.go()