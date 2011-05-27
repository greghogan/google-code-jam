#!/usr/bin/env python

# Assign smaller values to digits at the beginning of the number
# - the number abcdefghij would map to values 1023456789
# No leading 0, so swap 0 and 1; maximum 36 digits (a-z, 0-9)
digit_order = [1, 0] + range(2, 36)

def run_one(word):
    # Find the value of each digit
    digit_map = {}
    for c in word:
        if c not in digit_map:
            # Lookup values from digit_order in order
            digit_map[c] = digit_order[len(digit_map)]

    base = len(digit_map)
    # "they aren't using unary (base 1)"
    if base == 1:
        base = 2

    minimum = 0
    multiplier = 1
    # Iterate through word right-to-left
    for c in word[::-1]:
        # Add the value of each digit
        minimum += digit_map[c] * multiplier
        multiplier *= base

    return minimum


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Alien number of unknown base and digits
        word = lines.popleft().rstrip('\r\n')

        minimum = run_one(word)

        output.append('Case #{0}: {1}'.format(t + 1, minimum))

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
