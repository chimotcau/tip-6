from turtle import*
for i in range(4):
    forward(6*40)
    right(150)
    forward(6*40)
    right(30)
penup()
for x in range(-5,15):
    for y in range(-10,15):
        setpos(x*40,y*40)
        dot(5,'red')
#answer:12 points         
         