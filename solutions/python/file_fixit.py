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
        directories = set()
        for n in range(N):
            directories.add(lines.popleft().rstrip('\r\n'))

        # Count each directory which must be created
        count = 0
        for m in range(M):
            directory = lines.popleft().strip('\r\n')

            # Check whether each directory in the path exists
            subdirectory = ''
            for part in directory[1:].split('/'):
                subdirectory += '/' + part
                if subdirectory not in directories:
                    # Add newly created directories to the set
                    directories.add(subdirectory)
                    count += 1

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
