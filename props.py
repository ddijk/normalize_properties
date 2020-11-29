#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-11-28
Purpose: Rock the Casbah
"""

import argparse

import re
import os
import copy


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Normalize Properties file """

    args = get_args()
    bestand = args.file

    dict = {}
    for regel in bestand:
        k, v = regel.strip().split('=')
        dict[k]=v

    # print(dict)

    result = normalize(dict)

    print(result)


def normalize(dict):
    # print("---- start normalize")
    result = copy.deepcopy(dict)
    for k in dict:
        result[k]=replace(dict[k], dict)

        # print(f'key={k} en val={v}')
    # print(dict) 
    # print(result) 
    # print('-----')
    if result==dict:
        return result
    else:
        return normalize(result)
    # print("---- end normalize")

def replace(value, dict):    
    pattern =re.compile(r'\${(.+?)}')
    match=re.search(pattern, value) 
    # print(match)
    if match:
        # print(f'match op {match.group(0)}')
        # print(f'var is {match.group(1)}')
        replacee=escape_dollar(match.group(0))
        return re.sub(replacee, dict[match.group(1)],value)
    else:
        return value
    
def escape_dollar(input):
    return ''.join(['\\$' if n=='$' else n for n in input])



# --------------------------------------------------
if __name__ == '__main__':
    main()
