import random

# List of words to guess from
words_list = ['banana', 'apple', 'orange', 'grapes', 'mango', 'watermelon', 'peach', 'blueberry']

# Function to display the current state of the word with guessed letters
def display_word(word, correct_guesses):
    display = ''.join([letter if letter in correct_guesses else '_' for letter in word])
    return display

# Function to display the hangman state
def display_hangman(incorrect_guesses):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
        _________
        ''',  # Full hangman
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
        _________
        ''',  # Missing one leg
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
        _________
        ''',  # Missing both legs
        '''
           -----
           |   |
           O   |
          /|   |
               |
        _________
        ''',  # Missing both legs, one arm
        '''
           -----
           |   |
           O   |
           |   |
               |
        _________
        ''',  # Missing both legs, arms
        '''
           -----
           |   |
           O   |
               |
               |
        _________
        ''',  # Only head
        '''
           -----
           |   |
               |
               |
               |
        _________
        '''   # Initial stage
    ]
    return stages[len(incorrect_guesses)]

# Function to check if the user input is valid
def validate_input(user_input):
    if len(user_input) != 1 or not user_input.isalpha():
        return False
    return True

# Main hangman game function
def play_hangman():
    word = random.choice(words_list).lower()
    correct_guesses = set()
    incorrect_guesses = set()
    attempts_left = 6  # Maximum incorrect guesses
    guessed_letters = set()

    print("Welcome to Hangman!")

    while attempts_left > 0:
        print("\nWord: ", display_word(word, correct_guesses))
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {attempts_left}")
        print(display_hangman(incorrect_guesses))

        guess = input("Guess a letter: ").lower()

        if not validate_input(guess):
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            correct_guesses.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check if the user has guessed the word
        if set(word) == correct_guesses:
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"You've run out of attempts. The word was: {word}")
        print(display_hangman(incorrect_guesses))

# Replay option
def replay():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Game loop
if __name__ == "__main__":
    while True:
        play_hangman()
        if not replay():
            print("Thanks for playing!")
            break
