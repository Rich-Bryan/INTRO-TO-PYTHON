 
import turtle
 
sc = turtle.Screen()
sc.screensize(canvwidth=500, canvheight=500)
bob = turtle.Turtle()
gig = turtle.Turtle()
gig.pensize(5)
bob.pensize(5)
gig.color("cyan")
bob.color("cyan")
gig.hideturtle()
bob.hideturtle()
bob.goto(-75,0)
gig.goto(-75, 0)
 
for i in range(3):
    bob.forward(150)
    bob.left(360/3)
    
 
 
gig.forward(75)
gig.left(60)
gig.forward(75)
gig.left(120)
gig.forward(75)
gig.left(120)
gig.forward(75)
 
sc.exitonclick()
 
 


