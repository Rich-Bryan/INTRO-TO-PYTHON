import turtle

#1.1


myTurtle = turtle.Turtle()
def drawSquare(myTurtle, squareSize):
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        
    
#drawSquare(myTurtle, 50)





bob = turtle.Turtle()
bob.speed(0)

def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        myTurtle.fd(squareSize)

                
drawRow(bob, 5, 50)


def drawGrid(myTurtle, size, squareSize):
    
    for i in range(size):
        
        drawRow(bob,5,50)
        bob.up()
        bob.setpos(0,squareSize*(i+1))
        bob.down()
        
        
        
#drawGrid(bob,5,50)
        


def drawSquareStairs(myTurtle, height, squareSize):
    for i in range(height):
        drawRow(bob,5-i,50)
        bob.up()
        bob.setpos(0,squareSize*(i+1))
        bob.down()
        
        
#drawSquareStairs(bob,5,50)


#2.2.1

def drawNgon(myTurtle, numSides, sideLength):
    for i in range(numSides):
        bob.fd(sideLength)
        bob.left(360/numSides)
#drawNgon(bob, 6, 100)


def drawNgonSpiral(myTurtle, numSides, sideLength,numShapes):
    for i in range(numShapes):
        drawNgon(bob, numSides, sideLength)
        bob.right(360/numShapes)
        


#drawNgonSpiral(bob, 6, 100, 35)





#3.3 Bonus

def drawNgonSpiral(myTurtle, numSides, sideLength,numShapes):
    bob.color("red")
    for i in range(numShapes):
        drawNgon(bob, numSides, sideLength)
        bob.right(360/numShapes)
        if i % 2 == 0:
            bob.color("blue")
        else:
            bob.color("red")



#drawNgonSpiral(bob, 6, 100, 35)





    
