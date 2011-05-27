# Manual define character mapping as some keys match four letters
code_map = { 'a': '2', 'b': '22', 'c': '222',
             'd': '3', 'e': '33', 'f': '333',
             'g': '4', 'h': '44', 'i': '444',
             'j': '5', 'k': '55', 'l': '555',
             'm': '6', 'n': '66', 'o': '666',
             'p': '7', 'q': '77', 'r': '777', 's': '7777',
             't': '8', 'u': '88', 'v': '888',
             'w': '9', 'x': '99', 'y': '999', 'z': '9999',
             ' ': '0' }


def run_one(text):
    codes = []

    last_char = ''
    for char in text:
        # For each character of input, lookup the output sequence
        code = code_map[char]

        # In the case where consecutive input characters map to the
        # same ouput character, output a space (representating a pause)
        if last_char == code[0]:
            codes.append(' ')
        last_char = code[-1]

        codes.append(code)

    return ''.join(codes)



def run(lines):
    output = []

    # Number of test cases
    N = int(lines.popleft())
    for n in range(N):
        # Remove line terminators
        text = lines.popleft().rstrip('\r\n')

        coded_text = run_one(text)

        output.append('Case #{0}: {1}'.format(n + 1, coded_text))

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
