## code written by Karan jagota

import simplegui
import random 
message = "STONE PAPER OR SCISSOR"

a="stone"
b="paper"
c="scissor"

def stone():
    global a
    print "you choose " + a 
    b=random.randrange(1,4)
    if b==1:
        b=str(1)
        b="stone"
        print "computer chooses " + b
        print "tie"
    elif b==2:
        b=str(2)
        b="paper"
        print "computer chooses " + b
        print"you win"
    else:
        b="scissor"
        print "computer chooses " + b
        print "you loose"
           
def paper():
    global b
    print "you choose " + b
    c=random.randrange(1,4)
    if c==1:
        c=str(1)
        c="stone"
        print "computer chooses " + b
        print "you win"
    elif c==2:
        c=str(2)
        c="paper"
        print "computer chooses " + b
        print"tie"
    else:
        c="scissor"
        print "computer chooses " + b
        print "you loose"
    
def scissor():
    global c
    print "you choose " + c 
    b=random.randrange(1,4)
    if b==1:
        b=str(1)
        b="stone"
        print "computer chooses " + b
        print "you win"
    elif b==2:
        b=str(2)
        b="paper"
        print "computer chooses " + b
        print"you win"
    else:
        b="scissor"
        print "computer chooses " + b
        print "tie"   
    
    
def draw(canvas):
    canvas.draw_text(message, [22,102], 20, "white")
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("stone",stone,100 )
frame.add_button("paper",paper,100 )
frame.add_button("scissor",scissor,100 )
frame.set_draw_handler(draw)

frame.start()