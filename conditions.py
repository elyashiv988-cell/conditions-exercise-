#namber 1
user_age=int(input("please enter your age "))
if user_age >= 18:
    print("can enter")
else:
    print("cannot enter")
#namber 2
temperature=38.2
if temperature >37.5:
    print("high temperature")
else:
    print("normal temperature")
#namber 3

stored_namber=74
givin_namber=int(input("enter a namber"))
if stored_namber==givin_namber:
    print("even number")
else:
    print("odd number")
# number 4
battery=15
is_charging=True
if battery < 20 and is_charging==True:
    print("low battery, charging now")
elif battery <20 and is_charging==False:
    print("low battery, connent charger")
else:
    print("battery OK")
