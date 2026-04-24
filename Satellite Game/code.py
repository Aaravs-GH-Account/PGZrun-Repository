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
    st=t.time()
def draw():
    global satcou,sw
    screen.blit('space bg.jpg',(0,0))
    satseq=1
    for i in satel:
        i.draw()
        screen.draw.text(str(satseq),(i.pos[0],i.pos[1]),color='white')
        satseq=satseq+1
    #drawing lines from ligh list
    for i in ligh:
        screen.draw.line(i[0],i[1],'white')
    #showing a timer onscreen
    if satcou < 8:
       sw=t.time()-st
       sw=round(sw,1)
       screen.draw.text('Time:'+str(sw),(0,0),fontsize=25,color='white')
    else:
        screen.fill('black')
        screen.draw.text('Your final time is: '+str(sw),(75,175),fontsize=75,color='white')
satellite()
#click event
def on_mouse_down(pos):
    global satcou, ligh
    if satcou<8:
        if satel[satcou].collidepoint(pos):
            if satcou>0:
                ligh.append((satel[satcou-1].pos,satel[satcou].pos))
            #move to next satellight
            satcou=satcou+1
        else:
            ligh=[]
            satcou=0
def update():
    pass
p.go()
