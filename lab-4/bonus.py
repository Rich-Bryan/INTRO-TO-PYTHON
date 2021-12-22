
#HourGlass

c = 0
print(' |""""""""""|')
for i in range(8,0,-2):
    c += 1 
    print(" "*c, "\\"+(":"*i)+"/")
print(c*" "," ||")
for j in range(2,10,2):
    print(" "*c, "/"+(":"*j)+"\\")
    c -= 1

print(' |""""""""""|')



#Slash Figure

n = int(input("enter a number: "))

for i in range(n):
    print("\\\\"*i + "!"*(((n*4)-2)-(i*4))+ "//"*i)
        


# n = 4, 14 of !  increase by 4 
# n = 5, 18 of !
# n = 6, 22 of !
# n = 7, 26 of !

