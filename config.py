class Config:
    def __init__(self, file):
        file_info = read_file(file)




def read_file(file_name):
    try:
        file = open(file_name, 'r')
        file.close()
    except:
        # Make this give more detail about the problem
        # Give more types of excepts to catch differnt errors
        print('Unable to open file')