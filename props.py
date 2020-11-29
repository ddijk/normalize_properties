#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-11-28
Purpose: Normalize properties file with parameters of type ${my_param}
"""

import argparse

import re
import os
import copy


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
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

    print(normalizeAll(bestand))


def normalizeAll(propertiesFile):
    dict = {}
    for regel in propertiesFile:
        k, v = regel.strip().split('=')
        dict[k] = v

    return normalize(dict)


def normalize(dict):
    result = copy.deepcopy(dict)
    for k in dict:
        result[k] = replace(dict[k], dict)

    if result == dict:
        return result
    else:
        return normalize(result)


def replace(value, dict):
    pattern = re.compile(r'\${(.+?)}')
    match = re.search(pattern, value)
    if match:
        replacee = escape_dollar(match.group(0))
        return re.sub(replacee, dict[match.group(1)], value)
    else:
        return value


def escape_dollar(input):
    return ''.join(['\\$' if n == '$' else n for n in input])


# --------------------------------------------------
if __name__ == '__main__':
    main()
