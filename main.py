# -*- coding: utf-8 -*-

import bubble
import insertion
import merge
import quick
import selection
import argparse
import sys

def main():
    numbers = []
    if (len(sys.argv) == 1):
        for line in sys.stdin:
            line = line.strip('\n')
            numbers = line.split(' ')
            numbers = [float(i) for i in numbers]
    else:
        CLI = argparse.ArgumentParser()
        CLI.add_argument(
            "numbers",
            nargs='*',
            type=float,
            default=None,
        )
        args = CLI.parse_args()
        numbers = args.numbers
    """
    print('Loading numbers...')
    bubble.sort(numbers.copy())
    print('\nLoading numbers...')
    merge.sort(numbers.copy())
    print('\nLoading numbers...')
    insertion.sort(numbers.copy())
    print('\nLoading numbers...')
    """
    quick.sort(numbers.copy())
    """
    print('\nLoading numbers...')
    selection.sort(numbers.copy())
    """
    
if __name__ == "__main__":
    main()
