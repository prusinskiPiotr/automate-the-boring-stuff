#! /usr/bin/python3
# mapit.py - launches a map in the browser using an address from the command line or clipboard

import pyperclip
import webbrowser
import sys

if len(sys.argv) > 1:
    # Get the address from command line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.pl/maps/place/' + address)
