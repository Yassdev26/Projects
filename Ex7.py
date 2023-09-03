import random
number = random.randint(1,5)
while True:
    try:
        while True:
            guess = int(input('Enter Your Guess Number : '))
            if guess == number:
                print('You Won The Game ^_^')
            elif guess != number:
                if guess < number:
                    print('The random number is bigger...')
                elif guess < number:
                    print('The random number is smaller...')
                else:
                    print('The random number is smaller...')
    except ValueError as op :
        print(op)