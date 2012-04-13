#!/usr/bin/env python

import glob
import os
import sys
from collections import deque
from difflib import context_diff

contests = {
    '2008 Practice Contests':
        {'practice problems': ['Alien Numbers'],
         'practice contest': ['Old Magician']},
    '2008':
        {'round 1a': ['Minimum Scalar Product']},
    '2009':
        {'qualification round': ['Alien Language'],
         'round 1c': ['All Your Base']},
    '2010 Africa':
        {'qualification round': ['Store Credit', 'Reverse Words', 'T9 Spelling'],
         'online competition': ['Odd Man Out', 'Get To Work', 'Qualification Round']},
    '2010':
        {'qualification round': ['Snapper Chain', 'Fair Warning'],
         'round 1b': ['File Fix-It'],
         'round 1c': ['Rope Intranet']},
    '2011 EuroPython':
        ['Centauri Prime', 'Music Collection', 'Irregular Expressions', 'Twibet'],
    '2011':
        {'qualification round': ['Bot Trust', 'Magicka', 'Candy Splitting', 'GoroSort'],
         'round 1a': ['Freecell Statistics', 'Killer Word'],
         'round 1b': ['RPI']}
}


def problems_path():
    script_path = os.path.abspath(__file__)
    script_base = os.path.dirname(script_path)

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
        lines = deque([line.rstrip('\r\n') for line in file.readlines()])
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


def run_program(program_directory, program_name, program_inputs_to_run):
    print program_name

    io = os.path.join(program_directory, 'io').lower()

    module_name = 'python.' + program_name.replace(' ', '_').replace('-', '').lower()
    __import__(module_name)
    program = sys.modules[module_name]

    for infile in glob.glob(io + '/*.in'):
        if program_inputs_to_run and infile.split('/')[-1] not in program_inputs_to_run:
            continue
        outfile = infile[:-3] + '.out'
        execute_program(program, infile, outfile)


def run_programs(contest_directory, contests, programs_to_run=None, program_inputs_to_run=None):
    if type(contests) is list:
        for program_name in contests:
            if programs_to_run and program_name not in programs_to_run:
                continue
            program_directory = os.path.join(contest_directory, program_name)
            run_program(program_directory, program_name, program_inputs_to_run)
    else:
        for contest_name, contests in contests.iteritems():
            directory = os.path.join(contest_directory, contest_name)
            run_programs(directory, contests, programs_to_run, program_inputs_to_run)


if __name__ == '__main__':
    program_to_run = sys.argv[1:2] or None
    program_inputs_to_run = sys.argv[2:] or None

    run_programs(problems_path(), contests, program_to_run, program_inputs_to_run)
