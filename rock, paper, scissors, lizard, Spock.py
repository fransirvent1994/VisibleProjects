import random

options = ["paper", "scissors", "rock", "lizard", "spock"]
user = input(f"Choose option ({options}): ").lower()
choice = random.choice(options)
  
if user == "paper" and choice == "rock" or user == "paper" and choice == "spock" or user == "scissors" and choice == "paper" or user == "scissors" and choice == "lizard" or user == "rock" and choice == "scissors" or user == "rock" and choice == "lizard" or user == "lizard" and choice == "spock" or user == "lizard" and choice == "paper" or user == "spock" and choice == "rock" or user == "spock" and choice == "scissors":
  print(f"{user} vs {choice}")
  print("You win!")

elif user == choice:
  print("It's a draw")

else:
  print(f"{user} vs {choice}")
  print("You lose")
  
