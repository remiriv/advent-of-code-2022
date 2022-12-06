def getLastNValues(line, start, number):
    resultSet = set()
    for i in range(number):
        resultSet.add(line[start-i])

    if len(resultSet) == number:
        return start + 1


with open('day6/day6.txt') as file:
    lines = [line for line in file]
    result = 0
    first_line = lines[0]

    for index, value in enumerate(first_line):
        if index < 3:
            pass

        length = getLastNValues(first_line, index, 14)
        if length:
            print(length)
            break
'''

'''