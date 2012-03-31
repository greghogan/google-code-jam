#!/usr/bin/env python

from collections import defaultdict

def run_one(buttons):
    # Store last time and position for each robot,
    # robots start at time 0 and door 1
    robots = defaultdict(lambda: [0, 1])

    # Accumulate the time to press the buttons
    time = 0

    for color, door in buttons:
        last_time, last_door = robots[color]

        # Compute the time at which this robot would arrive
        # at the button
        distance = abs(door - last_door)
        arrival = last_time + distance

        # Robots may travel at the same time, but must press
        # buttons in order
        if arrival > time:
            time = arrival

        # One second required to push the button
        time += 1

        # Store the robot time and location
        robots[color] = [time, door]

    return time


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        items = lines.popleft().split(' ')

        # Number of buttons to be pressed
        N = int(items.pop(0))

        # Store (robot, door) pairs in a list
        buttons = zip(items[0::2], map(int, items[1::2]))

        time = run_one(buttons)

        output.append('Case #{0}: {1}'.format(t + 1, time))

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
