import webbrowser, sys, pyperclip

def amap_search(args=''):
    if len(sys.argv) > 2:
        address = ''.join(args)
    else:
        address = pyperclip.paste()

    webbrowser.open('https://amap.com/search?query=' + address)