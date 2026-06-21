computer_choice = "rock"
choose=input("cellect, rovk, paper, scissors ")
if choose==computer_choice:
    print("draw")
elif choose == "paper":
    print("you win!")
elif choose=="scissors":
    print("computer wins")
elif choose=="rock":
    print("draw")
else:
    print("invalid move")