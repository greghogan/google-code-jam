#!/usr/bin/env python

import string

# Find the mapping from the problem statement and sample input and output
known_phrases = [ # from the problem statement
                 ('a zoo',
                  'y qee'),
                  # from the problem sample
                 ('ejp mysljylc kd kxveddknmc re jsicpdrysi',
                  'our language is impossible to understand'),
                 ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                  'there are twenty six factorial possibilities'),
                 ('de kr kd eoya kw aej tysr re ujdr lkgc jv',
                  'so it is okay if you want to just give up')]

mapping = {}
for googlerese, english in known_phrases:
    mapping.update(zip(googlerese, english))

# One letter pair is missing, so locate the missing letters
letters = set(string.ascii_lowercase)

missing_english = (letters - set(mapping.keys())).pop()
missing_googlerese = (letters - set(mapping.values())).pop()

mapping[missing_english] = missing_googlerese


def run_one(googlerese):
    # Substitute each Googlerese letter with the English equivalent
    english_letters = [mapping[letter] for letter in googlerese]

    return ''.join(english_letters)


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        googlerese = lines.popleft().rstrip('\r\n')

        english = run_one(googlerese)

        output.append('Case #{0}: {1}'.format(t + 1, english))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
