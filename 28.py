from turtle import*
for i in range(4):
    forward(10*20)
    right(90)
right(30)
for j in range(5):
    forward(6*20)
    right(60)
    forward(6*20)
    right(120)
penup()
for x in range(-10,15):
    for y in range(-10,15):
        setpos(x*20,y*20) 
        dot(4,'red') 
#answer: 51               