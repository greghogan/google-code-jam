#!/usr/bin/env python

import re

# There may be multiple interpretations of a spell. The simplest interpretation
# is that the first and last words contain exactly two vowels, and these two
# vowels start and end the word. Neighboring consonants and extra vowels are
# part of the gibberish at the beginning or end, or to the word in the middle.
detector = re.compile(r'([aeiou][^aeiou]*[aeiou])[^aeiou]*[aeiou].*\1')

def run_one(spell):
    # re.search returns an object; use the double negative to return a boolean
    return not not re.search(detector, spell)


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        spell = lines.popleft().rstrip('\r\n')

        is_valid = run_one(spell)

        output.append('Case #{0}: {1}'.format(t + 1, 'Spell!' if is_valid else 'Nothing.'))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque([line.rstrip('\r\n') for line in file.readlines()])
        output = run(lines)
        print os.linesep.join(output)
