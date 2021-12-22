import turtle
# 1.1 
def bottles(x):
    for i in range(x):
        print(x-i, " bottles of beer on the wall", x -i, "bottles of beer \n Take one down, pass it around," , x-(i+1), "bottles of beer on the wall")
        i += 1
num_bottle = int(input("number of bottles: "))
bottles(num_bottle)



#1.2
def multi(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            total = row*col
                    
            print(total, end="\t")
        print()
number = int(input("enter a number: "))
multi(number)

#number practice

def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    print("total = ", total)
number = int(input("enter a number for n: "))
sum(number)
