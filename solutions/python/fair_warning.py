#!/usr/bin/env python

from fractions import gcd

def run_one(slarboseconds):
    # Find T, the GCD of the set of slarboseconds
    slarboseconds.sort()

    gaps = [slarboseconds[i] - slarboseconds[i-1] for i in range(1, len(slarboseconds))]

    divisor = reduce(gcd, gaps)

    # Find the time until the optimum anniversary
    optimum_anniversary = -slarboseconds[0] % divisor

    return optimum_anniversary


def run(lines):
    output = []

    # Number of test cases
    C = int(lines.popleft())
    for c in range(C):
        line = [int(x) for x in lines.popleft().split()]
        count, slarboseconds = line[0], line[1:]

        apocalypse = run_one(slarboseconds)

        output.append('Case #{0}: {1}'.format(c + 1, apocalypse))

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
