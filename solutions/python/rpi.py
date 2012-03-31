#!/usr/bin/env python

from collections import defaultdict

def run_one(teams, schedule):
    # Count number of wins and games played for each team
    wins = [0] * teams
    played = [0] * teams

    # Store result of games in a nested dictionary
    games = defaultdict(dict)

    for i, row in enumerate(schedule):
        for j, game in enumerate(row):
            # 1 = win, 0 = loss, . = teams did not play
            if game != '.':
                result = int(game)
                games[i][j] = result
                if result:
                    wins[i] += 1
                played[i] += 1

    # Compute winning percentage for each team
    wp = [float(wins[x])/(played[x]) for x in range(teams)]

    # Compute opponents winning percentage for each team
    owp = []

    # OWP is the average WP of a team's opponent when games between
    # that team and opponent are ignored
    for team in range(teams):
        sum = 0.0
        for opp in games[team].iterkeys():
            if games[team][opp]:
                # team won, opp lost
                sum += float(wins[opp]) / (played[opp] - 1)
            else:
                # team lost, opp won
                sum += float(wins[opp] - 1) / (played[opp] - 1)
        owp.append(sum/len(games[team]))

    # Compute opponents opponents winning percentage for each team
    oowp = []

    # OOWP is the mean of OWP of a team's opponents
    for team in range(teams):
        sum = 0.0
        for opp in games[team].iterkeys():
            sum += owp[opp]
        oowp.append(sum/len(games[team]))

    # Compute rpi for each team
    rpi = [0.25 * wp[x] + 0.50 * owp[x] + 0.25 * oowp[x] for x in range(teams)]

    return rpi


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of teams
        N = int(lines.popleft())

        schedule = [lines.popleft() for n in range(N)]

        rpi_list = run_one(N, schedule)

        output.append('Case #{0}:'.format(t + 1))
        for rpi in rpi_list:
            output.append(str(rpi))

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
