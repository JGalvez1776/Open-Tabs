import webbrowser
from add_website import *
# TODO:
#   Make it so the program can be configed.
#       Ex: Make it so files can only be added in notepad.
#   Make the help print something useful
#   Allow the program to add websites directly through main.py

def main():
    while True:
        try:
            action = input('Please enter: "Open", "Add", or "Help"\n').lower()
            assert action in ["open", "add", "help"]
        except AssertionError:
            print('Please enter only one of the following:')
            print('"Open", "Add", or "Help"')
            continue
        if action == 'help':
            # TODO Make the prints here actually useful
            print('Help')
        elif action == 'add':
            add_file()

        elif action == 'open':
            file = open('websites.txt', 'r')
            for line in file:
                if line == '' or line[0] == '#':
                    continue
                webbrowser.open(line.strip('\n'))
            file.close()
        else:
            print('Invalid Response')
        action = ''

if __name__ == "__main__":
    main()