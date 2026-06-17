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


def get_option_create(number_of_extra_items):
    items_to_create=['paper']
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item = Actor(option+'img')
        new_items.append(item)
    return new_items

def layout_items(new_items):
    gaps=len(new_items)+1
    gap_size=WIDTH/gaps
    random.shuffle(new_items)
    for index, item in enumerate(new_items):
        new_x_pos=(index+1) * gap_size
        item.x = new_x_pos

def animate_items(new_items):
    global animations
    for i in new_items:
        duration= START_SPEED-current_level
        animation=animate(i, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)
        
def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if 'paper' in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level=current_level+1
        items=[]
        animations=[]

def stop_animations(animations):
    for i in animations:
        if i.running:
            i.stop()
p.go()