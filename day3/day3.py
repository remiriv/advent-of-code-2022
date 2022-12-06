with open('day3/day3.txt') as file:
    lines = [line.strip() for line in file]
    print(lines)

    result = 0
    for (index, line) in enumerate(lines, start=1):
        if index % 3 == 0:
            same = [value for value in line if value in lines[index-2] and value in lines[index-3]][0]
            number_same = ord(same) - 96 if same.lower() == same else ord(same) - 64 + 26
            result += number_same

    print(result)
'''
    for line in lines:
        comp1 = line[:len(line)/2]
        comp2 = line[len(line)/2:]
        diff = [value for value in comp1 if value in comp2][0]
        number_diff = ord(diff) - 96 if diff.lower() == diff else ord(diff) - 64 + 26
        result += number_diff

    print(result)
'''
