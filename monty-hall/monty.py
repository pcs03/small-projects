"""
Simulation of the Monty Hall problem
"""

import random

wins = 0

switch = True

for i in range(10000000):
    doors = ["goat", "goat", "goat"]
    money_door = random.randint(0, 2)

    doors[money_door] = "money"
    goat_doors = [i for i, n in enumerate(doors) if n == "goat"]

    player_choice = random.randint(0, 2)

    opened_door = None

    if player_choice == money_door:
        opened_door = random.choice(goat_doors)
    else:
        for n in goat_doors:
            if n != player_choice:
                opened_door = n

    player_win = player_choice == money_door

    if switch:
        player_win = not player_win

    if player_win:
        wins += 1

print(wins)
