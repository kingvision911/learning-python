x = "awsome"
def myFun():
    x = "fantastic"
    print("python is " + x)
myFun()
print("python is " + x)

x = "awsome"

def myFunc():
    global x 
    x = "fantastic"

myFunc()

print("python is " + x)
