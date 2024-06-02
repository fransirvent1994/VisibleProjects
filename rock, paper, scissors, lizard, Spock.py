import random # First we import random library to make the computer choose between the options

start_game = True # Var to start the loop

while start_game: # Loop start
    options = ["paper", "scissors", "rock", "lizard", "spock"] # Different options to choose
    user = input(f"Choose an option: {', '.join(options)}: ").lower() # User option displayed with "," between each option.
    choice = random.choice(options) # Computer choice

    if user == choice: # If user chooses the same as computer
        print(f"{user} vs {choice}") # Prints the user choice and computer choice
        print("It's a draw!") # It will be a draw
    elif ( # This shows the results between the different choices
        (user == "paper" and choice in ["rock", "spock"])
        or (user == "scissors" and choice in ["paper", "lizard"])
        or (user == "rock" and choice in ["scissors", "lizard"])
        or (user == "lizard" and choice in ["spock", "paper"])
        or (user == "spock" and choice in ["rock", "scissors"])
    ):
        print(f"{user} vs {choice}")
        print("You win!")
    else:
        print(f"{user} vs {choice}")
        print("You lose!")

    play_again = input("Play again? (Y/N): ").lower() # Input to start again
    if play_again != "y" and play_again != "yes": # Conditional to start again or leave
        start_game = False
