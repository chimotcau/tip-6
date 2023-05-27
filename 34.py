from turtle import*
right(315)
for i in range(7):
    forward(16*20)
    right(45)
    forward(8*20)
    right(135)
penup()
for x in range(-10,25):
    for y in range(-10,15):
        setpos(x*20,y*20)
        dot(4,'red')    
#answer:77