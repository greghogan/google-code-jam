#!/usr/bin/env python

import glob
import os
import sys
from collections import deque
from difflib import context_diff

contests = {
    '2008 Practice Contests':
        {'practice problems': ['Alien Numbers']},
    '2008':
        {'round 1a': ['Minimum Scalar Product']},
    '2009':
        {'qualification round': ['Alien Language'],
         'round 1c': ['All Your Base']},
    '2010 Africa':
        {'qualification round': ['Store Credit', 'Reverse Words', 'T9 Spelling']}
}


def problems_path():
    script_path = os.path.abspath( __file__ )
    script_base = os.path.basename(script_path)

    return os.path.join(script_base, '../problems')


def diff(a, b, filename):
    lines = list(context_diff(a, b, fromfile=filename, tofile='program'))
    if len(lines):
        print os.linesep.join(lines)
    else:
        print 'Success!  (' + filename + ')'


def execute_program(program, infile, outfile=None):
    if not os.path.isfile(infile):
        raise Exception('File ' + infile + ' does not exist!')

    prog_out = []
    with open(infile) as file:
        lines = deque(file.readlines())
        prog_out.extend(program.run(lines))

    if outfile and os.path.isfile(outfile):
        with open(outfile) as file:
            file_out = [line.rstrip('\r\n') for line in file.readlines()]
            diff(file_out, prog_out, os.path.basename(outfile))
    else:
        print os.path.basename(infile)
        print '=' * len(os.path.basename(infile))
        print os.linesep.join(prog_out)
        print


def run_program(contest_name, round_name, program):
    program_name = program.__name__.split('.')[-1].replace('_', ' ')
    io = os.path.join(problems_path(), contest_name, round_name, program_name, 'io')

    for infile in glob.glob(io + '/*.in'):
        outfile = infile[:-3] + '.out'
        execute_program(program, infile, outfile)


def run_programs(programs_to_run=None):
    for contest_name, round in contests.iteritems():
        for round_name, programs in round.iteritems():
            for program_name in programs:
                if programs_to_run and program_name not in programs_to_run:
                    continue

                print program_name

                module_name = 'python.' + program_name.replace(' ', '_').lower()
                __import__(module_name)
                program = sys.modules[module_name]

                run_program(contest_name, round_name, program)


if __name__ == '__main__':
    run_programs(sys.argv[1:])
