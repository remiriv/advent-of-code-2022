import numpy as np
import copy

with open('day9/day9.txt') as file:
    lines = [line.strip() for line in file]
    result = []

    grid = [["." for col in range(2000)] for row in range(2000)]
    positions = [(1000, 1000) for i in range(0, 10)]
    result.append(positions[9])

    for line in lines:
        values = line.split(" ")
        if values[0] == 'U':
            for i in range(0, int(values[1])):
                initials = [copy.deepcopy(positions[0])]
                for b in range(0, len(positions)-1):
                    initials.append(copy.deepcopy(positions[b+1]))
                    if b == 0:
                        positions[b] = (positions[b][0], positions[b][1] + 1)
                    if positions[b+1][1] >= initials[-2][1]:
                        continue
                    elif positions[b+1][0] == initials[-2][0]:
                        positions[b+1] = (positions[b+1][0], positions[b+1][1] + 1)
                    elif positions[b+1][0] < initials[-2][0]:
                        positions[b+1] = (positions[b+1][0] + 1, positions[b+1][1] + 1)
                    elif positions[b+1][0] > initials[-2][0]:
                        positions[b+1] = (positions[b+1][0] - 1, positions[b+1][1] + 1)

                result.append(positions[9])
                print(positions)

        if values[0] == 'D':
            for i in range(0, int(values[1])):
                initials = [copy.deepcopy(positions[0])]
                for b in range(0, len(positions)-1):
                    initials.append(copy.deepcopy(positions[b+1]))
                    if b == 0:
                        positions[b] = (positions[b][0], positions[b][1] - 1)
                    if positions[b+1][1] <= initials[-2][1]:
                        continue
                    elif positions[b+1][0] == initials[-2][0]:
                        positions[b+1] = (positions[b+1][0], positions[b+1][1] - 1)
                    elif positions[b+1][0] < initials[-2][0]:
                        positions[b+1] = (positions[b+1][0] + 1, positions[b+1][1] - 1)
                    elif positions[b+1][0] > initials[-2][0]:
                        positions[b+1] = (positions[b+1][0] - 1, positions[b+1][1] - 1)

                result.append(positions[9])
                print(positions)

        if values[0] == 'L':
            for i in range(0, int(values[1])):
                initials = [copy.deepcopy(positions[0])]
                for b in range(0, len(positions)-1):
                    initials.append(copy.deepcopy(positions[b+1]))
                    if b == 0:
                        positions[b] = (positions[b][0] - 1, positions[b][1])
                    if positions[b+1][0] <= initials[-2][0]:
                        continue
                    elif positions[b+1][1] == initials[-2][1]:
                        positions[b+1] = (positions[b+1][0] - 1, positions[b+1][1])
                    elif positions[b+1][1] < initials[-2][1]:
                        positions[b+1] = (positions[b+1][0] - 1, positions[b+1][1] + 1)
                    elif positions[b+1][1] > initials[-2][1]:
                        positions[b+1] = (positions[b+1][0] - 1, positions[b+1][1] - 1)

                result.append(positions[9])
                print(positions)

        if values[0] == 'R':
            for i in range(0, int(values[1])):
                initials = [copy.deepcopy(positions[0])]
                for b in range(0, len(positions)-1):
                    initials.append(copy.deepcopy(positions[b+1]))
                    if b == 0:
                        positions[b] = (positions[b][0] + 1, positions[b][1])
                    if positions[b+1][0] >= initials[-2][0]:
                        continue
                    elif positions[b+1][1] == initials[-2][1]:
                        positions[b+1] = (positions[b+1][0] + 1, positions[b+1][1])

                    elif positions[b+1][1] < initials[-2][1]:
                        positions[b+1] = (positions[b+1][0] + 1, positions[b+1][1] + 1)

                    elif positions[b+1][1] > initials[-2][1]:
                        positions[b+1] = (positions[b+1][0] + 1, positions[b+1][1] - 1)

                result.append(positions[9])

    print(len(list(set(result))))

'''
'''