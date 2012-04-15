#!/usr/bin/env python

def run_one(A, B):
    # For each number m in the range [A, B), find each recycled number n by a
    # base-10 shift.  Compare against the constraint A <= m < n <= B.  Store
    # results in a set to prevent counting of duplicates.

    recycled = set()

    # Precompute values outside of the loop
    digits = len(str(A))
    digit_range = range(digits - 1)
    power = 10 ** (digits - 1)

    for m in range(A, B):
        n = m
        for i in digit_range:
            # Single digit base-10 circular right shift
            n = power * (n % 10) + n / 10

            # Verify ordering and problem constraint
            if m < n and n <= B:
                recycled.add((m, n))

    return len(recycled)


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        A, B = [int(x) for x in lines.popleft().split()]

        recycled_count = run_one(A, B)

        output.append('Case #{0}: {1}'.format(t + 1, recycled_count))

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
