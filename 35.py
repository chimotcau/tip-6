from turtle import*
right(45)
for i in range(7):
    forward(5*20)
    right(45)
    forward(10*20)
    right(135)
penup()
for x in range(-10,15):
    for y in range(-15,15):
        setpos(x*20,y*20) 
        dot(4,'red')   