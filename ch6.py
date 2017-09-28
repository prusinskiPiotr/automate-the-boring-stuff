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


# validateInput()
# joinnsplit()
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# picnicList(picnicItems, 15, 5)


