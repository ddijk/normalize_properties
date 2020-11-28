#!/usr/bin/env python3

import os
import random
from subprocess import getoutput

prg = './props.py'

def test_take():
    """leading consonant"""

    out = getoutput(f'{prg} take').splitlines()
    assert out[0] == 'bake'

# --------------------------------------------------
def test_chair():
    """consonant cluster"""

    out = getoutput(f'{prg} chair').splitlines()
    assert len(out) == 56
    assert out[1] == 'blair'
    assert out[-2] == 'yair'


