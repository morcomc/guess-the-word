#guess the word v8 - final

import random
  
#function checks if the users inout is a letter
def strcheck(question):
    list = ("a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z")

    while True:
        try:
            response = input(question).lower()
            if response not in list:
                print ("Please enter a letter eg. a or b")
                continue
        except ValueError:
            print 
        return response

#function to print out symbols such as ** around outputs 
def token_statement(statement, char):
    print
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# function to get the letters out of the randomly selected word
def get_letters(word):
    #makes variables global
    global guesses
    global guesses_left
    global letters_guessed
    global keep_going
   
    total_letterse = len(word)
    letters=[' ']*len(word)
    num = 0
    for letter in word:
        letters[num] = letter
        num +=1

    #tells the user if there guess was coorect/incorrect
    total_guessed = total_letterse
    if guess in already_guessed:    #when the user guesses the same letter twice  
            print ("\nYou have already guessed that letter\nYou still have {}/{} Guesses left".format(guesses_left,GUESSES))
    elif guess not in letters:  #when the users guess is incorrect
            token_statement("----- That letter is not in the secret word -----","-")
            guesses_left -=1
            print ("Guesses left: {}/{}".format(guesses_left,GUESSES))
            print ("Letters Guessed Correctly:{}/{}\n".format(letters_guessed,total_letterse))
    elif guess in letters:  #when the users guess is correct
            token_statement("===== Well Done, that letter is in the secret word =====","=")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: {}/{}".format(guesses_left,GUESSES))
            print ("Letters Guessed Correctly: {}/{}\n".format(letters_guessed , total_letterse))

    already_guessed.append(guess)

            
    #when the user has guessed all the letters
    if letters_guessed == total_guessed:
        token_statement("***** Well done, You guessed all of the letters in the secret word *****","*")
        print ("\nThe word was {}".format(word))
        keep_going ="n"
        #when the user runs out of guesses
    elif guesses_left <= 0:
        print ("You have run out of guesses\nThe secret word was {} \nGame Over".format(word))
        keep_going ="n"

    #main routine
keep_going = ""
while keep_going == "":

      #variables
    GUESSES = 12
    guesses_left = GUESSES
    letters_guessed = 0
    keep_going = " "
    already_guessed = []
   
    #intro
    token_statement("*****Welcome to Guess The Word*****","*")

    #asks user for name
    name = input ("\nWhat is your name?\n").title()
    print ("Hello", name + "!\n")

    print
    done = False
    yes = {"yes", "y",}
    no = {"no", "n", "NO", "No"}
    while not done:
        choice = input ("Do you know how to play?\n").lower()
        if choice in yes:
            print
            break
        elif choice in no:
            #game  instructions
            print ("\nAt the start of the game you must choose which level you want to play,\nEasy or Hard.")
            print ("If you choose the Easy level you'll be guessing the letters in a 5 letter word.")
            print ("If you choose the Hard level you'll be guessing the letters in a 7 letter word.")
            print ("For each level you will have 12 guesses.")
            print ("If you run out of guesses and you have yet to guess all of the letters correctly\nthe game will end")
            break
        else:
            print ("If you know how to play please enter 'yes' or 'y'\nIf you dont know how to play please enter 'no' or 'n'")

    #list of 5 letter words
    ewords = ["birth", "chest", "death",
             "judge", "mouth", "canoe",
             "zebra", "spain", "black",
             "white", "blank", "firth",
             "girth", "fudge", "train",
             "frail", "grail", "grain"]
    #list of seven letter words
    hwords = ["abdomen", "picture", "banquet",
             "glamour", "javelin", "trample",
             "voyager", "crowned", "plastic",
             "imagine", "organic", "protein",
             "kitchen", "victory", "upgrade",
             "student", "century", "conquer"]

    
    print ("\nTHE GAME IS NOW STARTING!\n")
    easy = {"easy", "e", "5", "5 letters", "5 letter"}
    hard = {"hard", "h", "7", "7 letters", "7 letter"}
    done = False
    while not done: #asks which level to play
        level = input ("Which level would you like to play, Easy (5 letters) or Hard (7 letters)? \n").lower()
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
        guess = strcheck("Please enter a letter \n").lower()
        get_letters(word)
    #asks if they want to play again
    keep_going = input ("\nPress <enter> to play again or any key + <enter> to quit\n")   
    
print ("\nThank you for playing")



