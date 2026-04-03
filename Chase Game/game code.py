import random as r, pgzrun as p
WIDTH=750
HEIGHT=420
TITLE='Slime Chase Game'
score=0
timer=45
slime=Actor('slime.png')
slime.pos=(250,250)
food=Actor('food.png')
food.pos=(r.randint(10,600),r.randint(10,400))
def draw():
    screen.blit('grass.jpg',(0,0))
    slime.draw()
    food.draw()
    #writing text onscreen
    screen.draw.text('Score:' +str(score),color='black',center=(660,30),fontsize=60)
    screen.draw.text('Time Left:' +str(timer),color='black',center=(620,400),fontsize=60)
    if timer==0:
        screen.fill('white')
        screen.draw.text('Your final score was ' +str(score),color='black', center=(375,210),fontsize=90)
def update():
    global score
    if keyboard.left:
        if slime.x>80:
            slime.x=slime.x-7
    if keyboard.right:
        if slime.x<660:
            slime.x=slime.x+7
    if keyboard.up:
        if slime.y>30:
            slime.y=slime.y-7
    if keyboard.down:
        if slime.y<370:
            slime.y=slime.y+7
    if slime.colliderect(food):
        food.pos=(r.randint(10,600),r.randint(10,400))
        score=score+1
def countdown():
    global timer
    if timer>0:
        timer=timer-1
clock.schedule_interval(countdown,1)
p.go()
