#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bubble
import insertion
import merge
import quick
import selection
import argparse

def main():
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "numbers",
        nargs='*',
        type=float,
        default=None,
    )
    args = CLI.parse_args()
    
    print('Loading numbers...')
    bubble.sort(args.numbers.copy())
    print('\nLoading numbers...')
    merge.sort(args.numbers.copy())
    print('\nLoading numbers...')
    insertion.sort(args.numbers.copy())
    print('\nLoading numbers...')
    quick.sort(args.numbers.copy())
    print('\nLoading numbers...')
    selection.sort(args.numbers.copy())
    
if __name__ == "__main__":
    main()
