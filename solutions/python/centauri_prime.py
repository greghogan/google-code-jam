#!/usr/bin/env python

def run_one(C):
    # The kind of ruler can be deduced from the last letter of the country name
    if C[-1].lower() == 'y':
        return 'nobody'
    elif C[-1].lower() in 'aeiou':
        return 'a queen'
    else:
        return 'a king'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Country
        C = lines.popleft().rstrip('\r\n')

        ruler = run_one(C)

        output.append('Case #{0}: {1} is ruled by {2}.'.format(t + 1, C, ruler))

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
