#!/usr/bin/env python

def run_one(W, B):
    # The possible outcomes for each draw and replacement
    #   remove W and W, add W => -1 W
    #   remove W and B, add W => -1 W
    #   remove B and B, add W => +1 W, -2 B
    # Since B can only be removed two at a time, the last ball
    # will be B if and only if we start with an odd number of B
    if B & 1 == 1:
        return 'BLACK'
    else:
        return 'WHITE'


def run(lines):
    output = []

    # Number of test cases
    N = int(lines.popleft())
    for n in range(N):
        W, B = [int(x) for x in lines.popleft().split()]

        last_ball = run_one(W, B)

        output.append('Case #{0}: {1}'.format(n + 1, last_ball))

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
