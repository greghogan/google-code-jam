#!/usr/bin/env python

import re

# Convert an alien pattern of the form '(ab)d(dc)'
# to a regular expression of the form '(a|b)d(d|c)'
def pattern_to_regex(pattern):
    regex_parts = []

    # Split the alien pattern and enumerate on the list.  The ordering of
    # the matched items is well defined.  From the re.split() documentation:
    #   "If there are capturing groups in the separator and it matches at the
    #   start of the string, the result will start with an empty string."
    chunks = re.split('[(|)]', pattern)

    for i, chunk in enumerate(chunks):
        if i % 2 == 0:
            # Copy the letters outside parenthesis
            regex_parts.append(chunk)
        else:
            # Inject a bar between letters within the parenthesis
            with_bar = '|'.join(list(chunk))
            regex_parts.append('(' + with_bar + ')')

    regex = ''.join(regex_parts)
    return re.compile(regex)


def run_one(words, pattern):
    regex = pattern_to_regex(pattern)

    # ... and count the words the regex matches against
    count = 0
    for word in words:
        if regex.match(word):
            count += 1

    return count


def run(lines):
    output = []

    # L: word length
    # D: number of words in alien language
    # N: number of patterns to match against words
    L, D, N = [int(x) for x in lines.popleft().split(' ')]

    # Read in the alien words
    words = []
    for d in range(D):
        words.append(lines.popleft())

    for n in range(N):
        # For each alien pattern, create a compiled regular expression ...
        pattern = lines.popleft()
        count = run_one(words, pattern)

        output.append('Case #{0}: {1}'.format(n + 1, count))

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
