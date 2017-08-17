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


# quiz()
# birthdayBank()
# letterCounter()
