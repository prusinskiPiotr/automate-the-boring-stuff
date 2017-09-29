def validateInput():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age')

    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and bumbers.')


def joinnsplit():
    tab = ['kiciaszek', 'mcdonalds', 'zabka']
    print(', '.join(tab))
    zdanie = 'alkohol, gitara, kosmiczni wojownicy'
    print(zdanie.split(', '))


def picnicList(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

tableData = [['John', 'Paul', 'George', 'Ringo'],
             ['Rhythm', 'Bass', 'Lead', 'Drums'],
             ["Don't", 'let', 'me', 'down']]


def printTable(tab):
    colWidths = [0] * len(tab)
    for i in colWidths:
        colWidths = max(tab[i], key=len)

    y = len(colWidths) + 3

    for x in range(len(tab[0])):
        print(str(tab[0][x]).ljust(y) + str(tab[1][x]).center(y) + str(tab[2][x]).rjust(y))

printTable(tableData)

# validateInput()
# joinnsplit()
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# picnicList(picnicItems, 15, 5)


