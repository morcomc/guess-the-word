import random

#intro
print ("Welcome to Guess The Word")

name = input ("What is your name?")
print ("Hello", name + "!")

ewords = ["birth", "chest", "death",
         "judge", "mouth", "canoe"]
hwords = ["abdomen", "picture", "banquet",
         "glamour", "javelin", "trample"]
#variables
guesses_left = 12
letters_guessed = 0
total_letterse = 5
total_lettersh = 7

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
    guess = input ("Please enter a letter ")
    #5 letter words
    if word == "birth":
        letters = ["b", "i", "r", "t", "h"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/5".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))

    elif word == "chest":
        letters = ["c", "h", "e", "s", "t"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))

    elif word == "death":
        letters = ["d", "e", "a", "t", "h"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))

    elif word == "judge":
        letters = ["j", "u", "d", "g", "e"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))

    elif word == "mouth":
        letters = ["m", "o", "u", "t", "h"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))

    elif word == "canoe":
        letters = ["c", "a", "n", "o", "e"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/5".format(letters_guessed))

    #7 letter words
    elif word == "abdomen":
        letters = ["a", "b", "d", "o", "m", "e", "n"]
        total_guessed = total_lettersh
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/7".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/7".format(letters_guessed))

    elif word == "picture":
        letters = ["p", "i", "c", "t", "u", "r", "e"]
        total_guessed = total_lettersh
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/7".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/7".format(letters_guessed))

    elif word == "banquet":
        letters = ["b", "a", "n", "q", "u", "e", "t"]
        total_guessed = total_lettersh
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/7".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/7".format(letters_guessed))

    elif word == "glamour":
        letters = ["g", "l", "a", "m", "o", "u", "r"]
        total_guessed = total_lettersh
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/7".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -= 1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/7".format(letters_guessed))

    elif word == "javelin":
        letters = ["j", "a", "v", "e", "l", "i", "n"]
        total_guessed = total_lettersh
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/7".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/7".format(letters_guessed))

    elif word == "trample":
        letters = ["t", "r", "a", "m", "p", "l", "e"]
        total_guessed = total_lettersh
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
            print ("Guesses left: {}".format(guesses_left))
            print ("Letters Guessed:{}/7".format(letters_guessed))
        elif guess in letters:
            print ("Well Done, that letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1
            print ("Guesses left: = {}".format(guesses_left))
            print ("Letters Guessed: {}/7".format(letters_guessed))

    if letters_guessed == total_guessed:
        print ("Well done, You guessed all of the letters in the secret word\nThe word was {}".format(word))
        break
    elif guesses_left <= 0:
        print ("You have run out of guesses, Game Over")
        break

        

print ("Thank you for playing")

