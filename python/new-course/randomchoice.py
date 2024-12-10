import random
def choicescount():
    list=[]
    rocks=0
    papers=0
    scissors=0  
    while True:
        choice=random.choice(["rock", "paper", "scissors"])
        list.append(choice)
        if len(list) == 50:
            for i in list:
                if i == "rock":
                    rocks+=1
                elif i == "paper":
                    papers+=1
                elif i == "scissors":
                    scissors+=1
            print(f"Rocks: {rocks}, Papers: {papers}, Scissors: {scissors}")
            break
def game():
    a = "rock"
    b = "paper"
    c = "scissors"
    usercount=0
    computerwins=0
    while True:
        print (f"[a] = {a}\n[b] = {b}\n[c] = {c}")
        user=str(input("Your choice is: "))
        computer=random.choice(["a","b","c"])
        print(f"Computer choice is: {computer}")
   
        if user == computer:
            print("------------------------ Tie")
        elif user == "a" and computer == "b":
            computerwins+=1
            print("------------------------ Computer wins")
        elif user == "a" and computer == "c":
            usercount+=1
            print("------------------------ User wins")
        elif user == "b" and computer == "a":
            usercount+=1
            print("------------------------ User wins")
        elif user == "b" and computer == "c":
            computerwins+=1
            print("------------------------ Computer wins")
        elif user == "c" and computer == "a":
            computerwins+=1
            print("------------------------ Computer wins")
        elif user == "c" and computer == "b":
            usercount+=1
            print("------------------------ User wins")
        else:
            print("Invalid input")
        print(f"User wins: {usercount}, Computer wins: {computerwins}")
    game()
game()
