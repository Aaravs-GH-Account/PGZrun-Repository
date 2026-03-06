import pgzrun
#width and height of output screen
WIDTH=500
HEIGHT=500
#title of output screen
TITLE='PyGame Zero: Shapes'
def draw():
    #screen color
    screen.fill('white')
    #creating a rectangle ((x coordinate, y coordinate),(width, height))
    a=Rect((0,0),(50,50))
    #using the rectangle's center to move the rectangle to the center of the screen (x coordinate, y coordinate)
    a.center=250,250
    #draw the actual rectangle (variable,('color name'))
    screen.draw.filled_rect(a,('red'))
    #screens
#vital to keep the output screen open
pgzrun.go()