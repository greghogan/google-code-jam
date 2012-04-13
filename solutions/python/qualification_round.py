#!/usr/bin/env python

def run_one(C, problems):
    # A maximum bound on the number of advancing contestants is to sum the
    # number of contestants solving each problem and divide by the number
    # of problems required to be solved.  For example, if C = 2 and
    # solved = [20 9 6], the sum is 35 and a maximum bound is 35 / 2 = 17;
    #
    # A minimum bound is found by sorting the list problems by the number of
    # contestants solving each problem, then taking the C'th value (1-indexed).
    # For C = 2 and solved = [20 9 6], the minimum bound is 9.
    #
    # The minimum bound fails to include contestants solving the extra problems
    # and the maximum bound has contestants solving a single problem multiple
    # times.  The following algorithm maintains a list of length equal to the
    # number of problems required to advance.  The list is pre-populated with
    # the values of the 'C' most solved problems.  The 'extra' problem values
    # are then added to this list, in the way that keeps the list as smooth
    # as possible.  For example, when required = [20 12 8], the value 7 will
    # update the list to [20 14 13].

    # Sort 'required' low to high, and 'extra' high to low
    problems.sort(reverse=True)

    required, extra = problems[:C], problems[C:]
    required.reverse()

    for count in extra:
        # Find the last index which value is not greater than the average of
        # the lesser indexed values plus count
        for idx in range(1, C):
            count += required[idx-1]
            if count <= idx * required[idx]:
                break
        else:
            # The entire list must be averaged
            idx = C
            count += required[-1]

        # Average the values and replace in the list
        div = count / idx
        mod = count % idx

        required[:idx] = [div] * (idx - mod) + [div + 1] * mod

    # Return the smallest value from the list
    return required[0]


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        line = [int(x) for x in lines.popleft().split()]

        # Number of problems, number of problems to advance,
        # and list of number of contestants solving each problem
        P, C, problems = line[0], line[1], line[2:]

        contestants = run_one(C, problems)

        output.append('Case #{0}: {1}'.format(t + 1, contestants))

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
