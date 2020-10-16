#!/usr/bin/env python3

import sys
import argparse

def commands():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--string", "-s",
        help="Specific string to search for.",
        action="store",
        type=str,
    )

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()
    
    return args

def checkString():
    print("Checking for string now...")
    
    for lineNum, line in enumerate(sys.stdin.readlines()):
        line = line.strip("\n")
        
        if commands().string == line:
            print("String is in file.")
            print(f"String exists on line {lineNum}")
            sys.exit(0)

        lineNum+=1

    # If line is not found
    print("String was not found in file.")

def main():
    checkString()

if __name__ == "__main__":
    main()
