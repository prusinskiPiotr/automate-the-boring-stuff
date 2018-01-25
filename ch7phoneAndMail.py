#! /usr/bin/python3
# phoneAndMail.py - program that looks for phone numbers and emails in copied text

import re

import pyperclip

phoneRegex = re.compile(r'''(
    (\+\d\d)?  # optional area code
    (\d{3})  # first 3 digits
    (\s|-|\.)?  # optional separator
    (\d{3})  # middle 3 digits
    (\s|-|\.)?  # optional separator
    (\d{3})  # last 3 digits
    )''', re.VERBOSE)

emailRegexp = re.compile(r'''(
    [a-zA-Z0-9._-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    if groups[1] != '':
        phoneNum += ' x' + groups[1]
    phoneNum = '-'.join([groups[2], groups[4], groups[6]])
    matches.append(phoneNum)

for groups in emailRegexp.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print("No matches were found")
