#guess the word 

import random
guesses_left = 12
letters_guessed = 0
keep_going = " "
 
def get_letters(word):
    global guesses_left
    global letters_guessed
    global keep_going
   
    total_letterse = len(word)
    letters=[' ']*len(word)
    num = 0
    for letter in word:
        letters[num] = letter
        num +=1

    total_guessed = total_letterse
    if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed Correctly:{}/{}".format(letters_guessed,total_letterse))
    elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed Correctly: {}/{}".format(letters_guessed , total_letterse))


            

    if letters_guessed == total_guessed:
        print ("\nWell done, You guessed all of the letters in the secret word\nThe word was {}".format(word))
        keep_going ="n"
    elif guesses_left <= 0:
        print ("\nYou have run out of guesses\nThe secert word was {} \nGame Over".format(word))
        keep_going ="n"
       
#intro
print ("*****Welcome to Guess The Word*****\n")

name = input ("What is your name?").title()
print ("Hello", name + "!\n")

ewords = ["birth", "chest", "death",
         "judge", "mouth", "canoe"]
hwords = ["abdomen", "picture", "banquet",
         "glamour", "javelin", "trample"]


print ("THE GAME IS NOW STARTING!")
easy = {"easy", "e", "5", "5 letters", "5 letter"}
hard = {"hard", "h", "7", "7 letters", "7 letter"}
done = False
while not done: #asks which level to play
    level = input ("Which level would you like to play, Easy (5 letters) or Hard (7 letters)? ").lower()
    if level in easy:
        print ("\nLEVEL = EASY")
        word = random.choice (ewords)
        break
    elif level in hard:
        print ("\nLEVEL = HARD")
        word = random.choice (hwords)
        break
    else:
        print("\nIf you would like to play Easy please enter either - 'easy' or 'e'\nIf you would like to play Hard please enter either - 'hard' or 'h'\n")


#user guesses letters
keep_going = ""

while keep_going == "":
    guess = input ("\nPlease enter a letter ")
    get_letters(word)
    
print ("Thank you for playing")



