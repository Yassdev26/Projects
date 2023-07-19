try:
    while True:
        num = int(input("Enter Your Number : "))
        result =  input("Enter your button : ")
        num1 = int(input("Enter Your Number : "))

        rstl = "Results : "



        if result == str("+"):
            print (f'{rstl} {int(num) + int(num1)}')

        if result == str("-"):
            print(f'{rstl} {int(num) - int(num1)}')

        if result == str("/"):
            print((f'{rstl} {int(num) / int(num1)}'))

        if result == str("*"):
            print (f'{rstl} {int(num) * int(num1)}')
except  ValueError as This:
    print('You Have Error')
    print(This)
