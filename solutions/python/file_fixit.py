#!/usr/bin/env python

def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # N: number of existing directories
        # M: number of directories to be created
        N, M = [int(x) for x in lines.popleft().split()]

        # Existing directories
        existing = set()
        for n in range(N):
            existing.add(lines.popleft().rstrip('\r\n'))

        # New directories (and parent directories)
        creating = set()
        for m in range(M):
            full_path = lines.popleft().strip('\r\n')

            directory = ''
            # Split on '/' (first removing the leading slash)
            for part in full_path[1:].split('/'):
                directory += '/' + part
                creating.add(directory)

        # Remove existing directories and count
        count = len(creating - existing)

        output.append('Case #{0}: {1}'.format(t + 1, count))

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
