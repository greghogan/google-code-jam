#!/usr/bin/env python

from collections import defaultdict

def run_one(songs):
    # A single song is matched by the empty string
    if len(songs) == 1:
        return ['""']

    # Compile the set of substrings, and number of words in which each occurs
    substrings = defaultdict(int)

    for song in songs:
        lc = song.lower()
        lsong = len(song)

        # Remove duplicate substrings by storing in a set
        song_substrings = set(lc[x:y] for x in xrange(lsong) for y in range(x+1, lsong+1))

        # Increment substring counts
        for substring in song_substrings:
            substrings[substring] += 1

    # Only consider substrings which are unique
    single_substrings = [s for s, count in substrings.iteritems() if count == 1]

    # Sort substrings first by length, then lexicographically
    single_substrings.sort(key=lambda s: (len(s), s))

    searches = []

    for song in songs:
        lc = song.lower()

        # Find the first matching substring
        for substring in single_substrings:
            if substring in lc:
                searches.append('"' + substring.upper() + '"')
                break
        else:
            # No substrings match
            searches.append(':(')

    return searches


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of songs
        N = int(lines.popleft())

        songs = [lines.popleft().rstrip('\r\n') for n in range(N)]

        searches = run_one(songs)

        output.append('Case #{0}:'.format(t + 1))
        output.extend(searches)

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque([line.rstrip('\r\n') for line in file.readlines()])
        output = run(lines)
        print os.linesep.join(output)
