# Version av king, högsta kortet vinner

from random import randint

play_game = "J"

while play_game.upper() == "J":
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(f"Spelare ett vinner kastet: (player_one_roll).")
    elif player_two_roll > player_one_roll:
        print(f"Spelare två vinner kastet: (player_two_roll).")
    else:
        print(f"Ingen spelare vinner, det var lika.")

    playgame = input("Vill du spela igen? [J/N]")

# att göra: komma ihåg vilken spelare som har vunnit
#sedan fråga om vi vill spela igen
# sedan fråga om vi vill spela igen