#!/usr/bin/env python

class Town:
    def __init__(self):
        self.employees = 0
        self.car_capacity = []

    # Track the number of employees living in this town,
    # and the capacity of their vehicles
    def add_employee(self, hometown, car_capacity):
        self.employees += 1
        if car_capacity > 0:
            self.car_capacity.append(car_capacity)


def run_one(N, T, employees):
    towns = [Town() for n in range(N)]

    for hometown, car_capacity in employees:
        towns[hometown].add_employee(hometown, car_capacity)

    cars_driven = []

    for n in range(N):
        # Employees do not commute from the company town, and if there are
        # no employees living in a town there will be no drivers
        if n == T or towns[n].employees == 0:
            cars_driven.append(0)
        else:
            # Sort the cars by capacity, largest to smallest; then find
            # the minimum number of cars in which all employees will fit
            employees = towns[n].employees
            car_capacity = sorted(towns[n].car_capacity, reverse=True)

            for drivers, capacity in enumerate(car_capacity, start=1):
                employees -= capacity
                if employees <= 0:
                    cars_driven.append(drivers)
                    break
            else:
                # If all employees cannot fit in all cars, there is no solution
                return None

    return cars_driven


def run(lines):
    output = []

    # Number of test cases
    C = int(lines.popleft())
    for c in range(C):
        # Number of towns and office location
        N, T = [int(x) for x in lines.popleft().split()]

        # Number of employees
        E = int(lines.popleft())

        # Employees
        employees = []
        for e in range(E):
            # Hometown and number of passengers
            H, P = [int(x) for x in lines.popleft().split()]
            employees.append((H-1, P))

        cars_driven = run_one(N, T-1, employees)

        if cars_driven is None:
            display = 'IMPOSSIBLE'
        else:
            display = ' '.join([str(car) for car in cars_driven])

        output.append('Case #{0}: {1}'.format(c + 1, display))

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
