import pgzrun as p,random

WIDTH=800
HEIGHT=600
TITLE='Recycle Paper Bags'

START_SPEED=10
ITEMS=['bag','battery','bottle','chips']
FINAL_LEVEL=6
current_level=1

#lose the game
game_over=False

#win the game
game_complete=False

items=[]
animations=[]

def draw():
    global items,current_level, game_over, game_complete
    screen.clear()
    screen.blit('bground',(0,0))

    if game_over:
        display_message('GAME OVER', 'Try again!')
    elif game_complete:
        display_message("YOU WIN",'Great Job!')
    else:
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300), color='black')
    screen.draw.text(subheading, fontsize=30, center=(400,330), color='black')

def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

#Make items

#1. Get the options from ITEMS list - random
#2. Create actors and add it to items list
#3. Layout items - diplay them with equal spacing
#4. Animations - move the objects down

def make_items(number_of_extra_items):
    items_to_create = get_option_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items


p.go()