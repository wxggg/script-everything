import os

def dir_each_file(dpath):
    for f in os.listdir(dpath):
        print(f)

def file_each_line(fname):
    with open(fname) as f:
        for line in f:
            print(line)

file_each_line('./test.csv')