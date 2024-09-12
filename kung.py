# Version av king, högsta kortet vinner

from random import randint

play_game = "J"
player_one_win = 0
player_two_win = 0

player_one_name = input("Vad heter spelare ett?")
player_two_name = input("Vad heter spelare två?")

while play_game.upper() == "J":
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(f"{player_one_name} vinner kastet med slaget: {player_one_roll}!")
        player_one_win += 1
    elif player_two_roll > player_one_roll:
        print(f"{player_two_name} vinner kastet med slaget: {player_two_roll}!")
        player_two_win += 1
    else:
        print(f"Ingen av spelarna vinner, det blir oavgjort!")

    # finisher
    if player_one_win >= 2:
        print(f"{player_one_name} vinner över {player_two_name}, som vann {player_two_win} gång(er)!")
        play_game = "N"
    elif player_two_win >= 2:
        print(f"S{player_two_name} vinner över {player_one_name}, som vann {player_one_win} gång(er)!")
        play_game ="N"

    

    # play_game = input("Vill du spela igen? [J/N]")
    
   