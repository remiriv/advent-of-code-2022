import subprocess
from collections import defaultdict
from functools import reduce
from operator import add


def is_visible(direction, lines, line, value, index):
    if direction == 'left':
        for i in range(index):
            if line[i] >= value:
                return False
        return True
    if direction == 'right':
        for i in range(index+1, len(line)):
            if line[i] >= value:
                return False
        return True
    if direction == 'up':
        for otherLine in lines:
            if otherLine == line:
                return True
            if otherLine[index] >= value:
                return False
        return True
    if direction == 'down':
        start = False
        for otherLine in lines:
            if otherLine == line:
                start = True
                continue
            if not start:
                continue
            if otherLine[index] >= value:
                return False
        return True


def max_vis(lines, line, value, index):
    left = 0
    right = 0
    up = 0
    down = 0

    for i in range(1, index+1):
        if index == 0:
            break
        left += 1
        if line[index-i] >= value:
            break

    for i in range(index+1, len(line)):
        if index == len(line)-1:
            break
        right += 1
        if line[i] >= value:
            break

    l_index = 0
    for ind, otherLine in enumerate(lines):
        if otherLine == line:
            l_index = ind
            break

    for j in range(1, l_index+1):
        if l_index == 0:
            break
        up += 1
        if lines[l_index-j][index] >= value:
            break

    start = False
    for otherLine in lines:
        if line == lines[len(lines)-1]:
            break

        if otherLine == line:
            start = True
            continue
        if not start:
            continue

        down += 1
        if otherLine[index] >= value:
            break

    return left * up * down * right


with open('day8/day8.txt') as file:
    lines = [line.strip() for line in file]
    max = 0

    for line in lines:
        for index, value in enumerate(line):
            visibility = max_vis(lines, line, value, index)
            if visibility > max:
                max = visibility

    print(max)


'''
with open('day8/day8.txt') as file:
    lines = [line.strip() for line in file]
    result = len(lines) * 2

    print(len(lines))
    print(result)
    print(len(lines[0]))

    for line in lines:
        for index, value in enumerate(line):
            print(line)
            print(index)
            if index == 0:
                continue
            if index == len(line) - 1:
                continue
            print(is_visible('left', lines, line, value, index) or is_visible('right', lines, line, value, index) or is_visible('up', lines, line, value, index) or is_visible('down', lines, line, value, index))
            if is_visible('left', lines, line, value, index) or is_visible('right', lines, line, value, index) or is_visible('up', lines, line, value, index) or is_visible('down', lines, line, value, index):
                result += 1

    print(result)
'''