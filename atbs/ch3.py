import random


def getAnswerLoop(ansNumber):
    for i in range(1, 10):
        if ansNumber == i:
            print('answer number ' + str(ansNumber))


getAnswerLoop(random.randint(1, 9))


def guessIt():
    answer = random.randint(1, 10)
    count = 0
    while True:
        print('Guess a number between 1 and 10')
        try:
            count += 1
            number = int(input())
            if number == answer:
                print('success, you guessed correctly!')
                print('you needed ' + str(count) + ' guesses')
                break
            elif number < answer:
                print('Too Low!')
                continue
            elif number > answer:
                print('Too high!')
                continue
            else:
                print('type in a number!')
                continue
        except ValueError:
            print('Error: give me a valid number')
            count = count - 1


def collatz():
    print('Hi, this is COLLATZ SEQUENCE, type in an integer')
    amount = 0
    try:
        number = int(input())
    except ValueError:
        print('Give me a valid number')
        number = int(input())

    while number != 1:
        amount = amount + 1
        if number < 0:
            print('your number must be positive value')
            continue
        elif number % 2 == 0:
            number = number / 2
            print(int(number))
        elif number % 2 == 1:
            number = (number * 3) + 1
            print(int(number))
    print('amount: ' + str(amount))


# getAnswerLoop(1)
guessIt()
collatz()
