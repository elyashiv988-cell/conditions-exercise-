trip=input("where do you want to go? ")
match trip:
    case "forest":
        choose=input("what do you want, hide or walk ")
        if choose == "hide":
            print("you gide behind a tree")
        elif choose == "walk":
            print("you find a sleeping wolf")
        else:
            print("invalid forest action")
    case "cave":
        choose=input("do you have a toruh? ")
        if choose == "yes":
            turn= input("left or right? ")
            if turn == "left":
                print("you find gold")
            elif turn == "right":
                print("you find bats")
            else:
                print("invalid cave path")
        else:
            print("it's too dark to enter")
