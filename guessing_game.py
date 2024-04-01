import random

def guessing_game():
    while True:
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10 

        print("Welcome to the Guessing Game!")
        print("I've picked a number between 1 and 100. Try to guess it.")

        while attempts < max_attempts:
            guess = input("Enter your guess (between 1 and 100): ")

            # Validating input
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
        else:
            print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    guessing_game()

