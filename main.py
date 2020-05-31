import webbrowser
from add_website import *

def main():
    while True:
        try:
            action = input('Please enter: "Open", "Add [website URL]", or "Help"\n').lower().split()
            assert action[0] in ["open", "add", "help"]
            break
        except AssertionError:
            print('Please enter only one of the following:')
            print('"Open", "Add", or "Help"')
    if action[0] == 'help':
        # TODO Make the prints here actually useful
        print('Help')
    elif action[0] == 'add':
        website = action[1]
        while True:
            add_file(website)
            website = input('Input next website to enter')
            break

    else:
        file = open('websites.txt', 'r')
        for line in file:
            if line == '' or line[0] == '#':
                continue
            webbrowser.open(line.strip('\n'))
if __name__ == "__main__":
    main()