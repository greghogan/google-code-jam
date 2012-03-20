#!/usr/bin/env python

import operator

def run_one(candy):
    # Sean adds value numerically, but Patrick 'adds' using xor.
    # A nice aspect of xor is that it is reversible (x ^ y ^ x = y).
    #
    # Moving candy from one pile to the other will change the value
    # of each pile by xor'ing with the value of that candy.  This means
    # that the two piles will have equal value only if they start with
    # the same value.
    #
    # Therefore, first compute Patrick's value of all the candy.  If
    # the xor is non-zero, there is no solution.  Otherwise give
    # Patrick the smallest piece and Sean takes the remainder.
    xor = reduce(operator.xor, candy)

    if xor == 0:
        return sum(candy) - min(candy)
    else:
        return "NO"


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of pieces of candy
        N = int(lines.popleft())

        # Candy values
        candy = [int(i) for i in lines.popleft().split(' ')]

        result = run_one(candy)

        output.append('Case #{0}: {1}'.format(t + 1, result))

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
