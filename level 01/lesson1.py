from turtle import *

#we want to paint a house

#step 1:  drow  a square
shape("turtle")
#speed(20)
width(5)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of scuare

#drawing a door

forward(75)
color("green")
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


# drawing a window
penup()
goto(170, 170)
pendown()

color("purple")
right(60)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)


#drawing a window
penup()
goto(35, 170 )
pendown()

color("purple")
right(180)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)




















exitonclick()