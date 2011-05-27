def run_one(v1, v2):
    # The minimum scalar product is when the largest value from each
    # vector is multiplied by the smallest value from the other vector
    v1.sort()
    v2.sort(reverse=True)

    # Compute the scalar (dot) product
    scalar_product = sum([i1 * i2 for i1, i2 in zip(v1, v2)])

    return scalar_product


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Length of scalar vectors
        n = int(lines.popleft())
        # Read vectors and convert strings to integers
        v1 = map(int, lines.popleft().split())
        v2 = map(int, lines.popleft().split())

        scalar_product = run_one(v1, v2)

        output.append('Case #{0}: {1}'.format(t + 1, scalar_product))

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
