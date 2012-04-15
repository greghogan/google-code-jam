#!/usr/bin/env python

def run_one(S, p, points):
    # To achieve an unsurprising best score of P, a dancer's scores must have
    # been at least (P, P-1, P-1) = 3 * P - 2.  A surprising best score of P
    # could be achieved with (P, P-2, P-2) = 3 * P - 4.

    # Hard code the following cases, as this algorithm fails when p = 1 and the
    # dancer's score is zero.  Negative scores are not possible, and (1, 0, -1)
    # is invalid.
    if p == 0:
        # Since zero is the minimum score, all dancers are counted
        return len(points)
    elif p == 1:
        # Any dancer with a non-zero total has a best of at least one
        return len(points) - points.count(0)

    unsurprising = 0
    needs_surprise = 0

    for score in points:
        if score >= 3 * p - 2:
            unsurprising += 1
        elif score >= 3 * p - 4:
            needs_surprise += 1

    # Limit the number of unsurprising scores to S
    return unsurprising + min(S, needs_surprise)


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        line = [int(x) for x in lines.popleft().split()]

        # Number of dancing Googlers, maximum number of surprising scores,
        # minimum 'best' score, and individual dancer total scores
        N, S, p, points = line[0], line[1], line[2], line[3:]

        max_googlers = run_one(S, p, points)

        output.append('Case #{0}: {1}'.format(t + 1, max_googlers))

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
