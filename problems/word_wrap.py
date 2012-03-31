#!/usr/bin/env python

import os
import sys

if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + ' <input file> [<output file>]'
    sys.exit()

infile = sys.argv[1]

lines = []
with open(infile) as file:
    for line in file.readlines():
        line = line.rstrip('\r\n')

        while len(line) > 80:
            cut = line.rfind(' ', 0, 80)
            if cut < 0:
                lines.append(line)
                break
            else:
                lines.append(line[:cut])
                line = line[cut+1:]
        else:
            lines.append(line)

output = os.linesep.join(lines)

outfile = sys.argv[2] if len(sys.argv) > 2 else infile

with open(outfile, 'w') as file:
    file.write(output)
