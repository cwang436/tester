import argparse
import random

def sample_lines(filename):
    with open(filename) as file:
        linelist = file.readlines()
    sample = [x for x in linelist if random.random() < 0.01]
    for i in sample:
        print(i, end='')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()    
    sample_lines(args.filename)

if __name__ == "__main__":
    main()
