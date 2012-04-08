#!/usr/bin/env python

def run_one(N, K):
    # The chain of snappers respond to the snaps as a binary count;
    # the number of snappers act as a bitmask on the count
    mask = (2 ** N - 1)

    # Determine if all snappers are on
    if K & mask == mask:
        return 'ON'
    else:
        return 'OFF'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        N, K = [int(x) for x in lines.popleft().split()]

        on_or_off = run_one(N, K)

        output.append('Case #{0}: {1}'.format(t + 1, on_or_off))

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
