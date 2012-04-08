#!/usr/bin/env python

def run_one(invitations):
    solo = set()

    for invitation in invitations:
        # Track whether an invitation has been seen once or twice;
        # if the second time remove the invitation
        if invitation in solo:
            solo.remove(invitation)
        else:
            solo.add(invitation)

    # The only remaining invitation is for the one solo guest
    return solo.pop()


def run(lines):
    output = []

    # Number of test cases
    N = int(lines.popleft())
    for n in range(N):
        # Number of guests
        G = int(lines.popleft())
        invitations = [int(x) for x in lines.popleft().split()]

        solo = run_one(invitations)

        output.append('Case #{0}: {1}'.format(n + 1, solo))

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
