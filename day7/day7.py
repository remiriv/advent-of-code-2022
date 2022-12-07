import subprocess
from collections import defaultdict
from functools import reduce
from operator import add

with open('day7/day7.txt') as file:
    lines = [line for line in file]
    result = defaultdict(int)
    dirs = []
    is_list = False

    for line in lines:
        line_elements = line.strip().split(' ')
        if line_elements[0] == "$" and line_elements[1] == "cd":
            if line_elements[2] == "..":
                dirs.pop()
            else:
                dirs.append(line_elements[2])
        else:
            if line_elements[0] == "$":
                pass
            elif line_elements[0] == "dir":
                pass
            else:
                for i in range(len(dirs)):
                    result['/'.join(dirs[:i + 1])] += int(line_elements[0])

    total = sorted([(key, result[key]) for key in result.keys()])

    true_total = sum([value for key, value in total if value <= 100000])

    unused = 70000000 - result['/']
    print(sorted([value for key, value in total if value > 30000000 - unused ])[0])