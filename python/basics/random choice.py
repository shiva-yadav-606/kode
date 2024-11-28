def game():
    import random
    print("rock-paper-scissors game")
    r="rock"
    p="paper"
    s="scissors"
    all_choices=(r,p,s)
    x=input(f"enter your choice by first letter of ({r},{p},{s}):")
    if x not in all_choices:
        print("\invalid choice!\n")
    bot=random.choice(all_choices)
    
    print("u choose=",x)
    print("bot choose=",bot)
    result()
    print('--------------PRESS ENTER TO PLAY-------------')
    input()

def result():

    if x == bot:
        print("Tie")
    elif (
            (x == "rock" and bot == "scissors") or (x == "paper" and bot == "rock") or (x == "scissors" and bot == "paper")
    ):
        print("you win")
    else:
        print("you lose")
    
