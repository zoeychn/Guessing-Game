# Guessing-Game

The `guessing_game()` function is the main function that runs the guessing game.

Within the function:
   - A `while True` loop ensures that the game keeps running until the player decides to stop.
   
   - `secret_number` is a random integer between 1 and 100, generated using `random.randint(1, 100)`. This is the number that the player needs to guess.
   
   - `attempts` is initialized to 0. This variable keeps track of how many attempts the player has made.
   
   - `max_attempts` is set to 10, limiting the number of guesses the player can make before the game ends.
   
   - The game starts with printing a welcome message and informing the player about the range of numbers they need to guess.
   
   - Inside the `while attempts < max_attempts` loop, the player is prompted to enter their guess.
   
   - Input validation is performed to ensure that the input is a valid integer within the range of 1 to 100. If the input is not valid, appropriate error messages are displayed, and the loop continues.
   
   - The player's guess is compared to the `secret_number`, and appropriate feedback is given (too low, too high, or correct).
   
   - If the player guesses the correct number within the allowed number of attempts, a congratulatory message is displayed along with the number of attempts taken, and the game breaks out of the loop.
   
   - If the player exhausts all their attempts without guessing the correct number, a message is displayed indicating that they've reached the maximum number of attempts, along with revealing the correct number.
   
   - After each game, the player is asked if they want to play again. If the player chooses not to play again, the game ends with a thank-you message.

The `if __name__ == "__main__":` block ensures that the `guessing_game()` function is executed when the script is run directly (not imported as a module). This allows the game to start when you run the script.
