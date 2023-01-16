import numpy as np
import copy
from math import floor


def add_to_result(c, r, v):
    if c in [20, 60, 100, 140, 180, 220]:
        print(c)
        print(r)
        print(v)
        return r + c * v
    return r


def is_dot_or_not(val, cyc):
    if (cyc - 1) % 40 in [val-1, val, val+1]:
        return "#"
    return '.'


with open('day10/day10.txt') as file:
    lines = [line.strip() for line in file]
    cycle = 0
    result = 0
    value = 1
    displayedResult = [[] for i in range(0, 6)]

    for line in lines:
        lineValue = line.split(" ")
        if lineValue[0] == 'noop':
            cycle += 1
            displayedResult[floor((cycle-1) / 40)].append(is_dot_or_not(value, cycle))
        if lineValue[0] == 'addx':
            cycle += 1
            displayedResult[floor((cycle-1) / 40)].append(is_dot_or_not(value, cycle))
            cycle += 1
            displayedResult[floor((cycle-1) / 40)].append(is_dot_or_not(value, cycle))
            value += int(lineValue[1])
    for i in range(0, 6):
        print(' '.join(displayedResult[i]))

''' PART 1

    lines = [line.strip() for line in file]
    cycle = 0
    result = 0
    value = 1

    for line in lines:
        lineValue = line.split(" ")
        if lineValue[0] == 'noop':
            cycle += 1
            result = add_to_result(cycle, result, value)
        if lineValue[0] == 'addx':
            cycle += 1
            result = add_to_result(cycle, result, value)
            cycle += 1
            result = add_to_result(cycle, result, value)
            value += int(lineValue[1])
    print(result)

'''