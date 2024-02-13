# File: lab2_functions.py
import sys

def print_arguments():
    print("Script name:", sys.argv[0])
    print("Arguments passed:", sys.argv[1:])

# Test the function
if __name__ == "__main__":
    print_arguments()
