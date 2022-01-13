command = ""
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("the car has already started")
        else:
             started = True
             print("the car has started")
    elif command == 'stop':
        if not started:
            print("The car has already stoped")
        else:
            started = False
            print("the car stoped")
    elif command == 'help':
        print("""
start to start the car 
stop to stop the car
quit to quit
""")
    elif command == "exit":
        break
    else:
        print("sory the input is not valid try again")

    


