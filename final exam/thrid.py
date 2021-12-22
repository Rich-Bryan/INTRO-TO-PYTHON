import random

def montecarlo():
    fruits = {"red apples": 4, "blue plums": 4, "green apples": 4, "yellow pears":4}
    my_list = ["Red", "Green", "Blue", "Yellow", "Basket", "Raven"]

    loser = 0
    win = 0



    while win < 16:
        pick = random.choice(my_list)
        pick = pick.lower()
        for i in fruits: 
            
    
            if pick == "basket":
                maximum = max(fruits, key=fruits.get)

                if fruits[maximum] == 0:
                    #print("empty")
                    break
                else:
                    fruits[maximum] -= 1
                    win += 1

            sep = i.split() # split the list

            if sep[0] == pick:
                #print(pick)
                #print(win)
                if fruits[i] == 0:
                    #print("emty")
                    break
                else:
                    fruits[i] -= 1
                    win += 1


            if pick == "raven":
                loser += 1
                if loser == 5:
                    #print("raven", loser)
                    return False

        #print(fruits)
    return True
#print(montecarlo())



trials = 100000
winning_rate = 0 #2/3
for _ in range(trials):
    if montecarlo():
        winning_rate += 1
print(winning_rate/trials)










