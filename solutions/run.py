#!/usr/bin/env python

import glob
import os
import sys
from collections import deque
from difflib import context_diff

from python import alien_numbers
from python import store_credit, reverse_words, t9_spelling

contests = {
    '2010 Africa':
        {'qualification round': [store_credit, reverse_words, t9_spelling]},
    '2008 Practice Contests':
        {'practice problems': [alien_numbers]}
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


if __name__ == '__main__':
    for contest_name, round in contests.iteritems():
        for round_name, programs in round.iteritems():
            for program in programs:
                print "Running " + program.__name__
                run_program(contest_name, round_name, program)
