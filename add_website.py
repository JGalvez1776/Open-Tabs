def add_file():
    print('Begining to add websites:')
    file = open('websites.txt', 'a')
    status = True
    while status:
        action = input('What URL should be added? (Ex: https://www.google.com/)\n')
        file.write(f'{action}\n')
        response = input("Do you want to continue adding URL's? (y/n)").lower()
        if response == 'y':
            continue
        elif response == 'n':
            status = False
        else:
            print('Invalid Response: Exiting add URL mode')
            status = False