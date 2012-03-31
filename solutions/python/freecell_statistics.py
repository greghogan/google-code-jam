#!/usr/bin/env python

from collections import defaultdict

def run_one(N, PD, PG):
    # If all games have been won, then every game today must have been won
    if PG == 100 and PD != 100:
        return False

    # If all games have been lost, then every game today must have been lost
    if PG == 0 and PD != 0:
        return False

    # For any overall percentage 1 <= PG <= 99, any daily percentage PD is valid;
    # however, we must check that PD is valid for the given N

    # Check whether some number of games played, 1 <= n <= N, would have an integer
    # number of games won (and therefore a valid solution).  If a solution cannot
    # be found for N <= 100, no solution exists for N > 100.
    for i in range(1, min(N, 100) + 1):
        if i * PD % 100 == 0:
            return True

    return False


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of teams
        N, PD, PG = [int(i) for i in lines.popleft().split(' ')]

        possible = run_one(N, PD, PG)

        output.append('Case #{0}: {1}'.format(t + 1, 'Possible' if possible else 'Broken'))

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
