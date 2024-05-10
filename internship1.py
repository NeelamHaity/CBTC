import random
print("ROCK-PAPER-SCISSOR")
print(f"___________________________________________________")

round=int(input("enter the number of rounds the player wants to play:"))
l=["rock","paper","scissor"]
player_win=0
comp_win=0

for i in range(1,round+1):
    print(f"round {i}")
    print(f"_____________________")
    player=input("player choice is:")
    if player!="rock" and player!="paper" and player!="scissor":
        print("try again")
        continue

    computer = (random.choice(l))
    print(f"computer choice is: {computer}")

    if computer=="rock":
        if player=="scissor":
            comp_win=comp_win+1
            print(f"computer won the round {i}")
            print(f" computer won score {comp_win}")
        elif player=="paper":
            player_win=player_win+1
            print(f"player won the round {i}")
            print(f"player won score {player_win}")
        elif player==computer:
            print("Draw round")
    elif computer=="paper":
        if player=="rock":
            comp_win = comp_win + 1
            print(f"computer won the round {i}")
            print(f" computer won score {comp_win}")
        elif player=="scissor":
            player_win=player_win + 1
            print(f"player won the round {i}")
            print(f"player won score {player_win}")
        elif player==computer:
            print("Draw round")
    elif computer=="scissor":
        if player=="paper":
            comp_win = comp_win + 1
            print(f"computer won the round {i}")
            print(f" computer won score {comp_win}")
        elif player=="rock":
            player_win = player_win + 1
            print(f"player won the round {i}")
            print(f"player won score {player_win}")
        elif player==computer:
            print("Draw round")
   


print(f" .....final announcement.....")

if player_win>comp_win:
    print(f"congrats! player won")
    print(f"player got marks {player_win}")
elif player_win==comp_win:
    print(f"Draw match ")
else:
    print(f" congrats! computer won")
    print(f"computer got marks {comp_win}")




