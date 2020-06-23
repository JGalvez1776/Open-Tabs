def read_file(file_name):
    # NOTE: This function can only read the contents of config.txt 
    # TODO: Maybe make this work for any function and have another
    #       work to process the data into something useable


    #try:
    file = open(file_name, 'r')
    config = dict()
    for line in file:
        # TODO: Check is the needed array is needed or if it can be shorted down to '', ' ' or something similar
        if line not in ['', ' ', '\n', '\t'] and line[0] != '#':
            split_line = line.split('=')
            split_line[1] = split_line[1].lower().strip() == 'true'
            config[split_line[0].strip()] = split_line[1]

    file.close()
    return config
    #except:
    # Make this give more detail about the problem
    # Give more types of excepts to catch differnt errors
    #print(f'Unable to open the file: "{file_name}""')



# The following isa just for debugging
# Remove once the full program is finished
def main():
    print('Start')
    config = read_file('config.txt')
    print(f'The config is: {config}')
    print('End')



if __name__ == "__main__":
    main()


