#!/usr/bin/env python

# When two items are unsorted, GoroSort requires an expected 2 hits to sort
# the items, since the two items will be sorted or remain unsorted with equal
# probability.  When three items are unsorted, the probabilities are:
#   1/6 that all three items are sorted
#   3/6 that one item is sorted and two remain unsorted
#   2/6 that all three items remain unsorted
#   (it is not possible to leave a single item unsorted)
# We can thus solve for three items using recursion as below, since we know
# the expected number of hits for two items.
#
# After solving for four items, the pattern emerges that the expected number of
# hits is equal to the number of unsorted items.
#
# 2 => 1/2 = 1
#      1/2 = 1 + n
#
# n = (2 + n)/2 = 2
#
# 3 => 1/6 = 1
#      3/6 = 1 + 2
#      2/6 = 1 + n
#
# n = (12 + 2n)/6 = 3
#
# 4 => 1/24 = 1
#      6/24 = 1 + 2
#      8/24 = 1 + 3
#      9/24 = 1 + n
#
# n = (60 + 9n)/24 = 4
#
# The following code prints the distribution of sorted items for all
# permutations for a given number of items.
#
#import collections
#import itertools
#import operator
## Perform calculations for 2+ unsorted items
#for i in range(2, 5):
#    # For each permutation of items after Goro hits the table,
#    # calculate the number of sorted items
#    items = list(range(i))
#    data = collections.defaultdict(int)
#    for mixed in itertools.permutations(items):
#        # Find the number of items that were sorted for this permutation
#        num_sorted = list(itertools.imap(operator.__sub__, items, mixed)).count(0)
#        data[num_sorted] += 1
#    print data
def run_one(elements):
    hits = 0

    # Count the number of unsorted items.  As described above, the expected
    # number of hits equals the number of unsorted items
    for index, element in enumerate(elements, start=1):
        if index != element:
            hits += 1

    return hits


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of elements
        N = int(lines.popleft())

        elements = [int(x) for x in lines.popleft().split(' ')]

        operations = run_one(elements)

        output.append('Case #{0}: {1:f}'.format(t + 1, operations))

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
