import random

start_game = True

while start_game:
    options = ["paper", "scissors", "rock", "lizard", "spock"]
    user = input(f"Choose an option ({', '.join(options)}): ").lower()
    choice = random.choice(options)

    if user == choice:
        print(f"{user} vs {choice}")
        print("It's a draw!")
    elif (
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

    play_again = input("Play again? (Y/N): ").lower()
    if play_again != "y" and play_again != "yes":
        start_game = False
