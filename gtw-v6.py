#guess the word 

import random
guesses_left = 12
letters_guessed = 0
keep_going = " "
already_guessed = []

def token_statement(statement, char):
    print
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

 
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
    if guess in already_guessed:
            print ("\nYou have already guessed that letter\nYou still have {} Guesses left".format(guesses_left))
    elif guess not in letters:
            token_statement("----- That letter is not in the secret word -----","-")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed Correctly:{}/{}".format(letters_guessed,total_letterse))
    elif guess in letters:
            token_statement("===== Well Done, that letter is in the secret word =====","=")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed Correctly: {}/{}".format(letters_guessed , total_letterse))

    already_guessed.append(guess)

            

    if letters_guessed == total_guessed:
        token_statement("\n***** Well done, You guessed all of the letters in the secret word *****","*")
        print ("\nThe word was {}".format(word))
        keep_going ="n"
    elif guesses_left <= 0:
        print ("\nYou have run out of guesses\nThe secert word was {} \nGame Over\n".format(word))
        keep_going ="n"
       
#intro
token_statement("*****Welcome to Guess The Word*****","*")

name = input ("\nWhat is your name?").title()
print ("Hello", name + "!\n")

print
done = False
yes = {"yes", "y",}
no = {"no", "n", "NO", "No"}
while not done:
    choice = input ("Do you know how to play?").lower()
    if choice in yes:
        print
        break
    elif choice in no:
        print ("At the start of the game you must choose which level you want to play,\nEasy or Hard.")
        print ("If you choose the Easy level you'll be guessing the letters in a 5 letter word.")
        print ("If you choose the Hard level you'll be guessing the letters in a 7 letter word.")
        print ("For each level you will have 12 guesses. When you guess a letter correctly\nyou will be shown that letters position in the word")
        print ("If you run out of guesses and you have yet to guess all of the letters correctly\nthe game will end")
        break
    else:
        print ("For yes please enter 'yes' or 'y'\nFor no please enter 'no' or 'n'")


ewords = ["birth", "chest", "death",
         "judge", "mouth", "canoe"]
hwords = ["abdomen", "picture", "banquet",
         "glamour", "javelin", "trample"]

keep_going = ""
while keep_going == "":
    
    print ("\nTHE GAME IS NOW STARTING!\n")
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
        print (already_guessed)
        guess = input ("\nPlease enter a letter ")
        get_letters(word)

    keep_going = input ("Press <enter> to play again or any key + <enter> to quit")   
    
print ("\nThank you for playing")



