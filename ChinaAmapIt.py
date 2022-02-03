# mapIt - Launches a map in Chinese Amap in the browser using an address from the 
# cli or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://amap.com/search?query=' + address)