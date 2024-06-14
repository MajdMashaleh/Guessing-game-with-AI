"""
madj mashaleh
guess game using AI
AI assignment
Dr.Moa'ath
"""

def guessing_game():
    attempts = 0
    low = 0
    high = 500 # Adjusted the upper bound to 1000

    print("Welcome to the Guessing Game!")
    name = input("What's your name? ")

    print(f"Hi {name}! Choose a number between 0 and 1000. I will try to guess it.")

    last_guess = None  # Initialize the last guess variable

    while True:
        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is {guess}.")
        response = input("Enter 'l' if your number is lower, 'h' if your number is higher, or 'c' if I guessed correctly: ")

        if response == 'c':
            print(f"Yay, {name}! I guessed your number {guess} correctly!")
            print(f"It took me {attempts} attempts.")
            break
        elif response == 'l':
            high = guess - 1
        elif response == 'h':
            low = guess + 1

        # Update the last guess
        last_guess = guess

if __name__ == "__main__":
    while True:
        guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
