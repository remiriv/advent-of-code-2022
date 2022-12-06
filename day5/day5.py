import re

with open('day5/day5.txt') as file:
    lines = [line for line in file]
    result = 0
    piles = [[] for _ in range(10)]
    for (index, line) in enumerate(lines):
        if line.strip().startswith('1'):
            stop_index = index + 1
            break

        for i in range(0, 9):
            if line[1 + 4 * i] != " ":
                piles[i+1].insert(0, line[1 + 4 * i])

    for (index, line) in enumerate(lines):
        if index > stop_index:
            move, start, end = [int(s) for s in re.findall(r'\b\d+\b', line)]

            piles[end].extend(piles[start][-move:])
            piles[start] = piles[start][0:-move]
    print("final", [crate[-1] for crate in piles[1:]])
'''

    lines = [line for line in file]
    result = 0
    piles = [[] for _ in range(10)]
    for (index, line) in enumerate(lines):
        if line.strip().startswith('1'):
            stop_index = index + 1
            break

        for i in range(0, 9):
            if line[1 + 4 * i] != " ":
                piles[i+1].insert(0, line[1 + 4 * i])

    print(piles)
    for (index, line) in enumerate(lines):
        if index > stop_index:
            move, start, end = [int(s) for s in re.findall(r'\b\d+\b', line)]
            for i in range(0, move):
                piles[end].append(piles[start].pop())
    print("final", [crate[-1] for crate in piles[1:]])
'''