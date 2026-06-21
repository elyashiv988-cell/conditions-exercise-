'''
undrestanding questions:

1. if checks if the condition is met
elif checks whether another condition is met before the else.
else fulfills whatener conditions weren't met before it

2. to check complex condition several times. 


3. it's check if the assignm is True (not empty)
it's helpful because it's a short way to check a simple condition. 

4.  a shortcut way to test one condition over several times. 
'''
# number 1
status_code=200
if status_code==200:
    print("ok")
elif status_code==404:
    print("not found")
elif status_code==500:
    print("server error")
else:
    print("unknown status")
#number 2
role="admin"
if role=="admin":
    print("full access")
elif role=="editor":
    print("limiter access")
elif role=="viewer":
    print("read only")
else:
    print("no access")
# number 3
score=87
print("pass") if score>=60 else print("fail")
print (score)
#number 4
command="start"
match command:
    case "start":
        print("startint system")
    case "stop":
        print("stoppint system")
    case "restart":
        print("restarting systen")
    case _:
        print("unknonwn command")
