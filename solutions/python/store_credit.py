#!/usr/bin/env python

# Notes:
# - the problem guarantees there will be one and only one solution pair
# - the answer is the index of the item not the price
def run_one(credits, prices):
    # Store the index with the value in a tuple
    items = list(enumerate(prices))
    # Sort on the value
    items.sort(key=lambda item: item[1])

    # Left and right list indices
    x = 0
    y = len(items) - 1

    # Each iteration, add the smallest and largest values
    # - if the sum is too small, reject the smallest value
    # - if the sum is too large, reject the largest value
    while x != y:
        cost = items[x][1] + items[y][1]
        if cost < credits:
            # Reject the smallest (leftmost) value
            x += 1
        elif cost > credits:
            # Reject the largest (rightmost) value
            y -= 1
        else:
            # Solution found
            indexes = [items[x][0], items[y][0]]
            indexes.sort()

            return (indexes[0], indexes[1])


def run(lines):
    output = []

    # Number of test cases
    N = int(lines.popleft())
    for n in range(N):
        # Credits
        C = int(lines.popleft())
        # Number of items
        I = int(lines.popleft())
        # Prices of items
        P = lines.popleft()

        prices = [int(p) for p in P.split()]

        indexes = run_one(C, prices)

        # Count case number and indexes starting at index 1
        output.append('Case #{0}: {1} {2}'.format(n + 1, indexes[0] + 1, indexes[1] + 1))

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
