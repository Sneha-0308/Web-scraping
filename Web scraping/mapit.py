# Project : mapit.py with the webbrowser module

import webbrowser, sys ,pyperclip


if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    pyperclip.copy('870 Valencia St, San Francisco, CA 94110')
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)