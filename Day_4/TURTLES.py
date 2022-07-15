import turtle
from turtle import *
import turtle as tur
tur.speed(1)






turtle.shape("turtle")
color('green', 'green')
begin_fill()
tur.circle(90,
           extent = 150)
while True:
    #one way to do this: you can use this loop, tweak it a bit and try to rewrite the movements such that
    #the movements of the turtle fit the turtle configurations that you wanted on your drawing
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
