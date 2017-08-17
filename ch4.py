import random
import copy

# spam = [['cat', 'bat', 'rat', 'elephant'], ['prosta', 'bella, bella', 'valentina', 'italia']]
# spam[1] * 3
# print(spam[1])


def catsNum():
    catName = []
    while True:
        print('Enter the name of the ' + str(len(catName) + 1) + ' cat, enter empty space to exit')
        name = input()
        if name == '':
            break
        catName = catName + [name]
    print('The cat names are: ')
    for name in catName:
        print('' + name)


def isMyPet():
    myPets = ['Abra', 'Tina', 'Lola', 'Sonia', 'Felix']
    while True:
        print('Enter a name of my pet: ')
        name = input()
        name = (name[0].upper() + name[1:])
        if name == '':
            break
        elif name in myPets:
            print(name + ' is one of my pets')
            continue
        else:
            print(name + ' is not my pet')
            break


# spam = ['prosta', 'bella, bella', 'valentina', 'italia', 'Valerina']
# spam.sort(key=str.lower)
# print(spam)


def magicBall():
    messages = [
        'It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook no so good',
        'Very doubtful'
    ]

    print(messages[random.randint(0, len(messages) - 1)])


def listToString(tab):
    for i in tab:
        print(i, end=', ')
        # linter marks this as error, but it works perfectly fine


def printGrid(tab):
    for x in range(len(tab[0])):
        print()
        for y in range(len(tab)):
            print(tab[y][x], end="")
    print()


def customGrid():
    print('pass X and Y')
    x = input()
    y = input()
    print('map size is: ' + str(x) + ':' + str(y))
    for i in range(int(x)):
        print()
        for j in range(int(y)):
            print('_|', end="")


grid = [['X ', 'X ', '0 ', '0 ', '0 ', 'X '],
        ['X ', 'O ', 'O ', 'X ', 'X ', 'X '],
        ['O ', 'O ', 'O ', 'O ', 'X ', 'X '],
        ['O ', 'O ', 'O ', 'O ', 'O ', 'X '],
        ['X ', 'O ', 'O ', 'O ', 'O ', 'O '],
        ['O ', 'O ', 'O ', 'O ', 'O ', 'X '],
        ['O ', 'O ', 'O ', 'O ', 'X ', 'X '],
        ['X ', 'O ', 'O ', 'X ', 'X ', 'X '],
        ['X ', 'X ', 'X ', 'X ', 'X ', 'X ']]
iSpam = ['apples', 'bananas', 'tofu', 'cats']
# catsNum()
# isMyPet()
# magicBall()
# listToString(iSpam)
# printGrid(grid)
customGrid()
