correct_pin=4321
balance=500
user_pin=int(input("Enter your PIN code"))
if correct_pin==user_pin:
    amaount=int(input("how much money do you want to withdraw? "))
    if amaount>balance:
        print("not enough miney")
    else:
        receipt=input("do you want a rceipt? ")
        if receipt=="yes":
            print("withdrawal approved with receipt")
        elif receipt=="no":
            print("withdrawal approved without receipt")
        else:
            print("withdrawal approved")
else:
    print("Wrong PIN")