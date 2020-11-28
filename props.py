#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-11-28
Purpose: Rock the Casbah
"""

import argparse

import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    line = args.positional

#    print(f'line = "{str_arg}"')
    
    print(f'input is {line}')
    matches=re.findall(r'(\${.+})',line) 
    print(matches)

    matches2=replaceDollar(matches[0])
  
    print('output:'+re.sub(matches2, 'aap',line))
    
def replaceDollar(input):
    return ''.join(['\\$' if n=='$' else n for n in input])

def test_dollar():
    assert 'a\\$b' == replaceDollar('a$b')
# --------------------------------------------------
if __name__ == '__main__':
    main()
