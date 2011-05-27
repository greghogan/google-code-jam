def run(lines):
    output = []

    # Number of test cases
    N = int(lines.popleft())
    for n in range(N):
        words = lines.popleft().split()
        words.reverse()

        output.append('Case #{0}: {1}'.format(n + 1, ' '.join(words)))

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
