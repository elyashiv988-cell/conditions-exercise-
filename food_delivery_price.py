order_price=float(input("how much the order price? "))
if order_price<50:
    print("order too small")
else:
    club_n=input("do you have a club namber? ")
    if club_n=="yes":
        coupon=input("do you have a coupon? ")
        if coupon=="yes":
            print("free delivery and 10 discount")
        else:
            print("free delivery")
    else:
        print("delivery costs 15")