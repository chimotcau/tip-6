from turtle import*
for i in range(6):
    right(36)
    forward(10*20)
    right(36)
penup()
for x in range(-10,15):
    for y in range(-15,15):
        setpos(x*20,y*20)
        dot(5,'red')    