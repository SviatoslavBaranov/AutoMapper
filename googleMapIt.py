import webbrowser, sys, pyperclip

def google_search(args=''):
    if len(sys.argv) > 1:
        address = '+'.join(args)
    else:
        address = pyperclip.paste()
   
    webbrowser.open('https://www.google.com/maps/place/' + address)