import turtle
#draw shape
bob = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor("blue")
bob.pensize(5)
bob.color("white")

n = input("Enter a number for side: ")
n = int(n)

for i in range(n):
    bob.forward(75)
    bob.left(360/n)

sc.exitonclick()