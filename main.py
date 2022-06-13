def startmenu():
    print("welcome to my text adventure game!")
    name = str(input("please enter your name  \n"))
    print("hello,", name)
    selection = int(input("press 1 to start when you are ready \n"))
    if selection == 1:
        print("alright then lets get started")

    else:
        startmenu()


startmenu()
