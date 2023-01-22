import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

name = input("Please input your name: ")
print("This is a contest out of 5 games. The first to win 3 games, wins the contest!")

computer_win_count = 0
player_win_count = 0
while computer_win_count < 3 or player_win_count < 3:
    print()
    player_1 = input("Please input: 'r' for Rock, 'p' for Paper or 's' for Scissors: ")

    while player_1 != "r" and player_1 != "p" and player_1 != "s":
        print()
        player_1 = input("Invalid Input: Try again\nPlease input: 'r' for Rock, 'p' for Paper or 's' for Scissors: ")
    else:
        if player_1 == "r":
            player_1 = rock
            print(f"{name} chose Rock")
        elif player_1 == "p":
            player_1 = paper
            print(f"{name} chose Paper")
        elif player_1 == "s":
            player_1 = scissors
            print(f"{name} chose Scissors")

    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_choice = rock
    elif computer_choice == 2:
        computer_choice = paper
    else:
        computer_choice = scissors

    print(f"Computer chose {computer_choice}")

    if player_1 == rock:
        if computer_choice == scissors:
            print(f"{name} wins")
            player_win_count += 1
        elif computer_choice == paper:
            print("Computer wins")
            computer_win_count += 1
        elif computer_choice == rock:
            print("it's a draw")
    elif player_1 == scissors:
        if computer_choice == rock:
            print("Computer wins")
            computer_win_count += 1
        elif computer_choice == paper:
            print(f"{name} wins")
            player_win_count += 1
        elif computer_choice == scissors:
            print("it's a draw")
    elif player_1 == paper:
        if computer_choice == rock:
            print(f"{name} wins")
            player_win_count += 1
        elif computer_choice == scissors:
            print("Computer wins")
            computer_win_count += 1
        elif computer_choice == paper:
            print("it's a draw")

    if computer_win_count == 3:
        print("Computer won the tournament!")
        print(f"The score finished Computer {computer_win_count} : {player_win_count} {name}!")
        exit()
    elif player_win_count == 3:
        print(f"{name} won the tournament!")
        print(f"The score finished Computer {computer_win_count} : {player_win_count} {name}!")
        exit()
