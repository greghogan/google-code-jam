#!/usr/bin/env python

from collections import defaultdict

def run_one(combine, oppose, invoke):
    # Maintain nest dictionary of element pairs
    # and the element they combine to
    combine_dict = defaultdict(dict)

    for string in combine:
        e1, e2, e3 = list(string)

        combine_dict[e1][e2] = e3
        combine_dict[e2][e1] = e3

    # Maintain a list of elements and the elements
    # they oppose
    oppose_dict = defaultdict(list)

    for string in oppose:
        e1, e2 = list(string)

        oppose_dict[e1].append(e2)
        oppose_dict[e2].append(e1)

    residue = []

    # Invoke each element
    for element in list(invoke):
        # If the list is empty add the element
        if len(residue) == 0:
            residue.append(element)
        else:
            last = residue[-1]
            # Compare with the last element and combine if possible
            if last in combine_dict[element]:
                # Remove the last element and add the new element
                residue.pop()
                residue.append(combine_dict[element][last])
            # If the elements could not combine, check for opposing elements
            else:
                for other_element in oppose_dict[element]:
                    if other_element in residue:
                        # Reset if opposed to element in list
                        del residue[:]
                        break
                else:
                    # Append the element if no combination or opposition
                    residue.append(element)

    return residue


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        items = lines.popleft().split(' ')

        # Number of combine strings
        C = int(items.pop(0))

        combine = items[0:C]
        del items[0:C]

        # Number of oppose strings
        D = int(items.pop(0))

        oppose = items[0:D]
        del items[0:D]

        # Number of elements in invocation string
        N = int(items.pop(0))

        invoke = items[0].strip()

        # Compute the remaining elements after invocation
        residue = run_one(combine, oppose, invoke)

        output.append('Case #{0}: [{1}]'.format(t + 1, ', '.join(residue)))

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
