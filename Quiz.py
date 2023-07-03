#1
answer = input("what my favorite subject ?")
if answer == "computer":
    print("GOOD")
else:
    print("BAD!")

#2
answer = input("what my favorite sport ?")
if answer == "soccer":
    print("GOOD")
else:
    print("BAD!")

#3
answer = input("what my favorite contry ?")
if answer == "Morocco":
    print("GOOD")
else:
    print("BAD!")

def WinGame():
        if answer == answer:
             print("You Win")
             quit()

def OverGame():
        print("Game Over")
        quit()

WinGame()
OverGame()