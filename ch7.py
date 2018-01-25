import re


def isPhoneNumber(text):
    if len(text) != 11:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 11):
        if not text[i].isdecimal():
            return False

    return True

print('730-344-894 is a phone number')
print(isPhoneNumber('730-344-894'))
print("730344894 technically is a phone number too, but it's not formatted correctly, so False")
print(isPhoneNumber('Moshi moshi'))

message = "Call me at 730-344-666 tommorow. 730-312-634 is my office."
for i in range(len(message)):
    chunk = message[i:i + 11]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print('Done.')

phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{3})')
mo = phoneNumRegex.search('My number is (521)-123-730')
print('Phone number found: ' + str(mo.groups()))

heroRegex = re.compile(r'Batman|Poison Ivy')
mo1 = heroRegex.search("Poison Ivy is an enemey of Batman")
print('This searches either for batman or Poison Ivy, found: ' + mo1.group())

batRegex = re.compile(r'Bat(man|mobile|arang|woman)')
mo2 = batRegex.search("The hero we are talking about uses a wide range of tools, including: Batbelt, Batarang, Batmobile")
print(mo2.group())

batwomanRegex = re.compile(r'Bat(wo)?man')
mo3 = batwomanRegex.search("The adventures of Batwoman")
print(mo3.group())

phoneNumRegex = re.compile(r'(\+\d\d)? (\d{3})-(\d{3}-\d{3})')
mo = phoneNumRegex.search('My number is +48 521-123-730')
print('Phone number with prefix found: ' + mo.group())

# ? match zero or one
# * match zero or more
# + match one or more
# (Ha){3} match exacly 3 repetitions of Ha
# (He){3, 5} match from 3 to 5 repetitions of He
# (Hi){3,} leave one blank to set minimum or maximum number of repetitions
# ^spam match string that starts with spam
# spam& match string that ends with spam
# . (dot) match any character except newline
# \d \w \s match digit, word, space respectively
# \D, \W, \S match anything except digit, word, space respectively
# [abc] match any character between the brackets (a, b or c)
# [^abc] match abt character that isn't between the brackets

batwowomanRegex = re.compile(r'Bat(wo)*man')
m3 = batwowomanRegex.search("The adventures of Batwowowowowowowoman")
print(m3.group())

namesRegex = re.compile(r'Agent \w+')
s1 = namesRegex.sub('CENSORED', 'Agent Arctor passed the informations to Agent Fred')
print(s1)

namesRegex = re.compile(r'Agent (\w)\w*')
s2 = namesRegex.sub(r'\1***', 'Agent Donna told Agent Fred that Agent Bob is a double agent')
print(s2)
