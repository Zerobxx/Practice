import sys
import random

def construct_data(filename):
    f = open(filename, 'w')
    for i in range(40):
        data = 'name_' + str(i) + ':' + str(random.randint(50, 100)) + '\n'
        f.write(data)
    f.close()

def create_file(file_list):
    for file in file_list:
        construct_data(file)

if __name__ == '__main__':
    print sys.argv[1:]
    create_file(sys.argv[1:])