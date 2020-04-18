
import os, time

def batch( script ):
    os.system(script)
    
class Vector:

    def __init__( self, x, y, z=None ):
        self.x = x
        self.y = y
        if z is not None:
            self.z = z

    def index( self, index, setter=None ):
        l = [self.x, self.y, self.z]
        if setter is not None:
            if index == 0:
                self.x = setter
            elif index == 1:
                self.y = setter
            elif index == 2:
                self.z = setter
        return l[index]

display = None

width = None
height = None

def init( title, w, h, fg, bg ):

    global display, width, height

    display = []
    
    batch(f"color {bg}{fg}")
    batch(f"title {title}")

    width = w
    height = h

    background(' ')

def get_state( x, y ):
    return display[x][y]

def background( state ):
    
    global display
    
    display = []
    
    for x in range(width):
        display.append(state * height)

text_aligner = 0.0

def text_align( align ):

    global text_aligner
    
    align.upper()
    if align == "CENTER":
        text_aligner = 0.5
    elif align == "RIGHT":
        text_aligner = 1.0
    else:
        text_aligner = 0.0

def text( text, x, y ):

    global display

    x = round(x)
    y = round(y)

    x -= int(round(len(text) * text_aligner))

    for i in range(len(text)):
        set_state(x + i, y, text[i]) 
        i += 1

def set_state( x, y, state ):
    
    global display

    x = round(x)
    y = round(y)

    row = ""
    cy = y
    y = 0
    
    for y in range(height):
        if y == cy:
            row += state
        else:
            row += display[x][y]

    display[x] = row

def fill_state( x, y, w, h, state ):

    x = round(x)
    y = round(y)
    w = round(w)
    h = round(h)

    for cx in range(w):
        for cy in range(h):
            try:
                set_state(x + cx, y + cy, state)
            except:
                print("ERROR (Out-of-Bounce): [X: " + str(x + cx) + "] [Y: " + str(y + cy) + "]")

frame = None

def set_frame( x_state, y_state ):

    global frame
    
    frame = Vector(x_state, y_state)

save = []    

def render( pause=None ):
    
    global display, save

    if save is not display:
        
        batch("cls")

        for y in range(height):
            line = ""
            for x in range(width):
                line += display[x][y]
            if frame is not None:
                line += frame.x
            print(line)
        if frame is not None:
            print(frame.y * (width + 1))
        
        save = display
    if pause is not None:
        if pause == "pause" : batch("pause")
        else : time.sleep(pause)
        
    
if __name__ == "__main__":
    init("Test", 32, 16, 'a', '0')
    for x in range(width):
        for y in range(height):
            background(' ')
            fill_state(x, y, 3, 5, '@')
            render(False)
    render(True)
