#Cash


while True:
    dollars = float(input("changes owned: "))
    if dollars >= 0:
        break



#greedy algorithms
def cash():
    count = 0 # count the coins
    cents = round(dollars*100)#convert into cents

    while cents >= 25: # 25c
        count += 1
        cents -= 25
        
    while cents >= 10: # 10c
        count += 1
        cents -= 10
        
    while cents >= 5: # 5c
        count += 1
        cents -= 5

    while cents >= 1: # 1c
        count += 1
        cents -= 1
    print(count)

cash()

