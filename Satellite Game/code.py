import pgzrun as p, random as r, time as t
WIDTH=700
HEIGHT=500
TITLE='Satellite Game'
satel=[]
ligh=[]
eigh=8
satcou=0
st=0
sw=0
def satellite():
    global st
    for i in range(8):
        act=Actor('satellite.png')
        act.x=r.randint(50,600)
        act.y=r.randint(100,450)
        satel.append(act)
def draw():
    screen.blit('space bg.jpg',(0,0))
    satseq=1
    for i in satel:
        i.draw()
        screen.draw.text(str(satseq),(i.pos[0],i.pos[1]),color='white')
        satseq=satseq+1
satellite()
p.go()