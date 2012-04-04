#!/usr/bin/env python

def run_one(follows):
    # Each monk whispers the words
    counts = [1] * len(follows)

    # Sum the number of monks directly following each monk
    followers = [0] * len(follows)
    for monk in follows:
        followers[monk] += 1

    # Some monks follow each other in a cycle (ie., 1 -> 2 -> 3 -> 1);
    # this loop processes all monks which are not in a cycle
    for monk in [idx for idx, count in enumerate(followers) if count == 0]:
        # Recursively remove each monk with zero followers, updating counts
        # and followers; for the monks (1, 2 -> 3 -> 4), M1 increments the
        # count of M3, then on the next iteration M2 increments M3 and
        # M3 increments M4 by two; counts is then [1, 1, 2, 3]
        while followers[monk] == 0:
            counts[follows[monk]] += counts[monk]

            monk = follows[monk]
            followers[monk] -= 1

    # Process the monks which are in cycles; there may be multiple cycles
    for monk, count in enumerate(followers):
        # A follower exists
        if count == 1:
            # Find all monks in this cycle; since every monk in the cycle
            # will hear the words from any other monk in the cycle, every
            # monk which has been counted will also hear the words
            cycle = []
            cycle_count = 0
            while monk not in cycle:
                cycle.append(monk)
                cycle_count += counts[monk]
                monk = follows[monk]

            # Update the count for every monk in the cycle
            for monk in cycle:
                counts[monk] = cycle_count
                followers[monk] = 0

    return counts


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of monks
        N = int(lines.popleft())

        # Each monk follows one other monk; convert to zero-index
        follows = [int(F) - 1 for F in lines.popleft().split()]

        counts = run_one(follows)

        output.append('Case #{0}:'.format(t + 1))
        output.extend([str(x) for x in counts])

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
