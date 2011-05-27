#!/usr/bin/env python

from operator import itemgetter

def run_one(wires):
    # Sorting by A (the left height) permits cutting the search
    # space and number of comparisons in half (only B is compared)
    wires.sort(key=itemgetter(0))

    intersections = 0
    # For each wire ...
    for i in range(len(wires)):
        # ... look for wires with a larger A ...
        for j in range(i + 1, len(wires)):
            # ... and a smaller B ...
            if wires[i][1] > wires[j][1]:
                # ... which must intersect
                intersections += 1

    return intersections


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of wires
        N = int(lines.popleft())

        # Load in each of the window height (A, B) tuples
        wires = []
        for n in range(N):
            a, b = [int(x) for x in lines.popleft().split()]
            wires.append((a, b))

        intersections = run_one(wires)

        output.append('Case #{0}: {1}'.format(t + 1, intersections))

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
