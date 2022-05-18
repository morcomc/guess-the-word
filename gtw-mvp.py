import random

ewords = ["birth", "chest", "death",
         "judge", "mouth", "canoe"]

#variables
guesses_left = 12
letters_guessed = 0
total_letterse = 5

word = random.choice (ewords)


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
        elif guess in letters:
            print ("That letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1

    elif word == "chest":
        letters = ["c", "h", "e", "s", "t"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
        elif guess in letters:
            print ("That letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1

    elif word == "death":
        letters = ["d", "e", "a", "t", "h"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
        elif guess in letters:
            print ("That letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1

    elif word == "judge":
        letters = ["j", "u", "d", "g", "e"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
        elif guess in letters:
            print ("That letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1

    elif word == "mouth":
        letters = ["m", "o", "u", "t", "h"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
        elif guess in letters:
            print ("That letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1

    elif word == "canoe":
        letters = ["c", "a", "n", "o", "e"]
        total_guessed = total_letterse
        if guess not in letters:
            print ("That letter is not in the secret word")
            guesses_left -=1
        elif guess in letters:
            print ("That letter is in the secret word")
            guesses_left -=1
            letters_guessed +=1


    if letters_guessed == total_guessed:
        print (word)
        print ("You guessed all of the letters in the secret word")
        break
    elif guesses_left <= 0:
        print (word)
        print ("You have run out of guesses, Game Over")
        break        

print

