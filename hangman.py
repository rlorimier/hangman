import random

# list with hangmans
def hangman(moves_left):
    hangmans = [ '''
    +---+
     O   |
    /|\  |
    / \  |
        ===''', '''
    +---+
     O   |
    /|\  |
    /    |
        ===''', '''
    +---+
     O   |
    /|\  |
        |
        ===''', '''
    +---+
     O   |
    /|   |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
        ===''', '''
    +---+
    O   |
        |
        |
        ===''', '''
    +---+
        |
        |
        |
        ===''']

    return hangmans[moves_left]


# selecting the word from a list
def get_word():
    words_list = "squirrel bear whale coyote hedgehog lion dolphin crocodile raccoon hyena monkey panda deer leopard kangaroo tiger zebra giraffe hippo wolf elephant gorilla snake eagle antelope vulture panther parrot rhino shark rabbit reindeer lizard leopard koala frog turtle toucan spider sparrow scorpion moose iguana capybara butterfly bison raven falcon sheep buffalo wildebeest baboon ostrich flamingo jackal".upper().split()
    word = random.choice(words_list)
    return word


# setting the game
def run_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    moves_left = 6
    print("\033[93m HANGMAN \033[m")
    print(hangman(moves_left))
    print(word_completion + "\n")

    while not guessed and moves_left > 0 :
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter. Please try again.")
            elif guess not in word:
                print(f"{guess} is not in the word. Please try again")
                moves_left -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                list_letters = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    list_letters[index] = guess
                word_completion = "".join(list_letters)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess. Please try again.")
        print(hangman(moves_left))
        print(word_completion + "\n")
        print(guessed_letters)

    if guessed:
        print("\033[96mCongratulations! You guessed the word!\033[m")
    else:
        print(f"\033[95mYou ran out of tries. The word was {word}. Game Over!\033[m")

# main function to run the game
def main():
    word = get_word()
    run_game(word)
    while input("Do you want to play again? [Y/N] ").upper() == "Y":
        word = get_word()
        run_game(word)
    print("See you next time")


if __name__ == "__main__":
    main()