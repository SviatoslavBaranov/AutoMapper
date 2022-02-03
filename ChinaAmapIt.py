# mapIt - Launches a map in Chinese Amap in the browser using an address from the 
# cli or clipboard

import webbrowser, sys, pyperclip

def amap_search(args=''):
    if len(sys.argv) > 2:
        address = ''.join(args)
    else:
        address = pyperclip.paste()

    webbrowser.open('https://amap.com/search?query=' + address)