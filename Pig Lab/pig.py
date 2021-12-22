import random

#Game 1
def Holdat20():
    total = 0
    while total <= 20:
        roll = random.randint(1,6)
        #print("roll: ", roll)
        if roll == 1:
            total = 0
            #print("turn total: ", total)
            return total
        else:
            total += roll
    #print("turn total: ", total)
    return total
#Holdat20()

#Game 2
#user = (int(input("how many simulations")))
def Hold_At_20_Out(numRun):
    outcome = {}
    for i in range(numRun):
 
        score = Holdat20()
        if score not in outcome:
            outcome[score] = 1
        else:
            outcome[score] += 1

    for i in sorted((outcome)):
        print("scores: ",i, "EStimate: ", outcome[i]/numRun)
    return outcome
#(Hold_At_20_Out(user))

# Game 3
def HoldAtX():
    total = 0
    while total <= 100:
        roll = random.randint(1,6)
        if roll == 1:
            total = 0
            return False

        else:
            total += roll
            #print("total: \t",total)
    #print("estimate: ",total/numRun)
    return total >= 100

#print(HoldAtX(100000))


def main():
    count = int(input("How mnay simulations: "))
    wins = 0
    for i in range(count):
        if HoldAtX():
            wins += 1
    print(wins)
    print("probability,", wins/count)
#main()

# Game 4
def Hold_At_20_Goal():

    New_score = int(input("New_score? "))
    turn_total = 0
    while True:
        roll = random.randint(1,6)
        print("Roll:", roll)
        turn_total += roll
        New_score += roll
        if turn_total >= 20 or New_score >= 100:
            print("Turn total: ", turn_total)
            print("New_score:", New_score)
            break


#(Hold_At_20_Goal())


# Game 5

def Hold_At_20_Goal_Game():
    turn_total = 0
    New_score = 0
    while True:
        roll = random.randint(1,6)
        print("Roll:", roll)
        if roll == 1:
            turn_total = 0
            print("turn total",turn_total )
            print("New score",New_score)

        if turn_total < 20:
            #print("turn total",turn_total)
            turn_total += roll
        else:
            New_score += turn_total
            print("turn total",turn_total)
            turn_total = 0
            print("new score,", New_score)

        if New_score >= 100:
            #print("New_score:", New_score)
            break

#Hold_At_20_Goal_Game()

# game 6
def Avg_pig_turn1():
    turn_total = 0
    New_score = 0
    turn = 0
    while True:
        roll = random.randint(1,6)
        #print("Roll:", roll)

        if roll == 1 :
            turn_total = 0    # reset to 0 if we get 1 
            turn += 1
            #print("turn total",turn_total )
            #print("New score",New_score)
            #print("turn", turn)

        elif turn_total < 20:
            turn_total += roll   # adding the new score and total turns
            #print("new turn total", turn_total)
            #print("insede turn total scores", New_score)

        else:  # add the score if the turn total is >= 20
            New_score += turn_total
            #print("new turn score",New_score)
            turn_total = 0
            turn += 1
            #print("turn", turn)
        if New_score + turn_total >= 100:
            #print("turn ", turn)
            #print("New_score:", New_score)
            break
    return turn 
#print(Avg_pig_turn1())

def Avg_Pig_Turn():
    games = int(input("Games? "))  # use 5
    totalTurn = 0   
    for i in range(games):
        x = Avg_pig_turn1()
        totalTurn += x
    print("average", totalTurn/games)
#Avg_Pig_Turn()

#Game 7

def Two_Player_Pig():
    turn_total = 0

    while True:
        roll = random.randint(1,6)
        print("Roll:", roll)

        if roll == 1 :
            turn_total = 0    # reset to 0 if we get 1 
            print("turn total", turn_total)
            break
    
        else:        # add to the turn total if roll is not 1
            turn_total += roll   

        if turn_total >= 20: # if turn total is >= 20 we stop 
            print("turn total", turn_total)
            break
    return turn_total

#Two_Player_Pig()


def main():
    score1 = 0 # to store values
    score2 = 0
    i = 1

    while True:
        print("Player 1 scores: ", score1)
        print("player 2 scores: ", score2)
        if i == 1:
            print("It is Player 1's turn")
            score1 += Two_Player_Pig()  # store the turn total
            print("New score",score1)
            i += 1    # go to next turn

        elif i == 2:
            print("It is Player 2's turn")
            score2 += Two_Player_Pig()# store the turn total
            print("New score",score2)   
            i -= 1          # go to previous turn

        if score2 >= 100 or score1 >= 100:
            break
#main()


#Game 8
def playerGame():
    turn_total = 0
    r = input("Roll/Hold")
    while r == "":
        roll = random.randint(1,6)
        print("Roll", roll)
        
        if roll == 1:
            turn_total = 0
            print("turn total", turn_total)
            break
        else:
            turn_total += roll
            r = input(f"turn total:{turn_total} Hold/Roll(Enter) ")


    return turn_total
        


def computerGame():
    turn_total = 0
    while True:
        roll = random.randint(1,6)
        print("Roll", roll)

        if roll == 1:
            turn_total = 0
            print("turn total", turn_total)
            break
        else:
            turn_total += roll

        if turn_total >= 20:
            print("Turn total", turn_total)
            break
    return turn_total



def main():
    player_score = 0
    computer_score = 0
    #player = random.randint(1,2)
    player = 1
    computer = 0
    if player == 1:
        computer = 2
        print("You are player 1")
    elif player == 2:
        computer = 1
        print("You are player 2")

    #print("You are player", player)
    print("Enter nothing to roll; anything to hold")
    
    turn = 1
    while True:
        
        if player == 1:
            print("Player 1 score", player_score)
            print("Player 2 score", computer_score)
        else:
            print("Player 1 score", computer_score)
            print("Player 2 score", player_score)

        if turn == 1 and player == 1:     # check if we get a player 1 and first turn
            print("It is Player 1's turn")
            player_score += playerGame()
            print("New score", player_score)
            turn += 1 # to the next turn

        elif turn == 1 and player == 2:  # check if player is 2 and we are on first turn
            print("It is Player", str(computer)+ "'s turn")
            computer_score += computerGame()
            print("New score", computer_score)
            turn += 1 # to the next turn

        elif turn == 2 and computer == 2:
            print("It is Player", str(computer)+ "'s turn")
            computer_score += computerGame()
            print("New score", computer_score)
            turn -= 1 # to the next turn

        else:
            print("It is Player 2's turn")
            player_score += playerGame()
            print("New score", player_score)        
            turn -= 1 # go back to previous turn

        if player_score >= 100 or computer_score >= 100: # end the prgram whoever reach 100
            break
main()
