#!/usr/bin/env python

def run_one(source_number, source_language, target_language):
    # The number of digits in each language (base-10 for Arabic numerals)
    source_base = len(source_language)
    target_base = len(target_language)

    # Convert the source number to base-10 value
    value = 0
    for digit in source_number:
        value = source_base * value + source_language.find(digit)

    # Convert the base-10 value to the target language
    target_number = []
    while value > 0:
        value, remainder = divmod(value, target_base)
        target_number.append(target_language[remainder])

    target_number.reverse()

    return target_number


def run(lines):
    output = []

    # Number of test cases
    N = int(lines.popleft())
    for n in range(N):
        source_number, source_language, target_language = lines.popleft().split()

        target_number = run_one(source_number, source_language, target_language)

        output.append('Case #{0}: {1}'.format(n + 1, ''.join(target_number)))

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
