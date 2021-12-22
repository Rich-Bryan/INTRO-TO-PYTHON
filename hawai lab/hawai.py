from typing import final
Vowels = {"a": "ah", "e":"eh", "i":"ee", "o":"oh", "u":"oo"}
GroupVowels = {"ai":"eye", 
        "ae":"eye",
        "ao":"ow",
        "au":"ow",
        "ei":"ay",
        "eu":"eh-oo",
        "oi":"oyo",
        "ou":"ow",
        "ui":"ooey"
}
options = "aeiou"
checking = ["a","e","i","o","u","p","k","h","l","m","n","w", " ", "'"]


def translate(word):
    str1 = ""
    for i in range(len(word)): # checking if i or e is after w
        if i == 0:
            str1 += word[i]
        elif (word[i] == "w" and (word[i-1] == "e" or word[i-1] == "i")):
            str1 += "v" 
        else:
            str1 += word[i]
    i = 0
    finalStr = ""   # aloha => len() => 5
                   # 01234
    tempStr = ""   # huaai ==> hoo-ah-eye

    while i < len(str1):
        if str1[i] in options: #checking if there is vowels
            if i != len(str1) -1: # check if we are on the last letter

                if str1[i] == str1[i+1] :
                    finalStr += Vowels[str1[i]] + "-"  # checking if the letter is = to the next letter
                    i+=1
                else:
                    tempStr += str1[i] + str1[i+1]    # if not add the letter and the next letter
                    if tempStr in GroupVowels.keys():   # check if the two letter is in the GroupVowels
                        finalStr += GroupVowels[tempStr] + "-"
                        i += 2
                    else:
                        finalStr += Vowels[str1[i]] + "-"
                        i += 1

                    tempStr = ""    # reset the temp string 
            else:
                finalStr += Vowels[str1[i]] # add the value if we are on the last letter
                i += 1
        else:
            finalStr += str1[i]  # add the consonant 
            i += 1

    if finalStr[-1] == "-":
        finalStr = finalStr[:-1] # remove the last (-) at the end 
    newString = finalStr.capitalize()

    result = ""
    for i in range(len(newString)):
        if newString[i] == "-" and newString[i+1] == " ": # remove the - when given an space input
            result += ""
        elif newString[i] == "'":
            result += ""
        else:
            result += newString[i]
    #print(result, "tes2")

    print(str1.upper(), "is pronounced",result)

#translate("aloha")

  

def UserInput():   # asking user for valid input
    correct = True
    while True:
        user = (input("Enter a hawaiian word to pronounce ==> ").lower())
        for letter in user: # invalid
            if letter not in checking:  # check for invalid words
                print(letter.upper(), "is not a valid hawaiian character")                       
                correct = False
                break # stop when we find a invalid char
        if correct:
            translate(user)
            while True:    # checking if user want another word
                user = input("Do you want to enter another word? Y/YES/N/NO ==> ").lower()
                #print(user)
                if user == "y" or user == "yes":
                    user = input("Enter a hawaiian word to pronounce ==>").lower()
                    for letter in user: 
                        if letter not in checking:
                            print(letter.upper(), "is not a valid hawaiian character")
                            print(letter)             
                            correct = False
                            break
                    if correct:
                        translate(user)
                elif user == "n" or user == "no":
                    print("bye")
                    return
        correct= True
UserInput()        
        
        
        
        
        
        
        
        
        
        
        
        
        

