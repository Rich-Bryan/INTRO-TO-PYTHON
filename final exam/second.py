import turtle
turtle.bgcolor("#000000") # This makes the background black
bob = turtle.Turtle()
bob.speed(0)

# Q1: What is iro?
# I have no idea what these are.  
# Programmer said they are "traditional"
iro = ["#F08F90","#F2EA0A","#003171","#A87CA0","#8DB255","#317589"]


excelsior = 360/(len(iro)) +7

# Q2: What is sky? What does changing it do? 
# Programmer said it affected how "groovy" it was
sky = 6
# Q3: What is petal? What does changing it do?
# Programmer said that it affected how "awesome" it was
petal = 15
# Q4: What is style? What does changing it do?
# Programmer said "the variable explains itself".
# I'm beginning to think the programmer is a liar.
style = 100


# Q5: What does desegni do?  What does storony and pikkus affect?
# Seems so familiar, like the students of CIS 1051 have written this before...
def desegni(bob,storony,pikkus):
    for _ in range(storony):
        bob.forward(pikkus)
        bob.left(360/storony)


# Q6: What does fnord do? 
def fnord(bob):
    for i in iro:
        bob.pencolor(i)
        desegni(bob,sky,style)
        bob.left(excelsior)

for i in range(petal):
    fnord(bob)

turtle.done()