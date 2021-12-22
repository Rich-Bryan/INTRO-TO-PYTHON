import turtle
# tirtle clock
sc = turtle.Screen()
sc.title("turtle clock")
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("white")
sc.bgcolor("blue")
bob.speed()


for i in range(12):
  bob.up()
  bob.forward(70)
  bob.down()
  bob.forward(20)
  bob.up()
  bob.forward(20)
  bob.stamp()  # leave the turtle on seen
  bob.forward(-110)
  bob.right(360 / 12)  #have 12 turles as a clock
  bob.hideturtle() # hide the turtle for the middle part
sc.exitonclick()
