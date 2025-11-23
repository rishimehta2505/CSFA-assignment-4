import random

def number_guessing_game():
    """
    A simple number guessing game where the user has to guess a number
    between 1 and 100.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guess = 0
    
    while guess != secret_number:
        try:
            # Get user input for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is too high, too low, or correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()