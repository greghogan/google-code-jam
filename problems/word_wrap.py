import sys

if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + ' <file>'
    sys.exit()

infile = sys.argv[1]

with open(infile) as file:
    for line in file.readlines():
        line = line.rstrip('\r\n')

        while len(line) > 80:
            cut = line.rfind(' ', 0, 80)
            if cut < 0:
                print line
                break
            else:
                print line[:cut]
                line = line[cut+1:]
        else:
            print line
