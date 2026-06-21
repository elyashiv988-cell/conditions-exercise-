trip=input("where do you want to go? ")
match trip:
    case forest:
        choose=input("what do you want, hide or walk ")
        if choose == "hide":
            print("you gide behind a tree")