print("Welcome To The Game Even and Odd")
print("please if you want to go click x")


while True:
    try:
        number  = input("enter your number : ")
        if number == "x":
            print("close the game")
        
        number = int(number)
        if number % 2 == 0:
            print("number even ")
        else:
            print("number odd ")
        print("-------------------------------------")
    except (ValueError, TypeError) as op:
        print(op)
