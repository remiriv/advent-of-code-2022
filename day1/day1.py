with open('day1/day1.txt') as file:
    lines = file.readlines()
    values = []
    current = 0
    for line in lines:
        value = line.strip()
        if value.isdigit():
            current += int(value)
        else:
            values.append(current)
            current = 0

    values.sort(reverse=True)
    print(values)
    print(values[0]+values[1]+values[2])