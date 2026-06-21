#namber 1
'''
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
# number 5
stored_password="python123"
user_password=(input("enter your password"))
if stored_password==user_password:
    print("access approved")
else:
    print("access denied")
# number 6
score=72
if score >90:
    print("excellent")
elif score >75:
    print("good")
elif score > 60:
    print("pass")
else:
    print("failed")
# number 7
number1=int(input("enter first number"))
number2=int(input("enter secend number"))
if number1 > number2:
    print("first is bigger")
elif number1 < number2:
    print("secend is bigger")
else: 
    print("equal")
# number 8
'''
fuel= 40
distance=30
if fuel - distance >=10:
    print("enough fuel with rserve")
elif 0 < fuel - distance < 10:
    print("enough fuel, low resreve")
else:
    print("not enough fuel")
# number 9
username=input("enter your username ")
if username:
    print(f"hello {username}")
else:
    print("guest user")