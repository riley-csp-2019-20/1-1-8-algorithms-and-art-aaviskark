#import trtl
import turtle as trtl

robot= trtl.Turtle()
robot.speed(0)
#draw side of first mountain
robot.pensize(5)
robot.up()
robot.goto(-200,-50)
robot.down()
robot.left(45)
robot.forward(200)

#make right side
robot.right(135)
robot.circle(120,90,45)

#make the next mountain
robot.up()
robot.goto(-10,0)
robot.down()
robot.circle(180,90,45)
robot.setheading(45)
robot.right(90)
robot.forward(325)

#make a horizon and add snowcaps to the mountains
robot.penup()
robot.goto(-300,-50)
robot.setheading(0)
robot.pendown()
robot.forward(700) 
robot.up()
robot.goto(-100,50)
robot.down()
robot.forward(50)
robot.up()
robot.goto(161,125)
robot.down()
robot.forward(64)

#make a house with a roof
robot.up()
robot.goto(135,75)
robot.setheading(180)
robot.down()
robot.forward(30)
robot.left(90)
robot.forward(30)
robot.up()
robot.goto(120,105)
robot.setheading(180)
robot.down()
robot.fillcolor("black")
robot.begin_fill()
robot.circle(20,360,3)
robot.end_fill()
robot.up()

#make a sun
robot.goto(-300,300)
robot.down()
robot.fillcolor("yellow")
robot.begin_fill()
robot.circle(50)
robot.end_fill()

#make a tree
robot.up()
robot.goto(75,25)
robot.setheading(90)
robot.down()
robot.pencolor("brown")
robot.circle(50,45,4)
robot.up()
robot.goto(80,75)
robot.down()
robot.pencolor("green")
robot.pensize(15)
robot.fillcolor("green")
robot.begin_fill
robot.circle(15)
robot.end_fill

#make smoke coming out of the house
smoke=0



wn= trtl.Screen()
wn.mainloop()