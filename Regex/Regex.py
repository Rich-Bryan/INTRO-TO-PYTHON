import re

with open("words.txt", "r") as file:
   
    CatDogPattern = re.compile(r"cat|dog") # word that contain cat or dog 1
    Four_letter_words = re.compile(r"\b\w{4}\b")  #four word letter 2
    hun_word = re.compile(r"hun") # word that contain hun 3
    ion = re.compile(r"ion\b") # word end in ion 
    ing = re.compile(r"ing\b") # word end in ing 
    q_word = re.compile(r"q(!?u)") #matching the word contain q not followed by u 4
    no_Vowels = re.compile(r"^[^\saeiou]*$") #word that have no vowels 5
    Only_Vowels = re.compile(r"\b[aeiou]+\b") # word that consit of only vowels 6
    End_with_nt = re.compile(r"nt\b")# word end with nt 7 
    two_row_vowels = re.compile(r"[aeiou]{2}") # two vowels in a row 8
    at_least_two_vowels = re.compile(r"\w*[aeiou]\w*[aeiou]\w*") # at least two vowels are in a word 9



    count1 = 0 #count for dog and cat
    count2 = 0 # count for four letter words.
    count3 = 0 # count for hun
    count_ing = 0
    count_ion = 0
    count4 = 0 # count for q not followed by u 
    count5 = 0 # count for word that have no vowels
    count6 = 0 # count for word consist of only vowels
    count7 = 0 # count for word end with nt
    count8 = 0 # count for two vowels in a row
    count9 = 0 # count for at least two vowels are in a word

    read = file.readlines()#[:12]
    for line in read:
        line = line.strip()


        if re.findall(CatDogPattern,line):
            count1 += 1
            #print(line, count1)

        if re.findall(Four_letter_words,line):
            count2 += 1

        if re.findall(hun_word, line):
            count3 += 1

        if re.findall(ion, line):
            count_ion += 1
        if re.findall(ing, line):
            count_ing += 1

        if re.findall(q_word, line):
            count4 += 1
        
        if re.findall(no_Vowels, line):
            count5 += 1
        
        if re.findall(Only_Vowels, line):
            count6 += 1
        
        if re.findall(End_with_nt, line):
            count7 += 1
        
        if re.findall(two_row_vowels,line):
            count8 += 1
        
        if re.findall(at_least_two_vowels, line):
            count9 += 1


    print("There are", count1, "word that contain cat or dog") # 1
    print("There are", count2, "word that are four letter") # 2
    print("There are", count3, "word that contain hun") # 3
    if count_ing > count_ion: # 4
        print("More words end with ing than with ion with", count_ing, "words")
    else:
        print("More words end with ion than with ing with", count_ion, "words")
    print("There are", count4, "word that contain q that are not immediately followed by a u")
    print("There are", count5, "word that have no vowels")
    print("There are", count6, "words that consist of only vowels")
    print("There are", count7, "word that end with nt")
    print("There are", count8, "words that are with two vowels in a row")
    print("There are", count9, "word that have at least two vowels in them")
