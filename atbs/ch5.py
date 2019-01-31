import pprint


def quiz():
    answers = {1: 'A', 2: 'C', 3: 'B'}
    i = 1
    for i in answers:
        print('question number ' + str(i) + ', your answer: ')
        userAnswer = input()
        if answers[i] == userAnswer:
            print('this is correct answer (' + answers[i] + ')')
            i += 1
        else:
            print('this is not the correct answer (' + answers[i] + ')')
            i += 1


def birthdayBank():
    birthdays = {'Julia': 'Dec 8', 'Piotr': 'Sep 7', 'Artur': 'Mar 13'}
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('what is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated')


def letterCounter():
    message = "Znowu dzis w Warszawie wieje wiatr, wlosy rozhustane jak ten bialy dym z marlboro"
    count = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    pprint.pprint(count)


def ticTacToe():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

    def printBoard(board):
        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for: ' + turn + ' move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    printBoard(theBoard)


def picnicItems():
    allguests = {'Damian': {'beers': 4, 'sausage': 3, 'bread': 1},
                 'Peter': {'wine': 1, 'cookies': 1},
                 'Joanna': {'beers': 4, 'crutches': 2},
                 'Julia': {'cookies': 2, 'sausage': 1, 'bread': 2}}

    def totalBrought(guests, item):
        numBrought = 0
        for keys, values in guests.items():
            numBrought = numBrought + values.get(item, 0)
        return numBrought

    print('Number of things brought:')
    print(' - beers ' + str(totalBrought(allguests, 'beers')))
    print(' - sausage ' + str(totalBrought(allguests, 'sausage')))
    print(' - bread ' + str(totalBrought(allguests, 'bread')))
    print(' - wine ' + str(totalBrought(allguests, 'wine')))
    print(' - cookies ' + str(totalBrought(allguests, 'cookies')))
    print(' - crutches ' + str(totalBrought(allguests, 'crutches')))


def gameInventory():

    def displayInventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
            print(str(v) + ' - ' + k)
            item_total += v
        print("Total number of items: " + str(item_total))

    def addToInventory(inventory, addedItems):
        for i in range(len(addedItems)):
            if addedItems[i] in inventory.keys():
                inventory[addedItems[i]] += 1
            else:
                inventory.setdefault(addedItems[i], 1)
        return inventory

    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'diamond']
    stuff = addToInventory(stuff, dragonLoot)
    displayInventory(stuff)


# quiz()
# birthdayBank()
# letterCounter()
# ticTacToe()
# picnicItems()
gameInventory()
